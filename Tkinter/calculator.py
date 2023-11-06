from tkinter import *

root = Tk()

e = Entry(root,width=45,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def Click(number):
    e.insert(0,number)
    

button1 = Button(root, text="1", padx=40,pady=20,command=lambda: Click(1))
button2 = Button(root, text='2', padx=40,pady=20,command=lambda: Click(2))
button3 = Button(root, text="3", padx=40,pady=20,command=lambda: Click(3))
button4 = Button(root, text="4", padx=40,pady=20,command=lambda: Click(4))
button5 = Button(root, text="5", padx=40,pady=20,command=lambda: Click(5))
button6 = Button(root, text="6", padx=40,pady=20,command=lambda: Click(6))
button7 = Button(root, text="7", padx=40,pady=20,command=lambda: Click(7))
button8 = Button(root, text="8", padx=40,pady=20,command=lambda: Click(8))
button9 = Button(root, text="9", padx=40,pady=20,command=lambda: Click(9))
button0 = Button(root, text="0", padx=40,pady=20,command=lambda: Click(0))
buttonClear = Button(root, text="clear", padx=80,pady=20,command=lambda: Click())
buttonEqual = Button(root, text="=", padx=90,pady=20,command=lambda: Click())
buttonAdd = Button(root, text="+", padx=40,pady=20,command=lambda: Click())


button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

button0.grid(row=4,column=0)

buttonClear.grid(row=4,column=1,columnspan=2)
buttonAdd.grid(row=5,column=0)
buttonEqual.grid(row=5,column=1,columnspan=2)






root.mainloop()
