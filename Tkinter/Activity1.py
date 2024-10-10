#working with Tkinter
from tkinter import *

window = Tk()
window.title('A window')
window.geometry('400x400')

greeting = Label(text="Hello User", fg="yellow", bg="pink")
button = Button(text="Click me", fg="blue", bg="red")
entry = Entry( fg="yellow", bg="pink", width=70)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=10)
frame.pack()
label = Label(master=frame, text='Label on Frame')
label.pack()

textbox = Text(fg='brown', bg='white')
textbox.pack()
window.mainloop()