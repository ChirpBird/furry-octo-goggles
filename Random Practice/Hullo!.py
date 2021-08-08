aanswer = None

def died():

    answer = input("\nYou died... Play again?")

while answer != "n":
    choice = input("\nYou are walking on a trail. \n\nSuddenly, you hear an ominous chirping noise. \n\nA racoon jumps out of a bush and steals your map. \n\nDo you, a, run after the racoon (you need a map!), or, \n\nb, continue onwards without a map. (I have a pretty good memory. It'll be an adventure!)")
    if choice == "":

        continue

    elif choice == "a":

        input("\nYou run after the racoon, oblivious to your surroundings. \n\nWhen you finally catch up to the racoon and get your map back, \n\nit is already sundown.")
        choice = input("\nDo you, a, try and get back to the trail, or, \n\nb, set up camp here?")

        if choice == "a":

            input("\nYou try to get back to the trail, but unfortunately, are eaten by a bear.")

            died()

        elif choice == "b":

            input("You set up camp where you are, only to find that your supplies fell out of your pack while chasing the racoon. A bear eats you in your sleep.")

            died()
    
    elif choice == "b":

        input("\nYou walk forward. Onwards!")
        input("\nYou reach a fork in the road. You ask the wise old man sitting at the fork where they go, and he says: \n One leads to death, and one leads to paradise."
)       choice = input("Will you go left, a, or right, b?")
 
