import re
import tkinter as tk
from tkinter import ttk

# Function to check password strength
def password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))  # Special characters

    strength_score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])

    if strength_score == 5:
        return "Very Strong", "#4CAF50"  # Green
    elif strength_score == 4:
        return "Strong", "#8BC34A"  # Light green
    elif strength_score == 3:
        return "Medium", "#FFEB3B"  # Yellow
    elif strength_score == 2:
        return "Weak", "#FFC107"  # Orange
    else:
        return "Very Weak", "#F44336"  # Red

# Function to update the password strength on the GUI
def check_password():
    password = password_entry.get()
    strength, color = password_strength(password)
    result_label.config(text=f"Password Strength: {strength}", fg=color)

# Function to close the window
def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Password Strength Checker")

root.configure(bg="lightblue")

root.geometry("600x400")

frame = tk.Frame(root, bg="lightblue")  
frame.place(relx=0.5, rely=0.5, anchor='center') 

title_label = tk.Label(frame, text="PASSWORD CHECKER", font=("Aial", 24, "bold"), fg="darkblue", bg="lightblue")
title_label.grid(row=0, column=0, pady=20)

instruction_label = tk.Label(frame, text="Enter your password:", font=("Helvetica", 12, "bold"), bg="lightblue")
instruction_label.grid(row=1, column=0, pady=10)

password_entry = tk.Entry(frame, width=50,  font=("Helvetica", 12, "bold"))
password_entry.grid(row=2, column=0, pady=10, sticky="ew")  

check_button = tk.Button(frame, text="Check Password Strength", command=check_password, font=("Arial", 12, "bold"), padx=10, pady=5, bg="#007BFF", fg="white")
check_button.grid(row=3, column=0, pady=10)

result_label = tk.Label(frame, text="Password Strength:", font=("Arial", 14, "bold"), bg="lightblue")
result_label.grid(row=4, column=0, pady=10)

exit_button = tk.Button(frame, text="Exit", command=exit_app, font=("Arial", 14, "bold"), bg="red", fg="white", padx=25, pady=5)
exit_button.grid(row=5, column=0, pady=20)

root.mainloop()
