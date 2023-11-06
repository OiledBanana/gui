from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap  as tb
from datetime import date

root = tb.Window(themename="superhero")

root.title("Date Entry")
root.geometry('500x450')

def get_date():
    my_label.config(text=f"You Picked: {my_date.entry.get()}")

my_date = tb.DateEntry(root,bootstyle="success",startdate=date(1999,12,16,),firstweekday=0)
my_date.pack(pady=10)

my_button = tb.Button(root,text="Get Date",bootstyle="danger outline",command=get_date)
my_button.pack(pady=10)

my_label = tb.Label(root,text="You Picked: ")
my_label.pack(pady=5)

user = tb.Entry(root,width=25,foreground="black",background="white",font=('Microsoft YaHei UI Light',11))
user.pack()
root.mainloop()