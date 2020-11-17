#Pet
#Imports Random Module
import random


input("Rock, Paper, Scissors! Hit ENTER to play!")
#Naming of vars
PlayerWins = 0
ComputerWins = 0
ties = 0
rounds = 0
moveInt = 0


#Player Move
def moveDef():
    move = input("\nWhat is your move? ")
    if move == "Rock" or move == "rock":
        moveInt = 1
        print(moveInt)

    elif move == "Paper" or move == "paper":
        moveInt = 2
        print(moveInt)

    elif move == "Scissors" or move == "scissors":
        moveInt = 3
        print(moveInt)
    else:
        input("\nInvalid answer.")
        moveDef()
moveDef()


