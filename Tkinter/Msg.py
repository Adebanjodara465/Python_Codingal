from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry('300x350')

#then display your tkinter message
def msg():
    messagebox.showwarning("Alert", "Stop, there is a virus!!")
button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=50) 

root.mainloop()   