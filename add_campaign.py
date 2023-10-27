import tkinter as tk
from tkinter import ttk
import mysql.connector as myconn
import dotenv

mydb = myconn.connect(host='localhost', user='root', password=dotenv.password, database='campaigns')
db_cursor = mydb.cursor()


def homepage(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
    def add_campaigns():
        search_urls = search_url_entry.get("1.0",'end-1c')
        all_campaigns = campaign_entry.get()
        status_value = status_dropdown.get()
        schedule_value = schedule_dropdown.get()
        db_cursor.execute('insert into mycampaigns(name, status, schedule, search_url) values(%s, %s, %s, %s)', (all_campaigns,status_value, schedule_value, search_urls))
        mydb.commit()
        print(db_cursor.rowcount, ' row inserted')
        
    frame['relief'] = 'solid'

    campaign_name = tk.Label(frame, text='Campaign Name', bg='white', fg='black', anchor="w", justify="left", width=100)
    campaign_entry = tk.Entry(frame, relief="flat", width=100,
                            highlightbackground='grey', highlightcolor='#1155cc', highlightthickness=1)
    status_label = tk.Label(frame, text='Status', bg='white', fg='black', anchor="w", justify="left", width=100)

    status_dropdown = ttk.Combobox(frame, width=100)
    status_dropdown['values'] = ('Active', 'Paused')
    status_dropdown.current(0)
    schedule_label = tk.Label(frame, text='Schedule', bg='white', fg='black', anchor="w", justify="left", width=100)

    schedule_dropdown = ttk.Combobox(frame, width=100)
    schedule_dropdown['values'] = ('1 Week', '2 Week', '3 Week', '4 Week')
    schedule_dropdown.current(0)
    search_url = tk.Label(frame, text="Search URL", bg='white', fg='black',
                        anchor="w", justify="left", width=100)
    search_url_entry = tk.Text(frame, height=3, relief="flat", highlightbackground='grey', width=100,
                                        highlightcolor='#1155cc', highlightthickness=1)
    save_btn = tk.Button(frame, text="SAVE", bg="#1F2937", fg="#ffffff", activebackground='#374151', width=10,  relief="flat", font= ('Poppins', 11, 'bold'), command=add_campaigns)
    campaign_name.pack(fill=tk.X)
    campaign_entry.pack(fill=tk.X, pady=[5, 15], padx=3)
    status_label.pack(fill=tk.X)
    status_dropdown.pack(fill=tk.X, pady=[5, 15], padx=3)
    schedule_label.pack(fill=tk.X)
    schedule_dropdown.pack(fill=tk.X, pady=[5, 15], padx=3)
    search_url.pack(fill=tk.X)
    search_url_entry.pack(fill=tk.X, pady=[5, 15], padx=3)
    save_btn.pack(side="left", padx=3)


