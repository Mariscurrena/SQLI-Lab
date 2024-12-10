import tkinter

#Create the container
window = tkinter.Tk()
window.geometry("1200x720") #Resize the window
window.configure(background="#eaeaea")

#Create a label
label = tkinter.Label(window, text = "Hello World", 
                                bg = "#33abff", 
                                font=("Arial",25))
label.pack(side= tkinter.TOP, fill = tkinter.X) #This shows and allign the element

#Create a button
def saludo(name):
    print("Hola "+name)

button = tkinter.Button(window, text = "Press Here!",
                                bg = "#040027", 
                                fg="white",
                                font=("Arial",20),
                                padx=40,
                                pady=30,
                                command= lambda: saludo("Python"))#This allows to perform an action
button.pack()

#Create a TextField
textfield = tkinter.Entry(window, font="Helvetica 25")
textfield.pack()

#Get text with an action button from an entry
def gettext():
    text = textfield.get()
    print(text)

buttonaction = tkinter.Button(window, text="Get text",
                                bg = "#090054", 
                                fg="white",
                                font=("Arial",20),
                                padx=40,
                                pady=30,
                                command=gettext)
buttonaction.pack()

#Print text from an entry to a label using a button
def entrytolabel():
    text = textfield2.get()
    label2["text"] = text
textfield2 = tkinter.Entry(window, font="Helvetica 25")
textfield2.pack()
label2 = tkinter.Label(window, font="Helvetica 25", fg="DARK RED")
label2.pack()
buttonaction2 = tkinter.Button(window, text="Get text",
                                bg = "#00296f", 
                                fg="white",
                                font=("Arial",20),
                                padx=40,
                                pady=30,
                                command=entrytolabel)
buttonaction2.pack()

#Main loop, this allows to perform actions into the window
window.mainloop()