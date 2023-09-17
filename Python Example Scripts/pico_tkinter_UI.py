import tkinter as tk
import serial

# Create a serial port object
ser = serial.Serial('COM10', 9600)

# Create a root window
root = tk.Tk()

# Create a text widget to display the serial data
text = tk.Text(root)
text.pack()

# Create a button to send data to the Pico
send_button = tk.Button(root, text='Send', command=lambda: send_data())
send_button.pack()

# Create a text entry widget to enter the data to send
data_entry = tk.Entry(root)
data_entry.pack()

# Create two buttons to turn on and off the on-board LED
def led_on_button():
    led_on()
led_on_button = tk.Button(root, text='On', command=led_on_button)
led_on_button.pack()
def led_off_button():
    led_off()
led_off_button = tk.Button(root, text='Off', command=led_off_button)
led_off_button.pack()

# Create a mainloop to keep the window open
root.mainloop()

def send_data():
    # Get the data from the text entry widget
    data = data_entry.get()

    # Send the data to the Pico
    ser.write(data.encode())

    # Clear the text entry widget
    data_entry.delete(0, tk.END)

def led_on():
    # Send a byte to the Pico to turn on the LED
    ser.write(b'1')

def led_off():
    # Send a byte to the Pico to turn off the LED
    ser.write(b'0')
