#import everything from tkinter
from tkinter import * 

#opens the window (root widget)
root = Tk() 

myButton = Button(root, text="Click Me!", padx=50, pady=50)
myButton.pack()
root.mainloop()

 