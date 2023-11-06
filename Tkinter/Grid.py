from tkinter import *
root = Tk()
#creating label
myLabel1= Label(root,text="Hello World")#.grid(row=0,column=1)
myLabel2= Label(root,text="My name is Adrian")#.grid(row=0,column=1)
#pushing it to the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=2)
3#it can ignore the index of column or row if its empty
root.mainloop()