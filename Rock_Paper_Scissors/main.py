#Learning python with rock/paper/scissors

#Importing the random library
#This library helps us generate random choices
import random


#Function that gets a choice
def get_choices():
    #Player input is required
    player_choice = input("Enter a choice: ")

    #List of possible options
    options = ["rock","paper","scissors"]

    #Getting the computer choice
    computer_choice = random.choice(options)

    #Storing the choices for both in a dictionary
    choices = {"player":player_choice, "computer":computer_choice}
    return choices

def check_win( player, computer):
    print(f"You chose {player}")
    print(f"The computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock, Computer wins!"
        if computer == "scissors":
            return "Rock smashes scissors, Player wins!"
    
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock, Player wins!"
        if computer == "scissors":
            return "Scissors cut paper, Computer wins!"

    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors, Computer wins!"
        if computer == "paper":
            return "Scissors cut paper, Player wins!"
        

choices = get_choices()

result = check_win(choices["player"],choices["computer"])

print(result)