def trigonidentify(a,b,c):
  if a + b < c or b + c < a or c + a < b:
    return("Illegal")
  elif a == b == c:
    return("Equilateral")
  elif a == b or b == c or c == a:
    return("Isoscelese")
  else:
    return("Scalene")
gameOver = False
while gameOver != True:
  a = int(input("\nGive me your first side length. "))
  b = int(input("\nGimme your 2nd side length. "))
  c = int(input("\nGimme ur 3rd side len "))
  print()
  input(trigonidentify(a,b,c))
  gameOver = bool(input("\nType smth to quit. "))
