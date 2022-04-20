/*==========================================================================
  //  Author      : Handson Technology
  //  Project     : BTD7960 Motor Control Board driven by Arduino.
  //  Description : Speed and direction controlled by a potentiometer attached
  //      to analog input A0. One side pin of the potentiometer (either one) to
  //      ground; the other side pin to +5V
  //  Source-Code : BTS7960.ino
  //  Program: Control DC motors using BTS7960 H Bridge Driver.
  //==========================================================================
  //  Connection to the BTS7960 board:
  //  BTS7960 Pin 1 (RPWM) to Arduino pin 5(PWM)
  //  BTS7960 Pin 2 (LPWM) to Arduino pin 6(PWM)
  //  BTS7960 Pin 3 (R_EN), 4 (L_EN), 7 (VCC) to Arduino 5V pin
  //  BTS7960 Pin 8 (GND) to Arduino GND
  //  BTS7960 Pin 5 (R_IS) and 6 (L_IS) not connected
*/

#include <Wire.h>
#include "RTClib.h"

RTC_DS3231 rtc;

int posVoltagePin = A0;
int negVoltagePin = A1;
int posVoltage = 0;  // variable to store the value read
int negVoltage = 0;  // variable to store the value read

volatile unsigned clockTicks = 0;
volatile byte flag = false;
volatile byte speedChange = false;
volatile unsigned RPM_Ticks = 0;
volatile unsigned RPM = 0;
volatile unsigned Ticks = 0;
static int motorSpeed = 0;

double RPS = 0;
int speed = 0;

const int RPWM_Output = 2;     // Arduino PWM output pin 5; connect to IBT-2 pin 1 (RPWM)
const int LPWM_Output = 3;     // Arduino PWM output pin 6; connect to IBT-2 pin 2 (LPWM)
const int IR_TACH_Input = 19;  // IR Sensor input for Tachometer
const int rtcTimerIntPin = 18; // RTC Square Wave input for Timer

void isrTACH() {
  //noInterrupts ();
  //flag = true;
  //Ticks = clockTicks;
  RPM_Ticks++;
  //clockTicks = 0;
  //interrupts ();
}

void rtc_interrupt()
{
  clockTicks++;
//  flag = true;
  // Ticks = RPM_Ticks;
//   RPM_Ticks = 0;
}  // end of rtc_interrupt

void setup()
{
  Serial.begin(115200);
  Serial3.begin(9600);
  
  while (!Serial);

  if (! rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);
  }

  if (rtc.lostPower()) {
    Serial.println("RTC lost power, lets set the time!");
    // following line sets the RTC to the date & time this sketch was compiled
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }

  // enable the 4kHz output
  rtc.writeSqwPinMode (DS3231_SquareWave4kHz);

  pinMode(RPWM_Output, OUTPUT);
  pinMode(LPWM_Output, OUTPUT);
  pinMode(IR_TACH_Input, INPUT);
  pinMode (rtcTimerIntPin, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt (IR_TACH_Input), isrTACH, RISING);   //interrupt pin
  /* attachInterrupt (digitalPinToInterrupt (rtcTimerIntPin), rtc_interrupt, RISING); */
  
  Serial.println("Speed -60 to 60");
}

void loop()
{
  posVoltage = analogRead(posVoltagePin);  // read the input pin
  negVoltage = analogRead(negVoltagePin);  // read the input pin
  
  if (motorSpeed != 0){
   RPM =  RPS * 60; //1/(double(RPM_Ticks)/4000/60);  // ticks * (1 sec/4000 ticks) * (1 min/ 60 sec)*/
    RPS = Ticks;
    Serial3.write(RPM);
    
    Serial.print(motorSpeed);
    Serial.print(" ");
    Serial.print(RPM_Ticks);
    Serial.print(" ");
    Serial.print(posVoltage);
    Serial.print(" ");
    Serial.print(negVoltage);
    Serial.print(" ");
    Serial.println(double(clockTicks)-4098,4);
    flag = false; 
    clockTicks = 0;
    RPM_Ticks = 0;
    Ticks = 0;
  }

  delay(1000);

 /*if (Serial.available()) {               // If user input new speed
    speed = Serial.parseInt();
    Serial.read(); */

    speed = Serial3.read();
    Serial.println(speed);
    if (speed >= -60 && speed <= 60) {
      motorSpeed = speed;
      speedChange = true;
    }


  if (speedChange) {
    // Motor rate is from -60 to 60
    if (motorSpeed < 0) {
      // reverse rotation
      int reversePWM = -motorSpeed;
      analogWrite(LPWM_Output, reversePWM);
      analogWrite(RPWM_Output, 0);
      speedChange = false;
     }
     else {
     // forward rotation
     int forwardPWM = motorSpeed;
     analogWrite(LPWM_Output, 0);
     analogWrite(RPWM_Output, forwardPWM);
     speedChange = false;
     }
  }
}
