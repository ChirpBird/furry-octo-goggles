
def TypoSaur():
    x = input("\nType smth. Hit ENTER when done. ")

    input("\nYou typed: "+ x+" ")

    input("\nWas that correct? ")

    input("\nHuzzah! Program was a success! ")

    n = input("\nPlay again? ")

    if n == "y" or n == "Y" or n == "yes" or n == "Yes":
        TypoSaur()
    else:
        input("\nThank you for playing! Hit ENTER to quit. ")

TypoSaur()
