from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title("practice.py")
root.geometry("500x620")
root.resizable(0,0)

myFont = Font(family="Arial", size=30,weight=NORMAL,underline=False,)

myFrame = Frame(root)
myFrame.pack(padx=40,pady=50)

Mylist = Listbox(myFrame,font=myFont,width=20,height=5,
                bd=1,highlightthickness=0,activestyle=NONE,
                selectbackground="#a6a6a6",fg="#464646")
Mylist.pack()

My_Entry = Entry(root,width=50)
My_Entry.pack(pady=10)


Button_Frame = Frame(root)
Button_Frame.pack(pady=10)

my_Scroll = Scrollbar(myFrame)
my_Scroll.pack(side=RIGHT, fill=BOTH)

Mylist.config(yscrollcommand=my_Scroll)
my_Scroll.config(command=Mylist.yview)

def Add_Item():
    Mylist.insert(END,My_Entry.get())
    My_Entry.delete(0,END)
    

def Delete_Item():
    Mylist.delete(ANCHOR)
    

def Cross_Item():
    Mylist.itemconfig(
        Mylist.curselection(),
        fg = "#dedede"
        )

def Uncross_Item():
    Mylist.itemconfig(
        Mylist.curselection(),
        fg = "#464646"
    )


def Delete_Crossed_Item():
    count = 0
    while count < Mylist.size():
        if Mylist.itemcget(count,"fg") == "#dedede":
            Mylist.delete(Mylist.index(count))
        else:
            count+=1

def Save_List():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/Users/USER/Desktop/Tkinter/practice_data",
        title="Save List", 
        filetypes=(("Dat Files","*.dat"),("All Files","*.*")),

    )

    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
        count = 0
        while count < Mylist.size():
            if Mylist.itemcget(count,"fg") == "#dedede":
                Mylist.delete(Mylist.index(count))
            else:
                count+=1
            stuff = Mylist.get(0,END)
            output_file = open(file_name,'wb')
            pickle.dump(stuff,output_file)




def Clear_List():
    Mylist.delete(0,END)
def Open_List():
    file_name = filedialog.askopenfilename(
        initialdir="C:/Users/USER/Desktop/Tkinter/practice_data",
        title="Save List", 
        filetypes=(("Dat Files","*.dat"),("All Files","*.*")),

    )

    if file_name:
        Mylist.delete(0,END)
        inpput_file = open(file_name,"rb")
        stuff = pickle.load(inpput_file)
    for item in stuff:
        Mylist.insert(END,item)

My_menu = Menu(root)
root.config(menu=My_menu)

file_menu = Menu(My_menu,tearoff=False)
My_menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="Open List",command=Open_List)
file_menu.add_command(label="Clear List",command=Clear_List)
file_menu.add_command(label="Save list", command=Save_List)


add_button = Button(Button_Frame,text="Add Item",command=Add_Item)
delete_button = Button(Button_Frame,text="Delete Item",command=Delete_Item)
cross_button = Button(Button_Frame,text="Cross Item",command=Cross_Item)
Uncross_button = Button(Button_Frame,text="Uncross Item",command=Uncross_Item)
delete_cross_button = Button(Button_Frame,text="Delete Crossed Item", command=Delete_Crossed_Item)


add_button.grid(row=0,column=0)
delete_button.grid(row=0,column=1,padx=25)
cross_button.grid(row=0,column=2)
Uncross_button.grid(row=0,column=3,padx=25)
delete_cross_button.grid(row=0,column=4)

myMainloop = root.mainloop()