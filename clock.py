
from tkinter import *
from datetime import datetime

app_window=Tk()
app_window.title("Digital Clock")
app_window.geometry("520x150")
app_window.resizable(0,0)

text_font=("Bolder",25,'bold')
background="black"
foreground="red"
border_width=55

label=Label(app_window,font=text_font,bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)

def digital_clock():
    time_live=datetime.now()
    label.config(text=time_live)
    label.after(200,digital_clock)


digital_clock()
app_window.mainloop()
