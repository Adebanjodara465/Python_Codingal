from tkinter import*

root = Tk()
root.geometry('400x550')
root.title("main")

#function to make a top level window
def topwin():
    #set up the window
    top = Toplevel()
    top.geometry('180x200')
    top.title("The top window")
    l2 = Label(top, text="This is the top level window")
    l2.pack()
    
    top.mainloop()
    
l = Label(root, text = "This is the root window")
btn = Button(root, text = "Click here to open another window", command = topwin)

#arranging the widgets
l.pack()
btn.pack()

root.mainloop()    