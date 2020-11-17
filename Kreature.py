#Pet
#Imports Random Module
import random

def Kreature():
    input("This is a pet simulator. Can you take care of your pet for 100 days?\nHit enter to find out. Dramatic music plays. :)")
#Naming of pet
    name = input("\n\nWhat are you naming your pet? ")
#Chance is what determines what happens
    Chance = random.randint(1,4)+random.randint(1,4)

    health = 250
#
    coins = 100
#mental health var
    mental = 10
#number of days the program runs
    x = 1

    while health > 0 or mental > 0 or x < 100:
#Chance is used here
        if Chance == 4:
            print("\n\n\n"+name+" is sick\n(o~o)")
            health = health-1
            answer = input("\nBuy meds? Y/N")
        #Analyzes answer. Glitching right now.
            if answer == "Y":
                health = health + 3
                coins = coins - 10
                input("\n\n(UwU)")

            elif answer == "N":
                health = health - 5
                input(" \n\n/o~o\ " )

            else:
                input("\nInvalid answer. Plz type in only Y or N capitalized.")


        elif Chance == 3:
            print("\n\n\n"+name+" is bored\n(0,0)")
            mental = mental-1
            answer = input("\nBuy toys? Y/N")
            if answer == "Y":
                mental = mental + 2
                coins = coins - 3
                input("\n\n(0w0)")
            if answer == "N":
                health = health-1
                mental = mental-1
                input("\n\nO.O")
            else:
                input("\nInvalid answer. Plz type in only Y or N capitalized.")

        elif Chance == 2:
            print("\n\n\n"+name+" is hungry\n(v~v)")
            mental = mental-1
            answer = input("\nBuy food? Y/N")
            if answer == "Y":
                mental = mental + 5
                coins = coins - 8
                input("\n\n(UwU)")
            if answer == "N":
                health = health-1
                mental = mental-1
                input( " \n\n/x,x\ " )
            else:
                input("\nInvalid answer. Plz type in only Y or N capitalized.")
        
        elif Chance == 6:
            print("\n\n\nIt's pay day!\n ($w$)")
            coins = coins + 20

        elif Chance == 5:
            print("\n\n\n"+name+" wants a new bed\n (/0v0\)")
            
            mental = mental-1
            answer = input("\nBuy new bed? Y/N")
            if answer == "Y":
                mental = mental + 10
                coins = coins - 20
                input("\n\n(VwV)")
            if answer == "N":
                mental = mental-1
                input("\n\n0-0")
            else:
                input("\n\nInvalid answer. Plz type in only Y or N capitalized.")
        else:
            print("\n\n\nAnother boring day! Yay!")
            input("\n\n(v.v)")

        input("\n\nYou have " + str(coins) +" coins. " + "\n\n")
        input(str(name) + " has " + str(health) + " health" )
        input("\n\nAnd "+ str(mental) +" mental health.")
        Chance = 2 * random.randint(1,4)
        x = x +1
        input("\n\nHit enter to acknowledge")
            
    if health == 0 or health < 0:
        print(name + " has died. You lose.")
        input("\n\n(/x~x\)")
        input("Hit enter to exit")

    elif coins == 0 or coins < 0:
        print("You went bankrupt and died. "+name+"starved to death.")
        input("RIP")
        input("Hit enter to exit")

    elif mental == 0 or mental < 0:
        print (name + " ran away. You lose")
        input("\n\n(X v X)")
        input("Hit enter to exit")
    else:
        print("You win!")
        input("\n\n(0w0)")
        input("Hit enter to exit")

Kreature()
