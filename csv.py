import time
import Time_Elapsed
#import RS232
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
            filename = str(num) + "_" + "data.csv"
            # create file if it does not exist
            with open(filename, 'x') as file:
                file.write('ID,Time,Solar_Voltage,Solar_Current,Solar_Battery_Voltage,Wind_Voltage,Wind_Current,Wind_Battery_Voltage\r')
                global file_num
                file_num = num
                with open("filename.txt", 'w') as file2:
                    file2.write(filename)
                return
        except:
            # except error if file exists
            print("File already exists")
            print(num)
            num = num + 1
            pass

def add_parameter(s_volt: float, s_cur: float, s_batt: float, w_volt: float, w_cur: float, w_batt: float) -> None:
    # add line of data to csv file
    # id, date, time, solar voltage, solar current, wind voltage, wind current
    print(file_num)
    with open((str(file_num) + "_" + "data.csv"), 'a') as file:
        file.write('\n' + str(u_id) + ',' + Time_Elapsed.elapsed_time() + ',' +
            str(s_volt) + ',' + str(s_cur) + ','+
            str(s_batt) + ','+ str(w_volt) + ',' + str(w_cur) + ',' + str(w_batt) + '\r\n')
        increment()

""""
t = time.localtime()
print(t)
create_csv(num)
add_parameter(Time_Elapsed.elapsed_time(), 12.3, 2.3, 12.4, 2.1)
time.sleep(2)
add_parameter(Time_Elapsed.elapsed_time(), 12.1, 2.5, 13.4,1.1)
#add_parameter(get_date(), get_time(), 5.3, 3.5, 6.9, 5.1)
"""