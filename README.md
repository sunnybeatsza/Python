
# Rock, Paper, Scissors Game

This is a simple Python implementation of the classic "Rock, Paper, Scissors" game. The code allows the user to play against the computer by choosing rock, paper, or scissors. The computer randomly selects its choice, and the winner is determined based on the game's rules.

## Features

- Takes user input for their choice (rock, paper, or scissors).
- The computer's choice is randomly selected.
- Determines the winner using standard game rules.
- Handles ties if both player and computer choose the same option.
- Displays results including both player's and computer's choices.

## How it Works

1. **Input**: The user is prompted to enter a choice (`rock`, `paper`, or `scissors`). 
2. **Randomization**: The computer's choice is randomly selected from the same options.
3. **Comparison**: The player's and computer's choices are compared to determine the winner:
   - Rock smashes Scissors.
   - Paper covers Rock.
   - Scissors cut Paper.
4. **Output**: The result is displayed, indicating whether the player won, lost, or tied.

## Code Breakdown

### Importing Libraries
```python
import random
```
- The `random` library is used to allow the computer to make a random choice.

### `get_choices` Function
This function is responsible for:
- Taking the player's choice as input.
- Randomly selecting the computer's choice from a list of options (`rock`, `paper`, or `scissors`).
- Storing the choices in a dictionary and returning them.

```python
def get_choices():
    player_choice = input("Enter a choice: ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
```

### `check_win` Function
This function:
- Takes both the player's and the computer's choices.
- Compares them to determine the result of the game based on the game's rules.
- Returns a string describing the outcome (win, lose, or tie).

```python
def check_win(player, computer):
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
```

### Main Program Flow
The game starts by calling `get_choices` to retrieve both the player's and computer's choices. Then, the `check_win` function is called to determine the winner, and the result is printed.

```python
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
```

## How to Run the Code

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/rock-paper-scissors.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rock-paper-scissors
   ```
3. Run the script:
   ```bash
   python rock_paper_scissors.py
   ```

## Future Improvements
- Add input validation to ensure only valid choices (rock, paper, or scissors) are entered.
- Implement a loop to allow multiple rounds without restarting the program.
- Add score tracking for both the player and the computer.

---

Feel free to replace `yourusername` with your actual GitHub username and the filename with the actual name of your script!
