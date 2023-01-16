from tkinter import *
import openai
import os

root = Tk()

root.title('Chat GPT Version 0.01')
root.geometry("600x400")

# Add a Scrollbar(horizontal)
v=Scrollbar(root, orient='vertical')
v.pack(side=RIGHT, fill='y')

# Creating object of photoimage class
img1 = PhotoImage(file = 'images.png')
root.iconphoto(False, img1)

# declaring string variable
input_text=StringVar()

#lets creat an Input Label
entery1 = Entry(root, textvariable = input_text)
entery1.place(x = 150, y = 310, width= 400, height= 50)


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

    label2 = Text(root, yscrollcommand=v.set, height = 10, width = 52)
    label2.place(x = 5, y= 5)
    label2.insert(END, message)



#Create a Button to push the query to ChatGPT server
button1 = Button(root, text = "Search", command=query_gpt)
button1.place(x = 50, y = 310)

mainloop()