from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file="C:/Users/USER/Desktop/Tkinter/projects/login (1).png")
Label(root,image=img,bg='white').place(x=50,y=50)
frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=50)
#Functions

def sign_in():
    username = user.get()
    password = pass_entry.get()

    if username == "admin" and password == "1234":
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen,text="Hello Everyone",bg="#fff",font=("Helvitica",50)).pack(expand=True)

        screen.mainloop()
    elif username != "admin" and password != "1234":
         messagebox.showerror("Invalid","Invalid username and password")
    elif password != "1234":
        messagebox.showerror("Invalid", "Invalid Password")
    elif username != "admin":
        messagebox.showerror("Invalid","Invalid Username") 

 




heading = Label(frame,text='Sign in',fg="#57a1f8",bg="white",font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
####................... USERNAME
user = Entry(frame,width=25,fg="black",border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,"Username")
user_Frame = Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

###................... PASSWORD
pass_entry = Entry(frame,width=25,fg="black",border=0,bg="white",font=('Microsoft YaHei UI Light',11),show="*")
pass_entry.place(x=30,y=150)
pass_entry.insert(0,"Password")
pass_entry_Frame = Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)


Sign_In = Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8",fg="white",border=0,command=sign_in)
Sign_In.place(x=35,y=204)


root.mainloop()