from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle
root = Tk()
root.title('Adrian To do List!')
root.geometry("650x500")
root.resizable(0,0)

#creatin a font 
my_font = Font(
    family="Arial",
    size= 25,
    weight= "bold"
)


#creating a frame
my_Frame = Frame(root)
my_Frame.pack(pady=50,padx=40)

#creating a listbox that will be put on our frame
my_list = Listbox(my_Frame,
                  font=my_font,
                  width=25,
                  height=5,
                  bg="SystemButtonFace",
                  bd=2,
                  fg="#464646",
                  selectbackground="#a6a6a6",
                  activestyle=NONE,highlightthickness=0)

#positioning our list
my_list.pack(side=LEFT,fill=BOTH)

#create a dummy list
#stuff = ["Aral","Iyotin asawa ko","Matulog"]

#iterating each item in stuff to insert each end to our list
#for item in stuff:
    #my_list.insert(END,item)


#create scroll bar to scroll through the list

my_Scroll = Scrollbar(my_Frame)
my_Scroll.pack(side=RIGHT, fill=BOTH)

#Add the scrollbar
my_list.config(yscrollcommand=my_Scroll)
my_Scroll.config(command=my_list.yview)

#create entry box to add to the list

my_Entry = Entry(root, font=("Helvetica"),width=50)
my_Entry.pack(pady=20)


#button to add

button_frame = Frame(root)
button_frame.pack(pady=30)

#Functions of Buttons
def Delete_Item():
    #deleting what is highlighted using anchor
    my_list.delete(ANCHOR)


def Add_Item():
    #using get 
    my_list.insert(END,my_Entry.get())
    my_Entry.delete(0,END)#to delete whatever is in the entry for the new re entry

    

def Cross_Item():
    #crossing the item by what is highlighted or in the curson and changing ots color
    my_list.itemconfig(
        my_list.curselection(),
        fg = "#dedede"
    )
    my_list.selection_clear(0,END)

def Uncross_Item():
        my_list.itemconfig(
        my_list.curselection(),
        fg = "#464646"
    )
        

def delete_crossed_Item():
     count = 0

     
     while count < my_list.size():
          if my_list.itemcget(count,"fg") == "#dedede":
              my_list.delete(my_list.index(count))
          else:
               count+= 1

def save_list():
     file_name = filedialog.asksaveasfilename(
          initialdir="C:/Users/USER/Desktop/Tkinter/data",
          title="Save file",
          filetypes=(("Dat Files","*.dat"),("All Files","*.*"))
     )
     if file_name:
          if file_name.endswith(".dat"):
               pass
          else:
               file_name = f'{file_name}.dat'
        #Delete crossed items before saving
          count = 0
          while count < my_list.size():
            if my_list.itemcget(count,"fg") == "#dedede":
               my_list.delete(my_list.index(count))
            else:
               count+= 1
        #write binary to save it
          stuff = my_list.get(0,END)
          output_file = open(file_name,'wb')
     #Add to the file
          pickle.dump(stuff,output_file)

def open_list():
     file_name = filedialog.askopenfilename(
          initialdir="C:/Users/USER/Desktop/Tkinter/data",
          title="Save file",
          filetypes=(("Dat Files","*.dat"),("All Files","*.*"))
     )
     if file_name:
         #delete current list
         my_list.delete(0,END)
         #Open the file
         input_file =open(file_name,'rb')
         #Load the data from the file
         stuff = pickle.load(input_file)

         for item in stuff:
             my_list.insert(END, item)
def clear_list():
    my_list.delete(0,END)
     
    
#Create Menu
my_Menu  = Menu(root)
root.config(menu=my_Menu)    

#Add items to menu
file_menu = Menu(my_Menu,tearoff=False)
my_Menu.add_cascade(label="File",menu=file_menu)
#Add dropdown Items

file_menu.add_command(label="Save List",command=save_list)
file_menu.add_command(label="Open List",command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List",command=clear_list)

#Add Some buttons
delete_button = Button(button_frame,text="Delete_Item",command=Delete_Item)
add_button = Button(button_frame,text="Add_Item",command=Add_Item)
crossOff_button = Button(button_frame,text="Cross Item",command=Cross_Item)
uncrossOff_button = Button(button_frame,text="UnCross Item",command=Uncross_Item)
delete_crossed_button = Button(button_frame,text="Delete Crossed Item",command=delete_crossed_Item)

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=20)
crossOff_button.grid(row=0,column=2)
uncrossOff_button.grid(row=0,column=3,padx=20)
delete_crossed_button.grid(row=0,column=4)





root.mainloop()