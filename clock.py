from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    ampm1 = time.strftime("%p")
    date1 = time.strftime("%d")
    month1 = time.strftime("%m")
    year1 = time.strftime("%Y")
    day1 = time.strftime("%A")

    hour.config(text=hr)
    minute.config(text=min)
    second.config(text=sec)
    ampm.config(text=ampm1)
    date.config(text=date1)
    month.config(text=month1)
    year.config(text=year1)
    day.config(text=day1)

    hour.after(200, date_time)

clock = Tk()
clock.title("Digital Clock")
clock.geometry("570x500")
clock.config(bg="yellow")

#hour, minute, second, ampm box design
#hour box design
hour = Label(clock, text="00", font=("times", 50, "bold"), bg="red", fg="white")
hour.place(x=50, y=50, width=100, height=100)
hrl = Label(clock, text=":", font=("times", 50, "bold"), bg="yellow", fg="black")
hrl.place(x=150, y=50, width=20, height=100)

#minute box design
minute = Label(clock, text="00", font=("times", 50, "bold"), bg="red", fg="white")
minute.place(x=170, y=50, width=100, height=100)
mrl = Label(clock, text=":", font=("times", 50, "bold"), bg="yellow", fg="black")
mrl.place(x=270, y=50, width=20, height=100)

#second box design
second = Label(clock, text="00", font=("times", 50, "bold"), bg="red", fg="white")
second.place(x=290, y=50, width=100, height=100)
srl = Label(clock, text=":", font=("times", 50, "bold"), bg="yellow", fg="black")
srl.place(x=390, y=50, width=20, height=100)

#AM/PM box design
ampm = Label(clock, text="AM", font=("times", 20, "bold"), bg="red", fg="white")
ampm.place(x=410, y=50, width=100, height=100)

#hour, minute, second, ampm label design
#hour label design
hour_label = Label(clock, text="HOUR", font=("times", 10, "bold"), bg="red", fg="black")
hour_label.place(x=50, y=160, width=100, height=50)

#minute label design
minute_label = Label(clock, text="MINUTE", font=("times", 10, "bold"), bg="red", fg="black")
minute_label.place(x=170, y=160, width=100, height=50)

#second label design
second_label = Label(clock, text="SECOND", font=("times", 10, "bold"), bg="red", fg="black")
second_label.place(x=290, y=160, width=100, height=50)

#AM/PM label design
ampm_label = Label(clock, text="AM/PM", font=("times", 10, "bold"), bg="red", fg="black")
ampm_label.place(x=410, y=160, width=100, height=50)

#date, month, year & day box design
#date box design
date = Label(clock, text="00", font=("times", 35, "bold"), bg="red", fg="white")
date.place(x=50, y=250, width=100, height=100)
datel = Label(clock, text="/", font=("times", 35, "bold"), bg="yellow", fg="black")
datel.place(x=150, y=250, width=20, height=100)

#month box design
month = Label(clock, text="00", font=("times", 35, "bold"), bg="red", fg="white")
month.place(x=170, y=250, width=100, height=100)
monl = Label(clock, text="/", font=("times", 35, "bold"), bg="yellow", fg="black")
monl.place(x=270, y=250, width=20, height=100)

#year box design
year = Label(clock, text="0000", font=("times", 35, "bold"), bg="red", fg="white")
year.place(x=290, y=250, width=100, height=100)
yearl = Label(clock, text="-", font=("times", 35, "bold"), bg="yellow", fg="black")
yearl.place(x=390, y=250, width=20, height=100)

#day box design
day = Label(clock, text="DAY", font=("times", 15, "bold"), bg="red", fg="white")
day.place(x=410, y=250, width=100, height=100)

#date, month, year & day label design
#date label design
date_label = Label(clock, text="DATE", font=("times", 10, "bold"), bg="red", fg="black")
date_label.place(x=50, y=360, width=100, height=50)

#month label design
month_label = Label(clock, text="MONTH", font=("times", 10, "bold"), bg="red", fg="black")
month_label.place(x=170, y=360, width=100, height=50)

#year label design
year_label = Label(clock, text="YEAR", font=("times", 10, "bold"), bg="red", fg="black")
year_label.place(x=290, y=360, width=100, height=50)

#day label design
day_label = Label(clock, text="DAY", font=("times", 10, "bold"), bg="red", fg="black")
day_label.place(x=410, y=360, width=100, height=50)

date_time()
clock.mainloop()