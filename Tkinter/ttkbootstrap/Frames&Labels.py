from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap  as tb


root = tb.Window(themename="superhero")
root.title("Frames and Labels")
root.geometry('500x450')

def thing():
    pass
#use invnsible frame if you want to grid
my_Frame = Frame(root)#bootstyle="dark")
my_Frame.pack(pady=20)

my_entry = tb.Entry(my_Frame,font=("Helvetica",15))
my_entry.pack(pady=10,padx=10)

my_button = tb.Button(my_Frame,text="Click Me!",bootstyle="success",command=thing)
my_button.pack(pady=10,padx=10)

my_label = tb.Label(root,text="Hello There",font=("Helvetica",15),bootstyle="inverse light")
my_label.pack(pady=10)

root.mainloop()