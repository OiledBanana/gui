from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap  as tb

root = tb.Window(themename="superhero")

root.title("TTK Bootstrap")
root.geometry("500x500")
counter = 0
#Create function for button
def SayName():
    myLabel = tb.Label(text="Hello "+ my_entry.get())
    myLabel.pack(pady=10)

def Counter():
    global counter
    counter += 1
    my_Label.config(text=f"Times clicked {counter}")

#Color
#Create label


my_Label = tb.Label(text= "Times clicked 0",font=("Helvetica",28), 
                    bootstyle ="danger")
my_Label.pack(pady=5)

my_entry = tb.Entry(bootstyle="default")
my_entry.pack(pady=5)


#create button
my_button = tb.Button(text="Enter your Name",bootstyle = "primary",command=SayName)
my_button.pack()
my_button1 = tb.Button(text="Clcik Me", bootstyle ="default",command=Counter)
my_button1.pack(padx=5,pady=10)
root.mainloop()