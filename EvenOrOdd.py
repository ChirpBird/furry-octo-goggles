def evenorodd():
    try:
        x = int(input("Gimme an int. "))
        if x % 2 == 0:
            print(str(x)+" is Even")
        else:
            print(str(x)+" is Odd")
        playagain = input("Play again? (y/n) ")
        if playagain == "y":
            evenorodd()
        else:
            input("Thanks for playing! Hit ENTER to exit.")
    except:
        input("Whoops! Something went wrong. Hit ENTER to exit.")
evenorodd()
