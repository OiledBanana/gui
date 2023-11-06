from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap  as tb

root = tb.Window(themename="superhero")

root.title("CheckButton")
root.geometry('500x350')

#Style
my_style = tb.Style()
my_style.configure('success.TButton',font=("Helvetica",18))
my_button = tb.Button(text="Hello World",
                      bootstyle ="success",
                      style="success.button",
                      width=20)
my_button.pack(pady=10)

root.mainloop()