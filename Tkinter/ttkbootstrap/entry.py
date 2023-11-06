from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap  as tb

root = tb.Window(themename="superhero")

root.title("Entry")
root.geometry('500x450')
#function
def speak():
    my_Label.config(text=f"You Typed: {my_Entry.get()}\nYour Password: {my_Entry2.get()}",font=("Helvetica",18))



    
    pass
my_label = tb.Label(root,text="Enter Your Name",font=("Helvetica",15))
my_label.pack(pady=10)
my_Entry = tb.Entry(root,bootstyle="success",font=("Helvetica",18),
                    foreground="#adadad")
my_Entry.pack(pady=10)
my_label2 = tb.Label(root,text="Enter Your Password",font=("Helvetica",15))
my_label2.pack(pady=10)
my_Entry2 = tb.Entry(root,bootstyle="success",font=("Helvetica",18),
                    foreground="#adadad",
                    show="*")

my_Entry2.pack(pady=10)
my_Button = tb.Button(root,
                      bootstyle="danger outline",
                      text="Click Me!",
                      command=speak)
my_Button.pack(pady=20)

my_Label = tb.Label(root,text="")
my_Label.pack(pady=20)
root.mainloop()