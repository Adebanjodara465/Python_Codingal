from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.title('image')
root.geometry('500x500')

#opening the image
upload = Image.open(r"C:\Users\HP\Desktop\Python_Codingal\Tkinter\picff.jpg")
upload = upload.resize((370, 350), Image.Resampling.LANCZOS)

#the image has to be tkinter compactible
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image)
label.place(x=50, y=0)
label2 = Label(root, text="This is how you add an image in tkinter")
label2.place(x=40, y=360)

root.mainloop()