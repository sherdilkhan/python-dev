from tkinter import *


root = Tk()
root.title('This is First App in Tkinter')
root.geometry('600x400+400+400')
root.resizable(False, False)

def on_click():
    label_1 = Label(root, text=f"Hello: {d_enter.get()}")
    label_1.pack()


d_enter = Entry(root, width=40, bg='yellow')
d_enter.pack()


button_1 = Button(root, text="Enter Your Name", padx= 50, pady= 50, command=on_click)
button_1.pack()


mainloop()
