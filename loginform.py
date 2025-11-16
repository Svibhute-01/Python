import tkinter as tk

def login():
    user = username.get()
    pwd = password.get()
    print("Username:", user)
    print("Password:", pwd)
    msg.config(text="Login Successful!", fg="green")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x250")

tk.Label(root, text="Username:").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password:").pack()
password = tk.Entry(root, show="*")
password.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

msg = tk.Label(root, text="")
msg.pack()

root.mainloop()
