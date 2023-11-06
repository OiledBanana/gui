import tkinter as tk
from tkinter import messagebox

# Function to validate the login
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Replace 'your_username' and 'your_password' with your actual login credentials
    if username == 'your_username' and password == 'your_password':
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login App")

# Create and place username label and entry field
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create and place password label and entry field
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # 'show' attribute hides the password
password_entry.pack()

# Create and place login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack()

# Start the GUI event loop
root.mainloop()