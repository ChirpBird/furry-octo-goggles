import random

def YosoGemu():
    x = random.randint(0,100)
    input("\n\nThis is a guess the number game. The computer will generate a number between 0 and 100. You will guess the number. If your answer is incorrect, the computer will tell you if your answer needs to be higher or lower.")
    Suisoku = 200
    mawaru = 0
    while Suisoku != x:
        Suisoku = int(input("\nWhat is your guess? "))
        mawaru = mawaru+1
        if Suisoku < x:
            print("\nHigher. ")
        elif Suisoku > x:
            print("\nLower. ")
    futabi = input("\nGood job! You did it in " + str(mawaru)+ " turns! Play again? ")
    if futabi == "Yes" or futabi == "yes" or futabi == "Y" or futabi == "y":
        YosoGemu()
    else:
        input("\nThank you for playing! Hit ENTER to exit. ")   
YosoGemu()
