from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename="superhero")
root.geometry("500x450")
root.title("MenuButtons")
def stuffs(x):
    my_label.config(text=f'You Picked {x}')
    my_menu.config(bootstyle=x)

my_menu = tb.Menubutton(root,bootstyle="warning",text="things")
my_menu.pack(pady=10)

#create basic menu

inside_menu = tb.Menu(my_menu)

#Add items to our inside menu
item_var = StringVar()
stuff = ['primary','secondary','danger','warning','outline danger',
'outline warning', 'outline primary','outline secondary']
for x in stuff:
    inside_menu.add_radiobutton(label=x,variable=item_var,command= lambda x=x: stuffs(x))
#Associate the inside menu to the menu button
my_label = tb.Label(root,text="")
my_label.pack(pady=25)
my_menu['menu'] = inside_menu
root.mainloop()