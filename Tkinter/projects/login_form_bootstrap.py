from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as tb

root = tb.Window(themename="litera")
root.geometry('925x500+300+200')
root.resizable(False,False)


img = tb.PhotoImage(file="C:/Users/USER/Desktop/Tkinter/projects/login (1).png")
image_label = tb.Label(root,image=img)
image_label.place(x=50,y=50)
my_frame = tb.Frame(root,width=350,height=350)
my_frame.place(x=480,y=50)

heading = tb.Label(my_frame,text='Sign in',foreground="#57a1f8",font=('Helvetica',23,'bold'))
heading.place(x=100,y=5)
user = tb.Entry(my_frame,width=25,foreground="black",font=('Helvetica',11),bootstyle="primary")
user.place(x=50,y=90)
username_label = tb.Label(my_frame,text='Username',foreground="#57a1f8",font=('Helvetica',23,'bold'))
root.mainloop()
