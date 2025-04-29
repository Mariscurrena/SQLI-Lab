import tkinter
from tkinter import messagebox
import pymysql

window = tkinter.Tk()
window.geometry("1200x720")
window.title("MySQL Query using Tkinter")
window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=2)
window.configure(background="#e1e9f7")

def users(data):
    connection = pymysql.connect(user='pythonuser', 
                             passwd='pass1234',
                             host='localhost',
                             db='Prueb1')
    cur = connection.cursor()
    cur.execute("SELECT " + data + " FROM firsttable;")
    data = []
    for i in cur.fetchall():
        data.append(i)
    cur.close()
    return data

def entry():
    user_entry = textfield.get()
    value_gotten = users(user_entry)
    label["text"] = value_gotten
    messagebox.showinfo("Well Done!!","Query performed successfully!!")

textfield = tkinter.Entry(window, font="Helvetica 30")
button = tkinter.Button(window, text="Submit", font="Helvetica 25", bg = "#00296f", fg="white", padx=40, pady=30, command=entry)
label = tkinter.Label(window, font="Helvetica 25", bg="#faf4cc")

textfield.grid(column=0, row=0)
button.grid(column=1, row=0)
label.grid(column=0, row=1, columnspan=2, sticky='nsew')

window.mainloop()