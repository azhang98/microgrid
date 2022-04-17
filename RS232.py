#from encodings import utf_8
#import os
#from machine import UART
#connectors should be black white red

# The ESP32 MUST BE powered on before being connected to the solar charge controller
# DO NOT connect the RS232 cable to the ESP Web server while it is powered off

from machine import UART
import time
uart = UART(2, 9600)

def send_battery_bytes() -> float:
    read_battery_voltage = bytes([0x01, 0x03, 0x01, 0x01, 0x00, 0x01, 0xd4, 0x36])
    uart.write(read_battery_voltage)
    buf = uart.read()
    return buf

def send_panel_voltage_bytes():
    read_panel_voltage = bytes([0x01, 0x03, 0x01, 0x07, 0x00, 0x01, 0x34, 0x37])
    uart.write(read_panel_voltage)
    buf = uart.read()
    return buf

def send_panel_current_bytes():
    read_panel_current = bytes([0x01, 0x03, 0x01, 0x08, 0x00, 0x01, 0x04, 0x34])
    uart.write(read_panel_current)
    buf = uart.read()
    return buf

def send_panel_power_bytes():
    read_panel_power = bytes([0x01, 0x03, 0x01, 0x09, 0x00, 0x01, 0x55, 0xF4])
    uart.write(read_panel_power)
    buf = uart.read()
    return buf

def get_battery_voltage():
    for x in range(2):
        temp = send_battery_bytes()
        time.sleep(0.1)
    batt_volt = (int.from_bytes(temp[4:5], "big") * 0.1)
    return batt_volt

def get_panel_voltage():
    for x in range(2):
        temp = send_panel_voltage_bytes()
        time.sleep(0.1)
    panel_volt = (int.from_bytes(temp[4:5], "big") * 0.1)
    return panel_volt

def get_panel_current():
    for x in range(2):
        temp = send_panel_current_bytes()
        time.sleep(0.1)
    panel_cur = (int.from_bytes(temp[4:5], "big") * 0.01)
    return panel_cur

def get_panel_power():
    for x in range(2):
        temp = send_panel_power_bytes()
        time.sleep(0.1)
    panel_cur = (int.from_bytes(temp[4:5], "big"))
    return panel_cur
