from tkinter import *
from tkinter import messagebox
import mysql.connector 
from ttkbootstrap import *
import ttkbootstrap as tb

root = tb.Window(themename="darkly")

root.title("Python crud")
root.geometry("500x500")
root.resizable(0,0)

#functions
def insert():
    id_value = id_entry.get()
    phone_value = phone_entry.get()
    name_value = name_entry.get()
    

    if id_value == "" or phone_value == "" or name_value == "":
        messagebox.showinfo("Insert Status","All Fields are required")
    else:
        conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="test")
        my_cursor = conn.cursor()
        insert_query = "INSERT INTO students (id, Student_Name, Phone_Number) VALUES (%s, %s, %s)"

# Define the data as a tuple with the corresponding values
        data = (id_value, name_value, phone_value)

        my_cursor.execute(insert_query, data)
        conn.commit()
        my_cursor.close()
        id_entry.delete(0,END)
        phone_entry.delete(0,END)
        name_entry.delete(0,END)

        messagebox.showinfo("Insert status", "Inserted Successfully")
        conn.close()
      

def Update():
        id_to_update = id_entry.get()
        new_name = name_entry.get()
        new_phone = phone_entry.get()
     

        if id_to_update == "":
            messagebox.showinfo("Insert Status","Insert Id to update")
        elif id_to_update == "" or new_name == "" or new_phone == "":
            messagebox.showinfo("Insert Status","All fields Required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="test")
                my_cursor = conn.cursor()
                update_query = "UPDATE students SET Student_Name = %s, Phone_Number = %s WHERE id = %s"
                data =(new_name,new_phone,id_to_update)
                my_cursor.execute(update_query,data)
                conn.commit()
                my_cursor.close()
                conn.close()
                id_entry.delete(0,END)
                phone_entry.delete(0,END)
                name_entry.delete(0,END)
                messagebox.showinfo("Update Status", "Data updated successfully")
                


            except mysql.connector.Error as error:
                    print("Error:", error)


def delete():
      id_to_delete = id_entry.get()
      if id_to_delete == "":
          messagebox.showinfo("Status","Id to be deleted needed")
      else:
        confirmed = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this record?")

        
      if confirmed:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="test")
                my_cursor = conn.cursor()
                
                # Create the DELETE query with a WHERE clause to specify the record to delete
                delete_query = "DELETE FROM students WHERE id = %s"
                data = (id_to_delete,)

                my_cursor.execute(delete_query, data)
                conn.commit()
                my_cursor.close()
                conn.close()

                id_entry.delete(0, END)
                messagebox.showinfo("Delete Status", "Record with ID {} deleted successfully.".format(id_to_delete))

           

            except mysql.connector.Error as error:
                print("Error:", error)

      else:
            messagebox.showinfo("Delete Status", "Delete operation canceled.")
def Show():
    new_window = tk.Toplevel(root)
    tree = tb.Treeview(new_window, columns=("ID", "Name", "Phone Number"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Phone Number", text="Phone Number")
    tree.pack()

    try:
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="test")
        my_cursor = conn.cursor()

        # Execute a SELECT query to retrieve all data from the table
        select_query = "SELECT * FROM students"
        my_cursor.execute(select_query)

        # Retrieve the result as a list of rows
        rows = my_cursor.fetchall()

        # Clear any existing data in the Treeview
        for row in tree.get_children():
            tree.delete(row)

        # Populate the Treeview with the retrieved data
        for row in rows:
            tree.insert("", "end", values=row)

        my_cursor.close()
        conn.close()

    except mysql.connector.Error as error:
        print("Error:", error)
    def refresh_data():
        # Clear any existing data in the Treeview
        for row in tree.get_children():
            tree.delete(row)

        # Re-run the logic to fetch and display data
        fetch_and_display_data()

    refresh_button = tb.Button(new_window, text="Refresh Data", command=refresh_data, bootstyle="primary")
    refresh_button.pack()

    def fetch_and_display_data():
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="test")
            my_cursor = conn.cursor()

            # Execute a SELECT query to retrieve all data from the table
            select_query = "SELECT * FROM students"
            my_cursor.execute(select_query)

            # Retrieve the result as a list of rows
            rows = my_cursor.fetchall()

            # Populate the Treeview with the retrieved data
            for row in rows:
                tree.insert("", "end", values=row)

            my_cursor.close()
            conn.close()

        except mysql.connector.Error as error:
            print("Error:", error)

 

#widgets

id_label = tb.Label(root,text="ID",font=("Helvetica",15),bootstyle="info")
id_label.place(x=40,y=20)
phone_label = tb.Label(root,text="Number",font=("Helvetica",15),bootstyle="info")
phone_label.place(x=40,y=60)
name_label = tb.Label(root,text="Name",font=("Helvetica",15),bootstyle="info")
name_label.place(x=40,y= 100)

id_entry = tb.Entry(root)
id_entry.place(x=160,y=20)
phone_entry = tb.Entry(root)
phone_entry.place(x=160, y=60)
name_entry = tb.Entry(root)
name_entry.place(x=160,y=100)

Insert_Button = tb.Button(root,text="Insert",command=insert,bootstyle="success")
Insert_Button.place(x=200, y=150)

Delete_Button = tb.Button(root,text="Delete",command=delete,bootstyle="danger")
Delete_Button.place(x=120, y=150)


Update_Button = tb.Button(root,text="Update",command=Update,bootstyle="warning")
Update_Button.place(x=275, y=150)

Get_Button = tb.Button(root,text="Show",command=Show,bootstyle="primary")
Get_Button.place(x=360, y=150)
root.mainloop()