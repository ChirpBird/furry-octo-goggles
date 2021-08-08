x = int(input("Gimme NUM!! "))
y = 1
while y <= x:
  z = 1
  print()
  while z <= y:
    print(z, end = " ")
    z+=1
  y+=1

y = x
while y >= 0:
  print()
  z = 1
  while z <= y:
    print(z, end = " ")
    z+=1
  y-=1