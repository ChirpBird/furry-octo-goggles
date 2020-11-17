#Imports Random Module
import random

def RockPaper():
    input("Rock, Paper, Scissors! Hit ENTER to play!")
#Naming of vars
    PlayerWins = 0
    ComputerWins = 0
    ties = 0
    rounds = 0
    moveInt = 0
    
#Chance is used here
    while rounds < 3:

    #Player Move
        def moveDef():
            move = input("\nWhat is your move? ")
            if move == "Rock" or move == "rock":
                moveInt = 1

            elif move == "Paper" or move == "paper":
                moveInt = 2

            elif move == "Scissors" or move == "scissors":
                moveInt = 3
            else:
                input("\nInvalid answer.")
                moveDef()
        moveDef()
            
        chance = random.randint(1,3)
        if chance == 3:
            print("\nComputer Plays: Scissors")
            rounds = rounds + 1
            if moveInt == 3:
                ties = ties + 1
                print("\nTie!")
                print("\nLosses: " + str(ComputerWins) + "\nWins: " + str(PlayerWins) + "\nTies: " + str(ties))
            elif moveInt == 2:
                ComputerWins = ComputerWins + 1
                print("\nLosses: " + str(ComputerWins) + "\nWins: " + str(PlayerWins) + "\nTies: " + str(ties))
            else:
                PlayerWins = PlayerWins + 1
                print("\nLosses: " + str(ComputerWins) + "\nWins: " + str(PlayerWins) + "\nTies: " + str(ties))

        elif chance == 2:
            print("\nComputer Plays: Paper")
            rounds = rounds + 1
            if moveInt == 2:
                ties = ties + 1
                print("\nLosses: " + str(ComputerWins) + "\nWins: " + str(PlayerWins) + "\nTies: " + str(ties))
            elif moveInt == 1:
                ComputerWins = ComputerWins + 1
                print("\nLosses: " + str(ComputerWins) + "\nWins: " + str(PlayerWins) + "\nTies: " + str(ties))
            else:
                PlayerWins = PlayerWins + 1
                print("\nLosses: " + str(ComputerWins) + "\nWins: " + str(PlayerWins) + "\nTies: " + str(ties))
            
            
        else:
            print("\nComputer Plays: Rock")
            rounds = rounds + 1
            if moveInt == 1:
                ties = ties + 1
                print("\nLosses: " + str(ComputerWins) + "\nWins: " + str(PlayerWins) + "\nTies: " + str(ties))
            elif moveInt == 3:
                ComputerWins = ComputerWins + 1
                print("\nLosses: " + str(ComputerWins) + "\nWins: " + str(PlayerWins) + "\nTies: " + str(ties))
            else:
                PlayerWins = PlayerWins + 1
                print("\nLosses: " + str(ComputerWins) + "\nWins: " + str(PlayerWins) + "\nTies: " + str(ties))
            
#Glitching right now.
#Edit. Fixed. Hee hee hee.
        



RockPaper()

playAgain = input("\nPlay Again?")

while playAgain == "yes" or playAgain == "Yes" or playAgain == "y" or playAgain == "Y":
    RockPaper()
