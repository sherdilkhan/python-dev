import minimalmodbus
import serial
from pymongo import *
import os
import subprocess as sp
import time

mongopass = os.getenv("MONGOPASS") #get connection string from user enviroment variable
client = MongoClient(mongopass) #create mongo client instance to connect with MongoDB online Cluster
db = client.db_rm96_001 #create a database
collection_1 = db.bd #create a document collection

instrument = minimalmodbus.Instrument('COM8', 1)  # port name, slave address (in decimal)
instrument.serial.port = 'COM8'                     # this is the serial port name
instrument.serial.baudrate = 9600         # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 1        # seconds
instrument.address = 1                         # this is the slave address number
instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
#nstrument.clear_buffers_before_each_transaction = True

while True:
    date_stamp = sp.getoutput("date /t")
    time_stamp = sp.getoutput('time /t')
    v_l1n = instrument.read_float(registeraddress=19000, functioncode=3,number_of_registers=2,byteorder = 0)  # Registernumber, number of decimals
    f = instrument.read_float(registeraddress=19050, functioncode=3,number_of_registers=2,byteorder = 0)  # Registernumber, number of decimals 
    try:
        print(v_l1n)
        print(f)
        myVal = {
        'date': date_stamp,
        'time': time_stamp,
        'v_l1n': v_l1n,
        'frequency': f 
        }
        x = collection_1.insert_one(myVal)
    except:
        print(v_l1n)
        print(f)
    time.sleep(2)
    os.system('cls')  #clear terminal screen
    
