#include <Wire.h>

#include "ESPAsyncWebServer.h"
#include "WiFi.h"
#include "heltec.h"
//#include <WiFi.h>
#include <Adafruit_INA219.h>
#include <ArduinoJson.h>
#include <HTTPClient.h>

#define RXDS 16
#define TXDS 17

Adafruit_INA219 ina219;

// void getvoltage_Generator();
void getvoltage_Battery();
void getcurrent_Battery();
void getRPM();
String httpGETRequest(const char* serverName);

int ADC = 0;
float RPM;
float interruptCounter = 0;
float batteryVoltage = 0;
float current_mA = 0;
String PWM;  // PWM
float PWM_wind;
float BatteryCharged = 12;  // at 12V battery is fully charged

// server ESP32
const char* ssid = "MicroPython AP";
const char* password = "123456789";
AsyncWebServer server(80);

String readBatteryVoltage() {
    return String(batteryVoltage);
}

String readRPM() {
    return String(RPM);
}

String readCurrent() {
    return String(current_mA);
}

void setup() {
    // setup Heltic OLED
    pinMode(LED, OUTPUT);
    digitalWrite(LED, LOW);

    Heltec.begin(true /*DisplayEnable Enable*/, false /*LoRa Enable*/, true /*Serial Enable*/);
    delay(2000);

    // setup Adafruit IN219
    Serial.begin(115200);
    while (!Serial) {
        delay(1);
    }
    uint32_t currentFrequency;

    // Initialize OLED display SSD1306
    Wire.begin(SDA_OLED, SCL_OLED);  // Scan OLED’s I2C address via I2C0
    Heltec.display->init();

    // check INA219 on the I2C0 bus
    int address = 0x40;  // address of INA219
    Wire.beginTransmission(address);
    // error = Wire.endTransmission();

    // Initialize the INA219.

    // arduino mega serial connection setup
    Serial2.begin(9600, SERIAL_8N1, RXDS, TXDS);
    while (!Serial2);

    Serial.begin(115200);

    // connect to server ESP32
    WiFi.begin(ssid, password);
    Serial.println("Connecting");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.print("Connected to WiFi network with IP Address: ");

    server.on("/BatteryVoltage", HTTP_GET, [](AsyncWebServerRequest* request) {
        request->send_P(200, "text/plain", readBatteryVoltage().c_str());
    });

    server.on("/Current", HTTP_GET, [](AsyncWebServerRequest* request) {
        request->send_P(200, "text/plain", readCurrent().c_str());
    });

    server.on("/RPM", HTTP_GET, [](AsyncWebServerRequest* request) {
        request->send_P(200, "text/plain", readRPM().c_str());
    });
}

void loop() {
    // get PWM from web based ESP32 and send PMW value to arduino mega
    const char* MicroPythonAPPWM = "http://192.168.6.9/wind-PWM";
    unsigned long previousMillis = 0;
    const long interval = 2000;
    unsigned long int currentMillis = millis();
    char Buf[10];

    if (currentMillis - previousMillis >= interval) {
        // Check WiFi connection status
        if (WiFi.status() == WL_CONNECTED) {
            PWM = httpGETRequest(MicroPythonAPPWM);
            PWM.toCharArray(Buf, 10);
            Serial.println("PWM: " + PWM);
        } else {
            Serial.println("WiFi Disconnected");
        }
    }

    // disable check - if battery is fully charged disable
    if (batteryVoltage >= BatteryCharged) {
        Serial2.write(0);  // send PWM value of 0 to Arduino Mega - disable
    } else {
        Serial2.write(10);
        // Serial2.write(Buf); //write PWM value to arduino mega
    }
    getvoltage_Battery();
    getcurrent_Battery();
    getRPM();

    httpPOSTRequest("http://192.168.6.9/wind-data");

    delay(500);

    Heltec.display->clear();
}

void getvoltage_Battery() {
    /*  ADC = analogRead(39);
      batteryVoltage = (ADC * 3.3) / 4095; */

    int shuntvoltage = ina219.getShuntVoltage_mV();
    int busvoltage = ina219.getBusVoltage_V();
    batteryVoltage = busvoltage + (shuntvoltage / 1000);

    Serial.print("Battery Voltage = ");
    Serial.println(batteryVoltage);
    // delay(500);
    /*
     Heltec.display -> drawString(0,20, "Battery");
     Heltec.display -> drawString(0,30, "Voltage = ");
     Heltec.display -> drawString(50,30,(String) batteryVoltage);
     Heltec.display -> drawString(80,30, "V");
     Heltec.display -> display();
     */
    // delay(500);
    // Heltec.display -> clear();
}

void getcurrent_Battery() {
    // shunt
    // current_mA = ((batteryVoltage)/(0.024))/100

    current_mA = ina219.getCurrent_mA();

    Serial.print("Battery Current = ");
    Serial.println(current_mA);
    /*
     Heltec.display -> drawString(0,30, "Battery");
     Heltec.display -> drawString(0,40, "Current = ");
     Heltec.display -> drawString(50,40,(String) current_mA);
     Heltec.display -> drawString(80,40, "mA");
     Heltec.display -> display();
     */
}

void getRPM() {
    // get RPM value from Arduino mega
    while (Serial2.available() != 0) {
        RPM = Serial2.read();
    }

    Serial.print("RPM = ");
    Serial.println(RPM);
    /*
     Heltec.display -> drawString(0,50, "RPM =");
     Heltec.display -> drawString(40,50,(String) RPM);
     Heltec.display -> drawString(60,50, "rpm");
     Heltec.display -> display();
    */
}

String httpGETRequest(const char* MicroPythonAP) {
    HTTPClient http;

    // Your IP address with path or Domain name with URL path
    http.begin(MicroPythonAP);

    // Send HTTP POST request
    int httpResponseCode = http.GET();

    String payload = "--";

    if (httpResponseCode > 0) {
        Serial.print("HTTP Response code: ");
        Serial.println(httpResponseCode);
        payload = http.getString();
    } else {
        Serial.print("Error code: ");
        Serial.println(httpResponseCode);
    }
    // Free resources
    http.end();

    return payload;
}

void httpPOSTRequest(const char* MicroPythonAP) {
    HTTPClient http;
    http.begin(MicroPythonAP);

    http.addHeader("Content-Type", "application/json");
    // Prepare JSON document
    DynamicJsonDocument doc(2048);

    doc["voltage"] = readBatteryVoltage();
    doc["current"] = readCurrent();

    // Serialize JSON document
    String json;
    serializeJson(doc, json);

    http.POST(json);
}