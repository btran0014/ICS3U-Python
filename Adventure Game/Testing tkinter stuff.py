#import everything from tkinter
from tkinter import * 
#opens the window (root widget)
root = Tk() 
#creating a Label Widget
myLabel = Label(root,text=" This is a test. Hello Brian! This is a basic GUI! ") 
#putting it on the screen
myLabel.pack() 

root.mainloop()