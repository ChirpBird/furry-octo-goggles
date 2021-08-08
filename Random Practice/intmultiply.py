n = range(int(input("How many items? ")))
c = 1
listo = []
for x in n: listo.append(int(input("Gimme a num. ")))
for x in listo: c *= x
print(c)
