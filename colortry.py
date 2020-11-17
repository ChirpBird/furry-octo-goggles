def colortry():
    try:
        color = input("Gimme a shorthand color. (r, g, b) ")
        if color == "R" or color == "r":
            color = "Red"
        elif color == "G" or color == "g":
            color = "Green"
        elif color == "B" or color == "b":
            color = "Blue"
        else:
            color = "ERROR"
        input("You have chosen " + color)
    except:
        input("Something went wrong. ")
    playagain = input("Play again? (y / n) ")
    if playagain == "y" or playagain == "Y":
        colortry()
    else:
        input("Thanks for playing! Hit ENTER to exit.")
colortry()
