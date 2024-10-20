from tkinter import *
import random

# Make the tkinter window
root = Tk()
root.title("RPS Game")
root.geometry('300x400')

result_label = Label(root, text="Let's play!", font=("Helvetica", 16))
result_label.pack(pady=20)

def game(player_pick):
    pick = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(pick)
    
    if player_pick == computer_choice:
        result = "It's a tie!"
        result_label.config(fg='yellow')
    
    elif (player_pick == "Rock" and computer_choice == "Scissors") or \
         (player_pick == "Paper" and computer_choice == "Rock") or \
         (player_pick == "Scissors" and computer_choice == "Paper"):
        result = f"You chose {player_pick}, computer chose {computer_choice}.\nYou WINNNNN!"
        result_label.config(fg='green')             
 
    else:
        result = f"You chose {player_pick}, computer chose {computer_choice}.\nYou LOSEEEE!"
        result_label.config(fg='red')

    result_label.config(text=result)   

# Create a frame to hold the buttons
frame = Frame(root, borderwidth=10)
frame.pack(pady=10)


button_1 = Button(frame, text="Rock", relief=RAISED, command=lambda: game("Rock")) 
button_1.pack(side=LEFT, padx=10)

button_2 = Button(frame, text="Paper", relief=RAISED, command=lambda: game("Paper")) 
button_2.pack(side=LEFT, padx=10)

button_3 = Button(frame, text="Scissors", relief=RAISED, command=lambda: game("Scissors")) 
button_3.pack(side=LEFT, padx=10)    

root.mainloop()
