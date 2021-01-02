#import everything from tkinter
from tkinter import * 

#opens the window (root widget)
root = Tk() 

#creating a Label Widget
myLabel1 = Label(root,text=" This is a test. ").grid(row=0, column=0)  
myLabel2 = Label(root,text=" Hello Brian! This is a basic GUI! ").grid(row=1, column=5) 
myLabel3 = Label(root,text="              ").grid(row=1, column=1) 

#putting it on the screen
"""
myLabel1.grid(row=0, column=0) 
myLabel2.grid(row=1, column=5) 
myLabel3.grid(row=1, column=1) 
"""
root.mainloop()

 