def cardtry():
  try:
    #asks for shorthand card
    card = input("Gimme a shorthand description for a card. ")

    #takes the first character of the shorthand description as the rank
    rank = card[0]

    #takes the second character of the shorthand description as the suit
    suit = card[1]
    
    #analyzes rank/number of the card
    if rank == "k" or rank == "K":
      rank = "King"
    elif rank == "q" or rank == "Q":
      rank == "Queen"
    elif rank == "j" or rank == "J":
      rank = "Jack"
    elif rank == "a" or rank == "A":
      rank = "Ace"
    else:
      rank = str(rank)
    
    #analyzes suit of the card
    if suit == "c" or suit == "C":
      suit = " of Clubs."
    
    elif suit == "d" or suit == "D":
      suit = " of Diamonds."
    
    elif suit == "h" or suit == "H":
      suit  = " of Hearts."
    
    else:
      suit = " of Spades." 
    
    #prints the long description of the card
    input("Your card was the " + rank + suit)

#catches exceptions
  except:
    input("Oops! Something went wrong. Hit ENTER to exit.")

#asks if user wants to play again  
  playagain = input("Play again? (y/n) ")
  
  if playagain == "y" or playagain == "Y":
    cardtry
  
  else:
    input("Thanks for playing! Hit ENTER to exit.")

#runs program
cardtry()
