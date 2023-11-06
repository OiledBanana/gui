from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap  as tb

root = tb.Window(themename="superhero")

root.title("CheckButton")
root.geometry('500x350')
#function
def checker():
    if var1.get() == 1:
        my_Label.config(text="Checked!")
    else:
        my_Label.config(text="Unchecked!")

#Label
my_Label = Label(text="Click the checkbutton below it",font=("Helvetica",18))
my_Label.pack(pady=(40,10))

#Checkbutton
var1 = IntVar()
my_Check = tb.Checkbutton(bootstyle = "info",text="Check me out!",
            variable=var1,
            onvalue=1,
            offvalue=0,
            command=checker,
            )
my_Check.pack(pady=10)
#toolButton
var2 = IntVar()
my_Check2 =tb.Checkbutton(bootstyle = "danger, toobutton", text="Toolbutton!",
            variable=var2,
            onvalue=1,
            offvalue=0,
            command=checker,
            )
my_Check2.pack(pady=10)

var3 = IntVar()
my_Check3 =tb.Checkbutton(bootstyle = "danger, toobutton, outline", text="Toolbutton!",
            variable=var2,
            onvalue=1,
            offvalue=0,
            command=checker,
            )
my_Check3.pack(pady=10)
#Round Button
var4 = IntVar()
my_Check4 =tb.Checkbutton(bootstyle = "success,round-toggle", text="Round Toggle!",
            variable=var4,
            onvalue=1,
            offvalue=0,
            command=checker,
            )
my_Check4.pack(pady=10)
#Square Toggle Button
var5 = IntVar()
my_Check5 =tb.Checkbutton(bootstyle = "success,square-toggle", text="Round Toggle!",
            variable=var5,
            onvalue=1,
            offvalue=0,
            command=checker,
            )
my_Check5.pack(pady=10)
root.mainloop()