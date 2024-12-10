#In order to have a better control into the widgets position, we can use the Grid Method
import tkinter

window = tkinter.Tk()
window.geometry("1200x720")

button1 = tkinter.Button(window, text="Button1", font="Helvetica 25", fg="Blue", width=15, height=2)
button2 = tkinter.Button(window, text="Button2", font="Helvetica 25", fg="Red", width=15, height=2)
button3 = tkinter.Button(window, text="Button3", font="Helvetica 25", fg="Green", width=15, height=2)

button1.grid(row=0, column=0)
button2.grid(row=1, column=1)
button3.grid(row=2, column=2)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.mainloop()