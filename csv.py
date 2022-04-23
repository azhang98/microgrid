import time_elapsed

u_id = 1
num = 1

# make uid for other purposes
def increment() -> None:
    global u_id
    u_id += 1

# create file
def create_csv(num) -> None:
    incre = 0
    while True:
        try:          
            global filename1
            filename1 = str(num) + "_" + "data.csv"
            # create file if it does not exist
            with open(filename1, 'x') as file:
                file.write('ID,Time,Solar_Voltage,Solar_Current,Solar_Battery_Voltage,Wind_Voltage,Wind_Current,Wind_Battery_Voltage\r')
                global file_num
                file_num = num
                #with open("filename.txt", 'w') as file2:
                #    file2.write(filename)
                return
        except:
            # except error if file exists
            print("File already exists")
            print(num)
            num = num + 1
            pass

def add_parameter(s_volt: float, s_cur: float, s_batt: float, w_volt: float, w_cur: float, w_batt: float) -> None:
    # add line of data to csv file
    # id, time elapsed, solar voltage, solar current, solar battery, wind voltage, wind current, wind current
    with open((str(file_num) + "_" + "data.csv"), 'a') as file:
        file.write('\n' + str(u_id) + ',' + time_elapsed.elapsed_time() + ',' +
            str(s_volt) + ',' + str(s_cur) + ','+
            str(s_batt) + ','+ str(w_volt) + ',' + str(w_cur) + ',' + str(w_batt) + '\r')
        increment()