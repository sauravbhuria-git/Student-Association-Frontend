import tkinter as tk
from tkinter import messagebox
import random
import string

# Store user (temporary)
stored_user = {}

# Generate Captcha
def generate_captcha():
    chars = string.ascii_uppercase + string.digits
    captcha = ''.join(random.choice(chars) for _ in range(5))
    captcha_label.config(text=captcha)
    return captcha

# Check password match
def check_password(*args):
    if pass_var.get() != confirm_var.get():
        pass_error.config(text="Passwords do not match!", fg="red")
    else:
        pass_error.config(text="Passwords match ✅", fg="green")

# Register
def register():
    if pass_var.get() != confirm_var.get():
        messagebox.showerror("Error", "Passwords must match!")
        return
    
    if captcha_entry.get() != captcha_label.cget("text"):
        messagebox.showerror("Error", "Invalid Captcha")
        generate_captcha()
        return
    
    stored_user["email"] = email_var.get()
    stored_user["password"] = pass_var.get()

    messagebox.showinfo("Success", "Account Created!")
    show_login()

# Login
def login():
    if (email_login.get() == stored_user.get("email") and
        pass_login.get() == stored_user.get("password")):
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Credentials")

# Switch Frames
def show_signup():
    login_frame.pack_forget()
    signup_frame.pack()

def show_login():
    signup_frame.pack_forget()
    login_frame.pack()

# GUI Setup
root = tk.Tk()
root.title("Student Association")
root.geometry("400x550")

# ---------------- LOGIN FRAME ----------------
login_frame = tk.Frame(root)

tk.Label(login_frame, text="Login", font=("Arial", 16)).pack(pady=10)

email_login = tk.Entry(login_frame)
email_login.pack(pady=5)
email_login.insert(0, "Student ID")

pass_login = tk.Entry(login_frame, show="*")
pass_login.pack(pady=5)

tk.Button(login_frame, text="Login", command=login).pack(pady=10)

tk.Button(login_frame, text="Create Account", command=show_signup).pack()

login_frame.pack()

# ---------------- SIGNUP FRAME ----------------
signup_frame = tk.Frame(root)

tk.Label(signup_frame, text="Create Account", font=("Arial", 16)).pack(pady=10)

name_var = tk.StringVar()
email_var = tk.StringVar()
pass_var = tk.StringVar()
confirm_var = tk.StringVar()

tk.Entry(signup_frame, textvariable=name_var).pack(pady=5)
tk.Entry(signup_frame, textvariable=email_var).pack(pady=5)

tk.Entry(signup_frame, textvariable=pass_var, show="*").pack(pady=5)
tk.Entry(signup_frame, textvariable=confirm_var, show="*").pack(pady=5)

pass_error = tk.Label(signup_frame, text="")
pass_error.pack()

pass_var.trace("w", check_password)
confirm_var.trace("w", check_password)

# DOB
tk.Label(signup_frame, text="Date of Birth").pack()

day = tk.Spinbox(signup_frame, from_=1, to=31)
day.pack()

month = tk.Spinbox(signup_frame, values=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
month.pack()

year = tk.Spinbox(signup_frame, from_=1947, to=2026)
year.pack()

# Captcha
captcha_label = tk.Label(signup_frame, font=("Arial", 14))
captcha_label.pack(pady=5)

captcha_entry = tk.Entry(signup_frame)
captcha_entry.pack(pady=5)

generate_captcha()

tk.Button(signup_frame, text="Register", command=register).pack(pady=10)

tk.Button(signup_frame, text="Back to Login", command=show_login).pack()

root.mainloop()