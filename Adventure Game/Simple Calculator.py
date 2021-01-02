from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0)
e.insert(0,"Enter Your Name In This Box")
def myClick():
    name_is = "Your name is: " + e.get()
    myLabel = Label(root, text = name_is)
    myLabel.pack()

myButton = Button(root, text="Your Statement", padx=100, pady=50, command=myClick, fg="white", bg="black")
myButton.pack()

root.mainloop()