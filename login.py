import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import dashboard

def login_frame(window):
    def login(event=None):
        username = 'kuware@kuware.com'
        password = 'kuware@$'
        if user.get() == username and passw.get() == password:
            messagebox.showinfo(title='success', message='logging in...')
            dashboard.after_login(frame, window)
        elif user.get() == "":
            messagebox.showerror('Invalid', 'Username is required')
        elif passw.get() == "":
            messagebox.showerror('Invalid', 'Password is required')
        elif user.get() != 'kuware@kuware.com' and passw.get() != 'kuware@$':
            messagebox.showerror('Invalid', 'Invalid username and password')
        elif passw.get() != 'kuware@$':
            messagebox.showerror('Invalid', 'Please enter a valid password')
        elif user.get() != 'kuware@kuware.com':
            messagebox.showerror('Invalid', 'Please enter a valid username')

    frame = tk.Frame(window, bg='white', padx=80, pady=50)
    user = tk.StringVar()
    passw = tk.StringVar()
    img = ImageTk.PhotoImage(Image.open('login-vector.png'))
    image = tk.Label(frame, image=img, bg="#fff", width="450")
    image.image = img
    image.pack(side='left', anchor='center')
    frame2 = tk.Frame(frame, bg='white')
    user_label = tk.Label(frame2, text='Username*', bg='white', fg='black', anchor="w", justify="left", width=52)
    user_entry = tk.Entry(frame2, font=('poppins', 12), textvariable=user, relief="flat", width=40,
                          highlightbackground='grey', highlightcolor='#1155cc', highlightthickness=1)
    password_label = tk.Label(frame2, text='Password*', bg='white', fg='black', anchor="w", justify="left", width=40)
    password_entry = tk.Entry(frame2, show='*',font=('poppins', 12), textvariable=passw, relief="flat", width=40,
                              highlightbackground='grey', highlightcolor='#1155cc', highlightthickness=1)
    login_button = tk.Button(frame2, text='Login', bg="#1F2937", fg="#ffffff", activebackground='#374151',
                             activeforeground='#ffffff', width=10, relief="flat", font=('Poppins', 11, 'bold'),
                             cursor='hand2', command=login)

    password_entry.focus()
    user_entry.focus()
    user_label.pack()
    user_entry.pack(pady=(5, 15), padx=3)
    password_label.pack(fill=tk.X)
    password_entry.pack(pady=(5, 15), padx=3)
    login_button.pack(pady=20)
    frame2.pack(side='right', padx=(50, 0))

    window.bind('<Return>', login)

    return frame