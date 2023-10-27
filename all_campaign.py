import tkinter as tk
from tkinter import ttk
import mysql.connector as myconn
import dotenv
import pandas as pd
import ebay_script
from ttkbootstrap import *


def homepage(frame):
    
    def run_script():
        flag = 'scrape'
        ebay_script.scraping(url, flag)
        
    def view_camp():
        flag = 'view'
        num_items = ebay_script.scraping(url, flag)
        link = url
        
    mydb = myconn.connect(host='localhost', user='root', password=dotenv.password, database='campaigns')
    db_cursor = mydb.cursor()
    # frame = tk.Frame(window, bg='white', padx=100, pady=100)
    for widget in frame.winfo_children():
        widget.destroy()
        
    mydb = myconn.connect(host='localhost', user='root', password=dotenv.password, database='campaigns')
    db_cursor = mydb.cursor()
    db_cursor.execute('select * from mycampaigns where status = "active"')
    result = db_cursor.fetchall()
    result_df = pd.DataFrame(result, columns = ['Campaign Name', 'status', 'schedule', 'urls'])
    n = result_df.shape[0]
    i = 0
    
    while i < n :
        name = result_df.iloc[i]['Campaign Name']
        status = result_df.iloc[i]['status']
        schedule = result_df.iloc[i]['schedule']
        url = result_df.iloc[i]['urls']
        
        cname = tk.Label(frame, text=name, bg='white', fg='black', anchor="w", justify="left", width=100)
        cname.pack()
        sname  = tk.Label(frame, text=status, bg='white', fg='black', anchor="w", justify="left", width=100)
        sname.pack()
        sched = tk.Label(frame, text=schedule, bg='white', fg='black', anchor="w", justify="left", width=100)
        sched.pack()
        download_button = tk.Button(frame, text='Download csv', bg="#1F2937", fg="#ffffff", activebackground='#374151',
                             activeforeground='#ffffff', width=20, relief="flat", font=('Poppins', 11, 'bold'),
                             cursor='hand2', command=run_script)
        download_button.pack()
        view_button = tk.Button(frame, text='View campaign', bg="#1F2937", fg="#ffffff", activebackground='#374151',
                             activeforeground='#ffffff', width=20, relief="flat", font=('Poppins', 11, 'bold'),
                             cursor='hand2', command=view_camp)
        view_button.pack()
        i += 1
        
        
    # db_cursor.execute('select * from mycampaigns')
    # result = db_cursor.fetchall()
    
    # trv = ttk.Treeview(frame, selectmode="browse")  
    
    # trv["height"] = 10
    # trv["show"] = "headings"
    # trv["columns"] = l1 = ['Campaign Name', 'status', 'schedule', 'keywords']
    # for i in l1:
    #     trv.column(i, width=90, anchor="c")
    #     trv.heading(i, text=i)
        
    # for i in result:
    #     v = list(i)
    #     trv.insert("", "end", iid=v[0], values=v)
        
    # trv.pack(padx=10, pady=20) 
    
    