import machine
import time

Down = machine.Pin(25, machine.Pin.OUT)     # Wire without the blue tape
Down.off()                                  # Connect to the 5V power supply
Up = machine.Pin(26, machine.Pin.OUT)       # Wire with the blue tape
Up.off()
pos_bottom = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)       # Top sensor
pos_top = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)          # Bottom Sensor

cur_pos = int(0)

def total_travel_time() -> float:           # Measures the time for the linear actuator to go from the bottom hall sensor to the top hall sensor
    while(pos_bottom.value() == 1):
        Down.on()

    start = time.time()
    Down.off()

    while(pos_top.value() == 1):
        Up.on()
    
    end = time.time()
    Up.off()

    return round((end - start), 3)

def calibrate_actuator():                   # Sets the 
    while(pos_bottom.value() == 1):
        Down.on()
    Down.off()
    while (pos_bottom.value() == 0):
        Up.on()
    Up.off()

max_time = total_travel_time()
print(max_time)
calibrate_actuator()

def go_up():
    while True:
        Up.on()

def move_actuator(new_pos: int) -> None:
    global cur_pos
    if((new_pos > 100) or (new_pos < 0)):
        print("Position of acuator cannot be greater than 100.")
        return
    z = (new_pos - cur_pos)/100 * max_time
    print(z, " + ", new_pos, " + ", cur_pos)
    cur_pos = new_pos
    #time_range = time.time() + max_time
    if(z < 0):
        now = time.time()
        while (time.time() < (now + abs(z))):
            if((pos_bottom.value() == 0) or (pos_top.value() == 0)):
                print("Sensor Detected")
                Down.off()
                break
            Down.on()
    else:
        now = time.time()
        while(time.time() < ( now + abs(z) )  ):
            if((pos_bottom.value() == 0) or (pos_top.value() == 0)):
                Up.off()
                print("Sensor Detected")
                break
            Up.on()
    Down.off()
    Up.off()

#move_actuator(50)
