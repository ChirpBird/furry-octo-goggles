secondhalf = ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
x = str(input("Gimme STR!! ").upper())
z = 0
for a in x:
  if a in secondhalf:
    z+=1
print(z)
