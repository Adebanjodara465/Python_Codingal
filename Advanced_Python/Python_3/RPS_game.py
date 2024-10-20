#set up a tkinter window
from tkinter import*
import random

root = Tk()
root.title("Rock, Paper, Scissors game")    #TODO: ADD A COUNTER    AND ADD IMAGES
root.geometry("500x400")

result = StringVar()
result.set("Welcome to the game")

def play(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
#the if statements

    if player_choice == computer_choice:
      result.set(f"Both of you picked {player_choice}. It's a tie!!!")

    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
     (player_choice == "Paper" and computer_choice == "Rock") or \
     (player_choice == "Scissors" and computer_choice == "Paper"):
     result.set(f"You chose {player_choice}, and Computer chose {computer_choice}. Hence, you WIN!")
 
    
    else:
     result.set(f"You chose {player_choice}, but Computer chose {computer_choice}. Hence, you loose. HAHAHAHAHAHAHHA") 
    
           
#add buttons for rock paper scissors
R_button = Button(root, text="Rock", command=lambda:play("Rock"))
R_button.pack(padx=20, pady=20)

P_button = Button(root, text="Paper", command=lambda:play("Paper"))
P_button.pack(padx=40, pady=40)

S_button = Button(root, text="Scissors", command=lambda:play("Scissors"))
S_button.pack(padx=50, pady=50)

#display results on the UI
label = Label(root, textvariable=result, fg="green" )
label.pack(pady=0, padx=80)

root.mainloop()
