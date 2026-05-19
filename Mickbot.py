from tkinter import *
import pyttsx3
import random
from google import genai

API_KEY = 'Your generated API_KEY'

client = genai.Client(api_key=API_KEY)

instructions = 'You name is "Mick", a connection to a google gemini, made by a computer engineering student "Anas". Be short and precise in your answer,Now, Answer this question:'


def enter():

    response = client.models.generate_content(
    model ="gemini-2.5-flash-lite",
    contents = f"{instructions} {entry.get()}"
    )

    engine = pyttsx3.init()
    engine.setProperty('rate',130)
    engine.setProperty("volume",1)

    voices = engine.getProperty("voices")

    engine.setProperty("voice", voices[0].id)

    engine.say(response.text)
    engine.runAndWait()



window = Tk()
window.geometry("1000x180")
window.title("MICK by Anus")
window.config(bg='#3477eb')
label = Label(window, text="Mick", font=("Pacifico", 40, "bold", "italic"),
               fg="White", bg="#3477eb")
entry = Entry(window, font=("Arial", 20), bg="White", fg="Black", width=50)
entry.insert(0, "ask me anything!")
button = Button(window, text="ENTER", font=("Pacifico", 15, "bold"), relief=RAISED, bd=10, command=enter)

label.pack()
entry.pack()
button.pack()

window.mainloop()

