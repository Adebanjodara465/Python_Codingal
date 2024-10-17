from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.title('image')
root.geometry('300x350')

#opening the image
upload = Image.open("picf.jpg")

#the image has to be tkinter compactible
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350, width=370)
label.place(x=50, y=0)
label2 = Label(root, text="This is how you add an image in tkinter")
label2.place(x=40, y=360)

root.mainloop()