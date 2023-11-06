from tkinter import *
root = Tk()
e = Entry(root,width=20,borderwidth=5)
e.pack()

#creating label
#myLabel1= Label(root,text="Hello World")#.grid(row=0,column=1)
#myLabel2= Label(root,text="My name is Adrian")#.grid(row=0,column=1)
#pushing it to the screen
def clickMe():
    myLabel = Label(root,text=e.get())
    myLabel.pack()

#myLabel1.grid(row=0,column=0)
#myLabel2.grid(row=1,column=2)
mybutton = Button(root, text="Enter Name",command=clickMe)
mybutton.pack()
root.mainloop()
#it can ignore the index of column or row if its empty
#root.mainloop()