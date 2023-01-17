from tkinter import *
import openai
import os

root = Tk()

root.title('Chat GPT Version 0.01')
# width x height + x offset + y offset
root.geometry("630x400+400+200")
root.config(bg = "skyblue")
root.resizable(False, False)

#bottom from for query area
frame_bottom = Frame(root, width= 600, height= 80, bg= 'grey')
frame_bottom.place(x = 5, y = 315)

#top frame for query area
frame_top = Frame(root, width= 600, height= 300, bg= 'light grey')
frame_top.place(x = 5, y = 5)

# Creating object of photoimage class
img1 = PhotoImage(file = 'images.png')
root.iconphoto(False, img1)

# Add a Scrollbar(horizontal)
v=Scrollbar(root, orient='vertical')
v.pack(side=RIGHT, fill='y')

# declaring string variable
input_text=StringVar()

#lets creat an Input Label
entery1 = Entry(frame_bottom, textvariable = input_text, width= 54, bg= 'white',font=('Helvetica', 12))
entery1.place(x = 100, y = 20)

def query_gpt():
    openai.api_key = os.getenv("OPENAI_API_KEY")  
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=str(input_text.get()),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        )
    message =  completions.choices[0].text

    label2 = Text(frame_top, yscrollcommand=v.set, height = 13, width = 53, font=('Helvetica', 14))
    label2.place(x = 5, y= 5)
    label2.insert(END, message)

#Create a Button to push the query to ChatGPT server
button1 = Button(frame_bottom, text = "Search", command=query_gpt, bg='green', fg= 'black', font=('Helvetica', 15))
button1.place(x = 20, y = 20)

mainloop()