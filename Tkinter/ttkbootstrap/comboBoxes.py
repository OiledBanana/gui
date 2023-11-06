from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap  as tb

root = tb.Window(themename="superhero")

root.title("Combo Boxes")
root.geometry('500x350')
#Functions
def clicker():
    my_label.config(text=f"The Day is "+my_Combo.get())



#Create Label
my_label= tb.Label(root,text="Hello User\nPick a Day",font=("Helvetica",20))
my_label.pack(pady=20)

#Create  DropDown Options
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#Create ComboBox
my_Combo = tb.Combobox(root,bootstyle="success",values=days)
my_Combo.pack(pady=10)

#default Combo 
my_Combo.current(0)

#Style for button
my_Style = tb.Style()
my_Style.configure('success.TButton',font=("Helvetica",18))

#Button
my_Button = tb.Button(root,text="Submit Day",
                      command=clicker,
                      bootstyle ="success",
                      style="success.button")
my_Button.pack()

root.mainloop()