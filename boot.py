#import machine, sdcard, os

#sd = machine.SDCard(slot = 2, width = 1, cd = None, wp = None, sck = machine.Pin(18), miso = machine.Pin(19), mosi = machine.Pin(23), cs = machine.Pin(5), freq = 4000000)
#sd = machine.SDCard(slot = 2)

#os.mount(sd, '/sd')

#os.listdir('/')
#os.unmount('/sd')

import os
from machine import Pin, SoftSPI
from sdcard import SDCard

Lin_Down = Pin(21, Pin.OUT)     #Green LED
Lin_Up = Pin(22, Pin.OUT)       # Red LED
Lin_Down.off()
Lin_Up.off()

spisd = SoftSPI(-1, miso=Pin(19), mosi=Pin(23), sck=Pin(18))
sd = SDCard(spisd, Pin(5))


#print('\nRoot directory:{}'.format(os.listdir()))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
#print('Root directory:{}'.format(os.listdir()))
os.chdir('sd')
#print('SD Card contains:{}'.format(os.listdir()))
print('\n\n\n\n\n')

import AP