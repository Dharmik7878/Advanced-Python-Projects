from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from deep_translator import GoogleTranslator

def change(text = "type", src = "English", dest = "Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans_text = trans.translate(text1, src=src1, dest=dest1)
    return trans_text.text

def data():
    s = combo_sor.get()
    d = combo_dest.get()
    msg = sorceText.get(1.0, END)
    gettext = change(text = msg, src = s, dest = d)
    destText.delete(1.0, END)
    destText.insert(END, gettext)

root = Tk()
root.title("Translator")
root.geometry("400x700")
root.config(bg="skyblue")
listText = list(LANGUAGES.values())

labText = Label(root, text="Translator", font=("Arial", 30, "bold"), bg="skyblue", fg="black")
labText.pack(pady=10)

frame = Frame(root, bg="skyblue")
frame.pack(side = BOTTOM, fill = BOTH, expand = True)

labText = Label(root, text="Source Text", font=("Arial", 20, "bold"), bg="skyblue", fg="black", borderwidth=2, relief="solid")
labText.pack()

sorceText = Text(frame, font=("Arial", 12), wrap = WORD)
sorceText.place(x = 30, y = 5, width = 340, height = 200)


combo_sor = ttk.Combobox(frame, values=listText, font=("Arial", 12))
combo_sor.place(x = 30, y = 210, width = 340, height = 30)
combo_sor.set("Select Language")

button_change = Button(frame, text = "translate", relief = RAISED, command = data)
button_change.place(x = 30, y = 250, width = 340, height = 30)

combo_dest = ttk.Combobox(frame, values=listText, font=("Arial", 12))
combo_dest.place(x = 30, y = 290, width = 340, height = 30)
combo_dest.set("Select Language")


destText = Text(frame, font=("Arial", 12), wrap = WORD)
destText.place(x = 30, y = 330, width = 340, height = 200)

# destLabel = Label(root, text="Destination Text", font=("Arial", 20, "bold"), bg="skyblue", fg="black", borderwidth=2, relief="solid")
# destLabel.pack()

root.mainloop()