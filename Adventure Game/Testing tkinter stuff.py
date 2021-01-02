from tkinter import * 

root = Tk() 

e = Entry(root, fg="green", bg="red")
e.pack()

def myClick():
    myLabel = Label(root,text="You clicked the button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", padx=100, pady=50, command=myClick, fg="white", bg="black")
myButton.pack()

root.mainloop()