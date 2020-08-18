x = (range(int(input("Gimme NUM!! "))))
listo = []
for a in x:
  listo.append(a+1)
x = int(len(listo))
y = 1
while y <= x:
    z = 1
    print()
    while z <= y:
      print(z, end =" ")
      z+=1
    y+=1
y = x
while y<=x:
  z = 1
  print()
  while z >=y:
    print(z, end = " ")
    z+=1
  y-=1

