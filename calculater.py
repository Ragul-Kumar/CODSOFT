import tkinter as tk

def setup():
    set_table.set("")

def calculate(event):
    current = set_table.get()
    clicked_button = event.widget.cget("text")

    if clicked_button == "=":
        try:
            result = eval(current)
            set_table.set(result)
        except:
            set_table.set("Error")
    elif clicked_button == "C":
        setup()
    else:
        set_table.set(current + clicked_button)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#2C3E50")  # Change background color
root.geometry("400x500")

set_table = tk.StringVar()

display_entry = tk.Entry(root, textvariable=set_table, font=("Arial", 20), bd=10, bg="#34495E", fg="white")
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

buttons = [
    ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("%", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, fg="white", bg="#27AE60", padx=25, pady=20, font=("Arial", 15), bd=5)
    elif text == "C":
        button = tk.Button(root, text=text, fg="white", bg="#E74C3C", padx=25, pady=20, font=("Arial", 15), bd=5)
    else:
        button = tk.Button(root, text=text, fg="black", bg="white", padx=25, pady=20, font=("Arial", 15), bd=5)

    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    button.bind("<Button-1>", calculate)

root.grid_columnconfigure((0, 1, 2, 3), weight=1)  # Make columns expandable
root.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)  # Make rows expandable

root.mainloop()
