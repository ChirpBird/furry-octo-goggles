def countfactors(x):
  try:
    y = 1
    z = 0
    while y <= x:
      if x%y == 0:
        z+=1
      y+=1
    return(z)
  except:
    input("Oops! Something went wrong.")

def printfacotrcount():
  try:
    inp = int(input("Gimme a positive int! "))    
    facotr = countfactors(inp)
    print("Your integer has " + str(facotr) + " factors")
    playagain = input("Try again? (y/n) ")
    if playagain == "y" or playagain == "Y":
      printfacotrcount()
    else:
      input("Thanks for playing! Hit ENTER to exit.")
  except:
    input("Oops! Something went wrong.")
printfacotrcount()

