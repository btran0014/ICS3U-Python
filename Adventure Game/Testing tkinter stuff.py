from tkinter import * 

root = Tk() 

e = Entry(root, fg="green", bg="red")
e.pack()
e.insert(0,"Enter Your Name In This Box")

def myClick():
    name_is = "Your name is: " + e.get()
    myLabel = Label(root, text = name_is)
    myLabel.pack()

myButton = Button(root, text="Your Statement", padx=100, pady=50, command=myClick, fg="white", bg="black")
myButton.pack()

root.mainloop()