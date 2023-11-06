import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap import Style

root = tb.Window(themename="superhero")
root.geometry("500x500")
root.title("Switch Pages")



option_frame = tb.Frame(root,bootstyle="secondary")
option_frame.propagate(False)
option_frame.pack(side=LEFT)
option_frame.configure(height=500,width=100)

style = Style()
#home_button_style = style.configure("TButton",font)

home_button = tb.Button(option_frame,bootstyle="info outline",text="Home")
home_button.place(x=10,y=50)

menu_button = tb.Button(option_frame,bootstyle="info outline",text="Contact")
menu_button.place(x=10,y=100)


contact_button = tb.Button(option_frame,bootstyle="info outline",text="Menu")
contact_button.place(x=10,y=150)

home_indicate = tb.Label(option_frame,text="",bootstyle="success")
home_indicate.place(x=3,y=50,width=5,height=40)

root.mainloop()