import machine
from time import sleep
import time
import time_elapsed
"""
def Move_Actuator(position: int):
    """

Down = machine.Pin(25, machine.Pin.OUT)     #Green LED
Down.off()
Up = machine.Pin(26, machine.Pin.OUT)       # Red LED
Up.off()
pos_bottom = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
pos_top = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

cur_pos = 0

def total_travel_time():
    while(pos_bottom.value() == 1):
        Down.on()

    start = time_elapsed.elapsed_time_seconds()
    Down.off()

    while(pos_top.value() == 1):
        Up.on()
    
    end = time_elapsed.elapsed_time_seconds()
    Up.off()

    return (end - start)

def move_actuator(new_pos: int) -> None:
    z = new_pos - cur_pos
    fifteen_sec = time.time() + 15
    if(z < 0):
        while (time.time() < ((fifteen_sec) * abs(z)) ):
            if((pos_bottom.value() == 0) or (pos_top.value() == 0)):
                Down.off()
            Down.on()
    else:
        while (time.time() < ((fifteen_sec) * abs(z)) ):
            if((pos_bottom.value() == 0) or (pos_top.value() == 0)):
                Up.off()
            Up.on()

def calibrate_actuator():
    while(pos_bottom.value() == 1):
        Down.on()
    Down.off()
    while (pos_bottom.value() == 0):
        Up.on()
    Up.off()

#move_actuator(50)
print("Yeet")
print(total_travel_time())
calibrate_actuator()