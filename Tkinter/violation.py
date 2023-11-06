import tkinter as tk
import sqlite3
from tkinter import messagebox

# Function to submit a violation
def submit_violation():
    student_name = student_name_entry.get()
    violation_type = violation_type_entry.get()
    violation_description = violation_description_entry.get()

    # Check if any field is empty
    if not student_name or not violation_type or not violation_description:
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        # Insert the violation into the database
        try:
            conn = sqlite3.connect("violations.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO violations (student_name, violation_type, violation_description) VALUES (?, ?, ?)", (student_name, violation_type, violation_description))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Violation recorded successfully.")
            # Clear the entry fields
            student_name_entry.delete(0, tk.END)
            violation_type_entry.delete(0, tk.END)
            violation_description_entry.delete(0, tk.END)
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if conn:
                conn.close()

# Create the main window
root = tk.Tk()
root.title("Violation Entry Form")

# Create and place student name label and entry field
student_name_label = tk.Label(root, text="Student Name:")
student_name_label.pack()
student_name_entry = tk.Entry(root)
student_name_entry.pack()

# Create and place violation type label and entry field
violation_type_label = tk.Label(root, text="Violation Type:")
violation_type_label.pack()
violation_type_entry = tk.Entry(root)
violation_type_entry.pack()

# Create and place violation description label and entry field
violation_description_label = tk.Label(root, text="Violation Description:")
violation_description_label.pack()
violation_description_entry = tk.Entry(root)
violation_description_entry.pack()

# Create and place submit button
submit_button = tk.Button(root, text="Submit Violation", command=submit_violation)
submit_button.pack()

# Start the GUI event loop
root.mainloop()