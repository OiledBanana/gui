from tkinter import *
root = Tk()
#size: padx, pady = x and y axis
def myclick():
    myLabel = Label(root,text="I clicked it")
    myLabel.pack()

myButton = Button(root,text="Click me",padx=25,pady=10,command=myclick,fg="blue",bg="white")
myButton.pack()
root.mainloop()