# microgrid (wip readme)
This repository contains the code for my senior design project. The focus of this project is a "feasibility study of microgrids for load interfaces".
The project runs off two ESP32's. One of the ESP32's host the server runs Micropython using MicroWebSrv2 for its backend framework. 

# file description
- python scripts
 - boot.py : default file the ESP32 looks for on startup
 - AP.py : creates access point for the server
 - website.py : MicroWebSrv2 instance for web routing
 - misc. files
   - csv.py : creates and manages datapoints while the server is active
   - RS232.py : sends data to the ESP32 from the solar charge controller
   - linear_actuator.py : send commands to the Arduino to move the linear actuator up or down for the solar panel
   - time_elapsed.py : starts a timer for the session for data logging purposes

# usage
1. Flash the firmware onto the device
2. Flash boot.py to the board using [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy)
3. Turn on any hardware needed
4. Open the ESP32 to your terminal/command line/whatever
5. Click the reset button on the board
6. Go to the IP address shown

# contributors
Project Sponsor: Eric Hamke
Project Manager: Anna Janicek
Wind turbine design and setup: Zinah Alsaad, Illiana Tafoya
Website design, server setup, solar charge controller setup: Luis Estrada, Andrew Zhang