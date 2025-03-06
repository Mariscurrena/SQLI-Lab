import tkinter
import pymysql
from tkinter import messagebox
from PIL import Image, ImageTk

#Window COnfiguration
window = tkinter.Tk()
window.geometry("1200x720")
window.title("Code Injection Lab - Unsecure")
window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.configure(background="#ffffff")

#MySQL Connection
connection = pymysql.connect(user='root', 
                             passwd='admin1234',
                             host='localhost',
                             db='Prueb1')

def validate():
    user= str("'" + User_Entry.get() + "'")
    password= str("'" + Pass_Entry.get() + "'")
    cur = connection.cursor()
    query = f"SELECT * FROM firsttable WHERE name = {user} AND password = {password}"
    cur.execute(query)
    results = cur.fetchall()
    if results:
        messagebox.showinfo("Login Successful!!","Hello There, it's nice to see you again c:")
    else:
        messagebox.showinfo("Oh no!!!","Credentials Invalid. Try again :c")
    cur.close()


#Forms Declaration
Login_Label = tkinter.Label(window, text="LOGIN", font="Helvetica 60 bold", bg="#ffffff", fg="#1A6AFF")
User_Label = tkinter.Label(window, text="Username", bg="#ffffff", fg="#1A6AFF", font="Helvetica 20 bold")
Pass_Label = tkinter.Label(window, text="Password", bg="#ffffff", fg="#1A6AFF", font="Helvetica 20 bold")
User_Entry = tkinter.Entry(window, bg="#f2f2f2", fg="#000a2d", font="Helvetica 22 bold")
Pass_Entry = tkinter.Entry(window, bg="#f2f2f2", fg="#000a2d", font="Helvetica 22 bold")
Button = tkinter.Button(window, text="Submit", fg="#ffffff", bg="#1A6AFF", font="Helvetica 30", padx=20, pady=10, command=validate)
Label_SQL = tkinter.Label(window, text="SQL Injection", font="Helvetica 45 bold", bg="#ffffff", fg="#1A6AFF")

#Image Declaration
image = Image.open("./logo.png")
image = image.resize((300,300))
image_tk = ImageTk.PhotoImage(image)
Image_Label = tkinter.Label(window, image=image_tk, bg="#ffffff")

#Grid declaration
Login_Label.grid(column=1, row=0, columnspan=3, sticky='nsew')
User_Label.grid(column= 1, row= 1, sticky='e')
Pass_Label.grid(column= 1, row= 2, sticky='e')
User_Entry.grid(column=2, row=1, columnspan=2, sticky='we', padx=(50,50))
Pass_Entry.grid(column=2, row=2, columnspan=2, sticky='we', padx=(50,50))
Button.grid(column=1, row=3, columnspan=3, sticky="we", padx=(50,50))
Image_Label.grid(column=0, row=0, rowspan=3)
Label_SQL.grid(column=0, row=3, sticky='n')

#Show window
window.mainloop()