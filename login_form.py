from tkinter import *
from tkinter import messagebox
import mysql.connector
import ttkbootstrap as tb


root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file="C:/Users/OJT/Downloads/gui-main/Tkinter/projects/login (1).png")
Label(root,image=img,bg='white').place(x=50,y=50)
frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=50)
#Functions

def sign_in():
    username = user.get()
    password = pass_entry.get()

    if username == "" or  password == "":
        messagebox.showwarning("Invalid","All fields are required")
    else:
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="password",database="mydb",port="3307")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM credentials WHERE username = %s AND password = %s", (username, password))
            result = my_cursor.fetchone()
            if result:
                screen = Toplevel(root)
                screen.title("App")
                screen.geometry('925x500+300+200')
                screen.config(bg="white")

                Label(screen,text="Hello Everyone",bg="#fff",font=("Helvitica",50)).pack(expand=True)

                screen.mainloop()
            else:
                 messagebox.showerror("Invalid","Invalid username and password")
                        
        
        except mysql.connector.Error as error:
                    print("Error:", error)


def Reset():
    global reset_Entry, user_Entry, pass_Entry,screen
    screen = Toplevel(root)
    screen.title("Reset")
    screen.geometry('350x350')
    screen.config(bg="white")
    reset_Entry = Entry(screen,fg="black",bg="white",font=('Helvetica',10),show="*")
    user_Entry = Entry(screen,fg="black",bg="white",font=('Helvetica',10))
    pass_Entry = Entry(screen,fg="black",bg="white",font=('Helvetica',10),show="*")
    user_Entry.insert(0,"Enter new Username")
    pass_Entry.insert(0,"Enter new password")
    reset_Entry.insert(0,"Enter reset password")
    reset_button = Button(screen, text="submit",command= submit)

    user_Entry.pack(pady=15)
    pass_Entry.pack(pady=15)
    reset_Entry.pack(pady=15)
    reset_button.pack(pady=15)


def submit():
    username = user_Entry.get()
    password = pass_Entry.get()
    reset = reset_Entry.get()

    if username == "" or password == "" or reset == "":
         messagebox.showwarning("Invalid","All fields are required")
    if reset != "admin123" and reset != "":
         messagebox.showwarning("Invalid","Invalid password")
    elif username != "" and password != "" and reset == "admin123":
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="password",database="mydb",port="3307")
            my_cursor = conn.cursor()
            update_query ="UPDATE credentials SET username = %s, password = %s WHERE ID = '1'"
            data = (username,password)
            my_cursor.execute(update_query,data)
            conn.commit()
            my_cursor.close()
            conn.close()
            user_Entry.delete(0,END)
            pass_Entry.delete(0,END)
            reset_Entry.delete(0,END)
            messagebox.showinfo("Reset Successfully","username and password reseted")
            screen.destroy()
        except mysql.connector.Error as error:
                    print("Error:", error)
    else:
         pass


         
    
    
         


    
    


        





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

reset_button = Button(frame, width=39, pady=7, text="Reset", bg="#ff5733", fg="white", border=0, command=Reset)
reset_button.place(x=35, y=240)





root.mainloop()