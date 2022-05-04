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

import csv

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


csv.create_csv(1)
csv.add_parameter(0, 0, 0, 0, 0)


import website
