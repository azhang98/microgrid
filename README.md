# microgrid
This repository contains the code for our senior design project. The focus of this project is to "investigate the feasibility of an internet-of-things approach to the monitoring and controlling a power management system".   

The project runs off three ESP32's. Two of the ESP32's host the server runs MicroPython using MicroWebSrv2 for its framework with one of them used to show server information. The other ESP32 runs on C and is used to control the wind turbine and battery. 

The wind charge controller charges a 12V DC battery. The wind charge controller ESP32 takes current and voltage readings using a Adafruit INA219 sensor. It also communicates with the Arduino mega on the work bench to receive RPM readings. These readings are passed the the web based interface. The two ESP32 communicate through a client/server connection. 

# file description
- python scripts
  - `boot.py` : default file the ESP32 looks for on startup
  - `AP.py` : creates access point for the server
  - `website.py` : MicroWebSrv2 instance for web routing
  - misc. files
    - `csv.py` : creates and manages datapoints while the server is active
    - `RS232.py` : sends data to the ESP32 from the solar charge controller
    - `linear_actuator.py` : send commands to the Arduino to move the linear actuator vertically for the solar panel
    - `time_elapsed.py` : starts a timer for the session for data logging purposes
- JS files: uses fetch API/RESTful design to read and update the graph 
- Hardware Design 
    - `WindChargeContollerESP32.ino` : takes current and voltage readings of battery. receives rpm value from arduino mega and passes all data to web based ESP32. send user input pwm to arduino mega. enable/disable functionality 
    - `MotorControllerTest_2.ino` : code for arduino mega on work bench. takes rpm reading and controls pwm values sent to generator 
    - Schematics & Simulatons: circuit design
    - Wind Charge Conroller Improvements : suggested improvements for future iterations 
# usage
1. Flash the firmware onto the device. Refer to [`/board_boot`](https://github.com/Cutherean/microgrid/tree/main/board_boot) for instructions
2. Flash `boot.py` and `sdcard.py` to the board using [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy)
3. Turn on any hardware needed
    1. Note: connect the RS232 cable before the solar charge controller is on or while they are both on
4. Connect the ESP32 to a power source or to a computer (if connecting to a computer you will need to use something like `screen` with a baud rate of 115200)
5. Click the reset button on the board
    1. A known issue is that you will need to reinsert the SD card after resetting the board
6. Go to the IP address shown

# contributors
**Project Sponsor**: [Eric Hamke](https://github.com/ehamke)  
**Project Manager**: Anna Janicek  
**Wind turbine design and setup**: Zinah Alsaad, [Iliana Tafoya](https://github.com/ilianatafoya)  
**Website design, server setup, solar charge controller setup**: [Luis Estrada](https://github.com/DragonPenguin), [Andrew Zhang](https://github.com/Cutherean)
