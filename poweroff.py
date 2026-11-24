from tkinter import *
import os

def shutdown():
    os.system("shutdown /s /t 1")

def restart():
    os.system("shutdown /r /t 1")

def singout():
    os.system("shutdown /l")

st = Tk()
st.title("Shutdown")
st.geometry("500x400")
st.configure(bg="black")

shutdown_btn = Button(st, text="Shutdown", font=("Arial", 20), bg="green", fg="black", relief=RAISED, command = shutdown)
shutdown_btn.pack(pady=20)

restart_btn = Button(st, text="Restart", font=("Arial", 20), bg="red", fg="black", relief=RAISED, command = restart)
restart_btn.pack(pady=20)

singout_btn = Button(st, text="Sign Out", font=("Arial", 20), bg="yellow", fg="black", relief=RAISED, command = singout)
singout_btn.pack(pady=20)

st.mainloop()