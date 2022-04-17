# Use this boot file to import all of the files to be run

try:
    import usocket as socket
except:
    import socket

import esp
esp.osdebug(None)

import gc
import usocket as socket
import network
import time
from MicroWebSrv2 import *
from time import sleep

#import linear_actuator
import csv
#import time_elapsed

# OLED Display Includes
#import OLED_Library
#from machine import Pin, SoftI2C

gc.collect()

ssid = 'MicroPython AP'
password = '123456789'
IP_Website = '192.168.6.9'
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, authmode=3, password=password)

# This Line is causing the ELF issue
ap.ifconfig(('192.168.6.9', '255.255.255.0', '192.168.0.1', '8.8.8.8'))

print('Connection successful')
print(ap.ifconfig())

"""
##############################################
# ESP32 Pin assignment 

i2c = SoftI2C(scl=Pin(15), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = OLED_Library.SSD1306_I2C(oled_width, oled_height, i2c)
oled.text(IP_Website, 0, 0)
oled.text(ssid, 0, 21)
oled.text(password, 0, 42)
oled.show()


##########################################
"""
"""
import framebuf

counter = 0
pic = 'wicked.pbm'

while True:
  with open(pic, 'rb') as f:
    f.readline() # Magic number
    f.readline() # Creator comment
    f.readline() # Dimensions
    data = bytearray(f.read())
  fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

  #oled.invert(1)
  oled.framebuf.blit(fbuf, 0, 0)

"""
"""
oled.text(IP_Website, 0,20)
oled.text(ssid, 0, 40)
oled.text(password, 0, 60)
"""
"""
  count = counter % 4
  oled.show()
  if count == 0:
    pic = 'supreme.pbm'
  elif count == 1:
    pic = 'amogus.pbm'
  elif count == 2:
    pic = 'wicked.pbm'
  else:
    pic = 'FortniteF.pbm'

  counter += 1

  sleep(5)
  """
#############################################

# sleep(5)
#import csv
csv.create_csv(1)
#csv.add_parameter(12.45, 1.37, 13.21, 12.23, 1.73, 11.34)
#import RS232      # Simply Modbus
#import linear_actuator

##############################################

import website
