from tkinter import *


root = Tk()
root.title("Learning stuff")

my_img = image.PhotoImage(Image.open("C:/Users/btran/OneDrive/Documents/School Documents/Grade 11/ICS3U/bear.png"))
my_label = Label(image-my_img)
my_label.pack()

#icon created
root.iconbitmap('C:/Users/btran/OneDrive/Documents/School Documents/Grade 11/ICS3U/clawmarks icon.ico')

















#quit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()