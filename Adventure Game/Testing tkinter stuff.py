from tkinter import * 

root = Tk() 

def myClick():
    myLabel = Label(root,text="You clicked the button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", padx=100, pady=50, command=myClick)
myButton.pack()
root.mainloop()

 