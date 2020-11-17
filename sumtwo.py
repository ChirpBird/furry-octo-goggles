def sumtwo(x):
    y = 0
    while y < x:
      x+=y
      y+=1
    input(x)
sumtwo(int(input("Gimme an int! ")))
print("Fin")