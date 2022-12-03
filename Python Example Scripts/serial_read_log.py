# for serial read and sleep functions
import serial
import time

#for data logging
import csv
from datetime import datetime
 

#initialize Serial Port 
ser = serial.Serial('COM7', 9600, timeout=1)

time.sleep(2)
 
i = 0
    


while(True):
    # Reading all bytes available bytes till EOL
    line = ser.readline() 
    if line:
        # Converting Byte Strings into unicode strings
        string = line.decode()
        dataSplit = string.split(',')  
        # Converting Unicode String into integer
        val1 = dataSplit[0]
        val2 = dataSplit[1]

        #num = int(string) 
        print(val1 + ' , ' + val2)
    with open("test.csv", "a") as nice:
        nice.write(f"{i},{time.strftime('%a %H:%M:%S')},{val1},{val2}")
        i += 1
 
ser.close()