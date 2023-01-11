from tkinter import *    #import everthing fromtkinter library

#in tkinter, everything is a widget....button, label etc
root = Tk()  #creat an object root from Tk() footprint or Class. Root Means Main Widget

#define button_realAll Click Event. Add all the code you want to execute on button click

def button_readAll_click():
    label_L1_n_value = Label(root, text='value rec1')
    label_L1_n_value.grid(padx = 20,row=0, column=1)

    label_f_value = Label(root, text='value rec2')
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

root.mainloop()

