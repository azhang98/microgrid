#from encodings import utf_8
#import os
#from machine import UART
from machine import Pin, UART
from time import sleep

uart = UART(2, 9600)


def Read_Panel_Battery_Voltage():
    read_battery_voltage = bytearray([0x01, 0x03, 0x01, 0x01, 0x00, 0x01, 0xD4, 0x36])
    uart.write(read_battery_voltage)
    sleep(1)
    buf = uart.read()
    print(buf)
    batt_volt = (int.from_bytes(buf[4:5], "big") * 0.1)
    return batt_volt

def Read_Panel_Voltage():
    read_panel_voltage = bytearray([0x01, 0x03, 0x01, 0x07, 0x00, 0x03, 0xB5, 0xF6])
    uart.write(read_panel_voltage)
    sleep(0.5)
    #buf = uart.read()
    #print(buf)
    #panel_volt = (int.from_bytes(buf[4:5], "big") * 0.1)
    #print(panel_volt)
    #panel_current = (int.from_bytes(buf[5:6], "big") * 0.01)
    #print(panel_current)
    #panel_volt_current = [panel_volt, panel_current]
    #return panel_volt_current
    #return panel_volt

def Read_Panel_Current():
    read_panel_current = bytearray([0x01, 0x03, 0x01, 0x08, 0x00, 0x02, 0x44, 0x35])
    uart.write(read_panel_current)
    sleep(0.5)
    #buf = uart.read()
    #print(buf)
    #panel_current = (int.from_bytes(buf[4:6], "big") * 0.01)
    #print(panel_current)
    #return panel_current
    #print(panel_volt_current)

Read_Panel_Battery_Voltage()
Read_Panel_Voltage()
Read_Panel_Current()
#print(Read_Panel_Battery_Voltage())
#print(Read_Panel_Voltage())
#print(Read_Panel_Current())


#  Recieve input from RS232 port and echo it back to through the UART/ Write it to the text file
"""
print("yeet")
while True:
    log = open("yeet.txt", "a")
    #print(buf)
    if(uart.any() > 0):
        buf = uart.read()
        buf = str(buf)
        #buf = buf.decode(utf_8)
        log.write(buf)
        log.close() 
        uart.write(buf[2])
"""

"""
oled_width = 128
oled_height = 64
oled = OLED_Library.SSD1306_SPI(oled_width, oled_height, i2c)
"""


#while True:
#    uart.write('ECE')
