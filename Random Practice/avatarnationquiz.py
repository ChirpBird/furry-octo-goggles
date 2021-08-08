#starts quiz
input("αναтαя ηαтιση qυιz")
input("Welcome to the αναтαя ηαтιση qυιz. Which nation in ATLA would YOU have been a part of? Hit ENTER to find out!")
#define variables
earth = 0
water = 0
air = 0
fire = 0
UserAns = 0


def AnsAnalysis():
    global earth
    global water
    global air
    global fire
    try:
        if UserAns == 1:
            earth+=1
        elif UserAns == 2:
            water+=1
        elif UserAns == 3:
            air+=1
        elif UserAns == 4:
            fire+=1
        else:
         input("\nInvalid Answer. Question removed from consideration.")   
         print
    except:
        input("\nSomething went wrong... Hit ENTER to continue.")
def finalAnalysis():
    global earth
    global air
    global water
    global fire

    if earth > air and earth > water and earth > fire:
        input("You're part of the EARTH kingdom!")
    elif air > earth and air > water and air > fire:
        input("You're an AIR nomad!")
    elif water > earth and water > air and water > fire:
        input("You're part of the WATER tribes!")
    elif fire > earth and fire > air and fire > water:
        input("You're part of the FIRE nation!")
    else:
        input("Something went wrong. Hit ENTER to try taking the test again. If the problem persists, the programmer says sorry.")
        AvatarQuiz()


def AvatarQuiz():
#declares vars global
    global earth
    global water
    global air
    global fire
    global UserAns
#resets vars
    earth = 0
    water = 0
    air = 0
    fire = 0
    print("\nQuestion One: Which nation would you want to be a part of?")
    UserAns = int(input("\nEarth = 1; Water = 2; Air = 3; Fire = 4; "))
    AnsAnalysis()

    print("\nQuestion Two: Which color(s) do you like best?")
    UserAns = int(input("\nBrown/Beige/Green = 1; White/Blue/Teal = 2; White/Light Blue = 3; Red/Black = 4; "))
    AnsAnalysis()

    print("\nQuestion Three: Which animal is your favorite?")
    UserAns = int(input("\n Lemur = 1; Rhino = 2; Lizard = 3; Seal = 4; "))
    
    print("\nQuestion Four: What would you most like to have a career in?")
    UserAns = int(input("\nEngineering = 1; Medicine = 2; Diplomat = 3; Military = 4; "))
    AnsAnalysis()

    print("\nQuestion Five: Which is your favorite character??")
    UserAns = int(input("\n Aang = 1; Toph = 2; Zuko = 3; Sokka = 4; "))

    print("\nQuestion Six: Which is most closely linked to your hobbies, or what you do to relax?")
    UserAns = int(input("\nPottery, Ceramics, Metal-Working = 1; \nSwimming, Sailing, Dance, Music = 2; \nGlass-Blowing, Making Paper Gliders, Yoga = 3; \nMartial Arts, Running/Jogging, Pyrotechnics = 4; "))
    AnsAnalysis()

    print("\nQuestion Seven: Which ATLA food would you like to eat?")
    UserAns = int(input("\n Jennamite = 1; Sea Prunes = 2; Moon Peaches = 3; Flaming Fire Flakes = 4; "))
    AnsAnalysis()



    finalAnalysis()


AvatarQuiz()

