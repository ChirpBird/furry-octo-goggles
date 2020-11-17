#imports the random module
import random


#defines vars
#declares that game is not over
gameOver = False
tie = False
loss = False
win = False


#sets up the board list for the display
boardDisp = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
#list of available plays for computer's move
availPlays = [0, 1, 2, 3, 4, 5, 6, 7, 8]


#board display
#sets up board
def boardDisplay():
    print(boardDisp[0] + " | " + boardDisp[1] + " | " + boardDisp[2])
    print(boardDisp[3] + " | " + boardDisp[4] + " | " + boardDisp[5])
    print(boardDisp[6] + " | " + boardDisp[7] + " | " + boardDisp[8])

    """ -|-|-
        -|-|-
        -|-|-
    """


#handles player's turn
def handleTurn():
    try:
        position = int(input("\nWhere do you want to place your marker? (1-9, L2R, Rows) "))-1
        availPlays.remove(position)
        boardDisp.pop(position)
        boardDisp.insert(position, "X")
    except:
        input("\nWhoops! Something went wrong. Let's try that again.")
        handleTurn()


#defines computer's move
def compMove():
    if gameOver != True:
        compPos = random.choice(availPlays)
        availPlays.remove(compPos)
        boardDisp.pop(compPos)
        boardDisp.insert(compPos, "O")

        


#checks if there is a tie
def checkiftie():
    global gameOver
    global tie

    if bool(availPlays) == False:
        gameOver = True
        tie = True
        

#check if loss
def checkifloss():
    global gameOver
    global loss
    #defining variable that checks position
    x = 0
    y = 0
    while x<3:

        if boardDisp[x] == "O":
            #checking columns
            if boardDisp[x] == boardDisp[x+3] == boardDisp[x+6]:
                gameOver = True
                loss = True
            
            #checking rows
            if boardDisp[y] == boardDisp[y+1] == boardDisp[y+2]:
                gameOver = True
                loss = True
        x+=1
        y = x+3

    #checking diagonals
    if boardDisp[0] == boardDisp[4] == boardDisp[8] == "O" or boardDisp[2] == boardDisp[4] == boardDisp[6] == "O":
        loss = True
    
    #for debugging


#checks if player won
def checkifwin():
    global gameOver
    global win
    x = 0

    while x<3:

        if boardDisp[x] == "X":
            
            #checking columns
            if boardDisp[x] == boardDisp[x+3] == boardDisp[x+6]:
                gameOver = True
                win = True
            
            #checking rows
            if boardDisp[x] == boardDisp[x+1] == boardDisp[x+2]:
                gameOver = True
                win = True
        x+=1
    
    #checking diagonals
    if boardDisp[0] == boardDisp[4] == boardDisp[8] == "X" or boardDisp[2] == boardDisp[4] == boardDisp[6] == "X":
        win = True
    
    #for debugging


#checks if game is over
def gameOverCheck():
    global gameOver
    checkiftie()
    checkifloss()
    checkifwin()
    if checkiftie == True:
        gameOver = True


#defines playGame
def playGame():
    #states that game is not over
    global gameOver
    gameOver = False
    global availPlays
    #resets availplays
    availPlays = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    #states that there is no tie, loss, or win
    tie = False
    loss = False
    win = False
    
    while gameOver != True:
        
        #displays initial board
        boardDisplay()
        
        #handles player turn
        handleTurn()
        
        #checks if game is over
        gameOverCheck()
        
        #defines computer's move
        compMove()
        
        #checks if game is over
        gameOverCheck()
        
        #breaks loop if game is over
        if gameOver == True:
            break

    print("Game Over.")
    
    if tie == True:
        input("It was a tie.")
    
    elif loss == True:
        input("You lose.")
    
    elif win == True:
        input("You win!")
    
    else:
        input("Your game ended unexpectedly. Please go yell at the programmer.")
    
    playAgain = input("Play again? (Y/N) ").lower
    
    if playAgain == "Y":
        input("Hit ENTER to start!")
        playGame()
    
    elif playAgain == "N":
        input("Thanks for playing! Hit ENTER to exit.")
    
    else:
        input("Invalid input. Hit ENTER to exit game.")

#starts game
playGame()