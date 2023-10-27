import tkinter as tk
from tkinter import Menu
import all_campaign
import add_campaign
    
def homepage(window):
    camp1 = tk.Frame(window, width=400, height=500, bg='white', padx=50, pady=50)
    camp2 = tk.Frame(window, bg='white', padx=100, pady=100)
    def show():        
        all_campaign.homepage(camp2)
        camp2.pack(fill='both', expand=True, side='bottom')
        camp1.pack_forget()
    def add():
        add_campaign.homepage(camp1)
        camp1.place(relx=.5, rely=.4, anchor='center')
        camp2.pack_forget()
        
    
    window.configure(bg='#F3F4F6')        
    frame = tk.Frame(window, bg='black')
    
    menubar = Menu(window, background='#1F2937', foreground='#ffffff')  
    menubar.add_command(label="Add Campaign", command=add, activebackground='blue',activeforeground='white')  
    menubar.add_command(label="Show Campaign", command=show, activebackground='blue', activeforeground='white')  
    
    # display the menu  
    window.config(menu = menubar)  
    
    add_campaign.homepage(camp1)
    camp1.place(relx=.5, rely=.4, anchor='center')
    return frame

def after_login(lf, window):
    lf.place_forget()
    dframe = homepage(window)
    dframe.pack()
    