import minimalmodbus
import serial
import os

instrument = minimalmodbus.Instrument('COM3', 1)  # port name, slave address (in decimal)
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
    v_l1n = instrument.read_float(registeraddress=19000, functioncode=3,number_of_registers=2,byteorder = 0)  # Registernumber, number of decimals
    f = instrument.read_float(registeraddress=19050, functioncode=3,number_of_registers=2,byteorder = 0)  # Registernumber, number of decimals 
    try:
        print(v_l1n)
        print(f)
    except:
        print(v_l1n)
        print(f)
    os.system('cls')  #clear terminal screen