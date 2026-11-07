from tkinter import *
import speedtest

def speedcheck():
    st = speedtest.Speedtest()
    st.get_servers()
    down = str(round(st.download() / 1000000, 3)) + " Mbps"
    up = str(round(st.upload() / 1000000, 3)) + " Mbps"
    download.config(text=down)
    upload.config(text=up)


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="skyblue")

lab = Label(sp, text="Internet Speed Test", font=("Arial", 20, "bold"), bg="skyblue")
lab.pack(pady=20)

download_label = Label(sp, text="Download Speed: ", font=("Arial", 15), bg="skyblue")
download_label.pack(pady=10)

download = Label(sp, text="00", font=("Arial", 15), bg="skyblue")
download.pack(pady=10)

upload_label = Label(sp, text="Upload Speed: ", font=("Arial", 15), bg="skyblue")
upload_label.pack(pady=10)

upload = Label(sp, text="00", font=("Arial", 15), bg="skyblue")
upload.pack(pady=10)

button = Button(sp, text="Test Speed", font=("Arial", 15), bg="green", relief=RAISED, command=speedcheck)
button.pack(pady=20)

sp.mainloop()