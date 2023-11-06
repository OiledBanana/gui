from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap  as tb

root = tb.Window(themename="superhero")

root.title("Entry")
root.geometry('500x450')

def starter():
    my_gauge.start()
    

def stopper():
    my_gauge.stop()

def incrementer():
    my_gauge.step(10)
    my_label.config(text=f"Percentage: {my_gauge.variable.get()}")

my_gauge = tb.Floodgauge(root,bootstyle="success",font=("Helvetica",18),
                         mask="Pos: {}%",
                         maximum=80,
                         orient="horizontal",
                         mode='determinate'#indeterminate
                         )
my_gauge.pack(pady=50,fill=X,padx=20)

start_button = tb.Button(root,text="Start",bootstyle="danger outline",command=starter)
start_button.pack(pady=10)
stop_button = tb.Button(root,text="Stop",bootstyle="danger outline",command=stopper)
stop_button.pack(pady=10)
inc_button = tb.Button(root,text="Increment",bootstyle="danger outline",command=incrementer)
inc_button.pack(pady=10)

my_label = tb.Label(root,text="Position: ",bootstyle="warning",font=("Helvetica",15))
my_label.pack(pady=10)
root.mainloop()