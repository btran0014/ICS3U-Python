from tkinter import *

root = Tk()
root.title("Alone")

prompt = "this is the scenario phrase"

#create the text box
txt_box = Text(root, width=160, height=16, borderwidth=5)
txt_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
txt_box.insert(0, prompt)

var_a= "this is option a" 
var_b= "this is option b"
var_c= "this is option c"
var_d= "this is option d"


#create buttons
answer_a = Button(root, text=var_a, padx=40, pady=4)
answer_b = Button(root, text=var_b, padx=40, pady=4)
answer_c = Button(root, text=var_c, padx=40, pady=4)
answer_d = Button(root, text=var_d, padx=40, pady=4)

#put buttons on screen in right order
answer_a.grid(row=1, column=0)
answer_b.grid(row=1, column=1)
answer_c.grid(row=2, column=0)
answer_d.grid(row=2, column=1)

root.mainloop()