import math
a = int(input("What's a? "))
b = int(input("What be b? "))
c = int(input("What c? "))
def quadfunc(a,b,c):
  d = math.sqrt((b**2 + 4*a*c))
  ans1 = ((-b+d)/2*a)
  ans2 = ((-b-d)/2*a)
  return("First answer: "+str(ans1)+"\nSecond answer: "+str(ans2))
input(quadfunc(a,b,c))
