import tkinter as tk

count = 0

def sub():
    global count
    count -= 1
    label.config(text=f"{count}")

def add():
    global count
    count += 1
    label.config(text=f"{count}")

def multiply():
    global count
    count *= 2
    label.config(text=f"{count}")

def reset():
    global count
    count = 0
    label.config(text=f"{count}")

root = tk.Tk()
root.geometry("150x110")
root.title("Counter")

label = tk.Label(root, text="0", font=("Helvetica", 20))
label.grid(row=0, column=0, columnspan=3, pady=5)

button1 = tk.Button(root, text="+", width=4, command=add)
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = tk.Button(root, text="-", width=4, command=sub)
button2.grid(row=1, column=1, padx=10, pady=10)

button4 = tk.Button(root, text="x2", width=4, command=multiply)
button4.grid(row=1, column=2, padx=10, pady=10)

button3 = tk.Button(root, text="Reset", width=14, command=reset)
button3.grid(row=2, column=0, columnspan=3, pady=5)

root.mainloop()

