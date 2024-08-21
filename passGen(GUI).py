import tkinter as tk
from tkinter import ttk
import random
import string

# Function to generate password
def generate_password():
    length = int(length_var.get())
    charset = ''
    
    if numeric_var.get():
        charset += string.digits
    if alphanumeric_var.get():
        charset += string.ascii_letters + string.digits
    if special_var.get():
        charset += string.ascii_letters + string.digits + string.punctuation
    
    if not charset:
        charset = string.ascii_letters
    
    password = ''.join(random.choice(charset) for _ in range(length))
    password_var.set(password)

# Function to copy password to clipboard
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())

# Creating the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")
root.resizable(False, False)

# Color theme matching the temperature converter
bg_color = "#0d0d0d"
fg_color = "#f0f0f0"
button_color = "#1f1f1f"
button_fg_color = "#d4d4d4"
active_button_color = "#444444"
highlight_color = "#34A2FE"

root.configure(bg=bg_color)

# Style configuration
style = ttk.Style()
style.configure('TLabel', background=bg_color, foreground=fg_color)
style.configure('TButton', background=button_color, foreground=button_fg_color, 
                padding=6, highlightthickness=0, relief='flat')
style.map('TButton', background=[('active', active_button_color)])

# Password length
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(column=0, row=0, padx=20, pady=10)

length_var = tk.IntVar(value=12)
length_spinbox = ttk.Spinbox(root, from_=4, to_=64, textvariable=length_var, width=5, justify='center')
length_spinbox.grid(column=1, row=0)

# Options: Numeric, Alphanumeric, Special Characters
numeric_var = tk.BooleanVar()
numeric_check = ttk.Checkbutton(root, text="Numeric", variable=numeric_var)
numeric_check.grid(column=0, row=1, padx=20, pady=5, sticky='w')

alphanumeric_var = tk.BooleanVar(value=True)
alphanumeric_check = ttk.Checkbutton(root, text="Alphanumeric", variable=alphanumeric_var)
alphanumeric_check.grid(column=1, row=1, padx=20, pady=5, sticky='w')

special_var = tk.BooleanVar()
special_check = ttk.Checkbutton(root, text="Special Characters", variable=special_var)
special_check.grid(column=0, row=2, padx=20, pady=5, sticky='w')

# Generate Button
generate_button = ttk.Button(root, text="Generate", command=generate_password)
generate_button.grid(column=1, row=2, padx=20, pady=10)

# Password display
password_var = tk.StringVar()
password_entry = ttk.Entry(root, textvariable=password_var, width=30, justify='center', state='readonly')
password_entry.grid(column=0, row=3, columnspan=2, padx=20, pady=10)

# Copy Button
copy_button = ttk.Button(root, text="Copy", command=copy_password)
copy_button.grid(column=0, row=4, columnspan=2, padx=20, pady=10)

root.mainloop()
