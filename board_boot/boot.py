import os
from machine import Pin, SoftSPI
from sdcard import SDCard

spisd = SoftSPI(-1, miso=Pin(19), mosi=Pin(23), sck=Pin(18))
sd = SDCard(spisd, Pin(5))

vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
os.chdir('sd')

print('\n\n\n\n\n')

import AP