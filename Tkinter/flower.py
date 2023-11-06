import tkinter as tk

def draw_flower():
    # Clear the canvas
    canvas.delete("all")
    
    # Stem
    canvas.create_rectangle(145, 200, 155, 400, fill="green", outline="green")
    
    # Petals
    petal_colors = ["red", "orange", "yellow", "pink", "purple"]
    for i in range(5):
        angle = 360 / 5 * i  # Angle between petals
        x1 = 150 + 50 * (1.5 - i % 2) * (1 - 0.1 * i)
        y1 = 200
        x2 = x1 + 20
        y2 = 300
        canvas.create_oval(x1, y1, x2, y2, fill=petal_colors[i], outline=petal_colors[i])
        canvas.create_arc(x1 - 10, y1 - 30, x2 + 10, y2 - 30, start=45, extent=90, style=tk.CHORD, fill=petal_colors[i], outline=petal_colors[i])
    
    # Flower center
    canvas.create_oval(140, 240, 160, 260, fill="yellow", outline="orange")

# Create the main window
root = tk.Tk()
root.title("Beautiful Flower")

# Create a canvas to draw the flower on
canvas = tk.Canvas(root, width=300, height=400)
canvas.pack()

# Create a button to draw the flower
draw_button = tk.Button(root, text="Draw Flower", command=draw_flower)
draw_button.pack()

# Draw the flower initially
draw_flower()

# Start the Tkinter main loop
root.mainloop()