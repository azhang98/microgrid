# microgrid (wip readme)
This repository contains the code for our senior design project. The focus of this project is to "investigate the feasibility of an internet-of-things approach to the monitoring and controlling a power management system".   

The project runs off three ESP32's. Two of the ESP32's host the server runs MicroPython using MicroWebSrv2 for its framework with one of them used to show server information. The other ESP32 runs on C and is used to control the wind turbine and battery. 

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
- JS files: uses fetch API/RESTful design patterns to read and update the graph 

# usage
1. Flash the firmware onto the device. Refer to [`/board_boot`](https://github.com/Cutherean/microgrid/tree/main/board_boot) for instructions
2. Flash `boot.py` and `sdcard.py` to the board using [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy)
3. Turn on any hardware needed
4. Open the ESP32 to your terminal/command line/whatever
5. Click the reset button on the board
6. Go to the IP address shown

# contributors
**Project Sponsor**: [Eric Hamke](https://github.com/ehamke)  
**Project Manager**: Anna Janicek  
**Wind turbine design and setup**: Zinah Alsaad, [Illiana Tafoya](https://github.com/ilianatafoya)  
**Website design, server setup, solar charge controller setup**: [Luis Estrada](https://github.com/DragonPenguin), [Andrew Zhang](https://github.com/Cutherean)