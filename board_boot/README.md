# folder for ESP32 boot files.
Here are the files that will be stored on the ESP's on-board memory.

# flash instructions
To start off, clone the MicroPython (v1.18) repository:

```
$ git clone --recursive https://github.com/micropython/micropython
```

Navigate to `/ports/esp32` and follow the instructions to flash the custom firmware. 

Additionally, MicroWebSrv2 (v2.0.6) is also used so you should also clone the repository:

```
$ git clone --recursive https://github.com/jczic/MicroWebSrv2
```

Move only the `/MicroWebSrv2` folder into `/ports/esp32/modules`