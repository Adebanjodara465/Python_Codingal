import random
import string
from tkinter import*

def generate_password(length):
    #making the first character a letter
    first_char = random.choice(string.ascii_letters)
    #getting the characters i need
    characters = string.ascii_letters + string.digits + string.punctuation

#code to randomly select characters
    remaining_chars = ''.join(random.choice(characters) for i in range(length - 1))
    password =  first_char + remaining_chars
    return password

#time to show the password
def show_password():
    length = 10
    generated_password = generate_password(length)
    password_label.config(text=generated_password)
    
#creating the tkinter window
window = Tk()
window.title("See your random passwords")
window.geometry('400x450')

password_label = Label(window, text="Your password will appear here", bg="yellow")
password_label.pack(pady=40)

#a button to generate the password
generate_button = Button(window, text="Generate your password", command=show_password, bg="pink", fg="brown", relief=RAISED)
generate_button.pack(pady=60)

window.mainloop()
