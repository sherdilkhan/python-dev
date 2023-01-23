from tkinter import *    #import everthing fromtkinter library
import minimalmodbus
import serial
import os
import time
import schedule


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
#in tkinter, everything is a widget....button, label etc
root = Tk()  #creat an object root from Tk() footprint or Class. Root Means Main Widget

# specify size of window.
root.geometry("600x400")


#define button_realAll Click Event. Add all the code you want to execute on button click
def button_readAll_click():
    v_l1n = instrument.read_float(registeraddress=19000, functioncode=3,number_of_registers=2,byteorder = 0)  # Registernumber, number of decimals
    f = instrument.read_float(registeraddress=19050, functioncode=3,number_of_registers=2,byteorder = 0)  # Registernumber, number of decimals 
    #clear the text from label
    label_L1_n_value = Label(root, text='')
    label_L1_n_value.grid(padx = 20,row=0, column=1)
    label_L1_n_value = Label(root, text=str(v_l1n))
    label_L1_n_value.grid(padx = 20,row=0, column=1)
 

def update_label_cnt():
    f = instrument.read_float(registeraddress=19050, functioncode=3,number_of_registers=2,byteorder = 0)  # Registernumber, number of decimals 
    label_f_value = Label(root, text='')
    label_f_value.grid(padx = 20,row=1, column=1)
    label_f_value = Label(root, text=str(f))
    label_f_value.grid(padx = 20,row=1, column=1)  

#lets creat two label widgets. One for Name, other for its value over main Root Widget
label_L1_n_name = Label(root, text = 'L1-N: ')
label_L1_n_value = Label(root, text= '', state=DISABLED)
label_f_name = Label(root, text = 'Hz: ')
label_f_value = Label(root, text= '', state=DISABLED)
#lets creat a button
button_readAll = Button(root, text='Read All Param',command=button_readAll_click, fg='black', bg='white')

#shoving the labels to scree.
#label_L1_n_name.pack(pady=20)
#label_L1_n_value.pack(pady=20)
label_L1_n_name.grid(padx = 50, row=0, column=0)
label_L1_n_value.grid(padx = 50,row=0, column=1)
label_f_name.grid(padx=50, row=1, column=0 )
label_f_value.grid(padx=50, row=1, column=1)
button_readAll.grid(padx = 50, row=0, column=2)

#lets create a event loop for this program
root.after(1000,update_label_cnt)

mainloop()