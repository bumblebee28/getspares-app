import tkinter as tk
import login

window = tk.Tk()
window.title('Getspares')
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("%dx%d" % (width, height))
window.configure(bg='#F3F4F6')

login_frame = login.login_frame(window)
login_frame.place(relx=.5, rely=.4, anchor='center')


window.mainloop() 