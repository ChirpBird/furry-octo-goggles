x = False
def gradeCalc():
  try:
    x = int(round(float(input("Give a percentage. Omit the percentage sign. "))))
    if 95 <=x<100:
      print("A")
    elif 92 <=x<95:
      print("A-")
    elif 88 <= x < 92:
      print("B+")
    elif 85 <= x < 88:
      print("B")
    elif 82 <= x < 85:
      print("B-")
    elif 79 <= x < 82:
      print("C+")
    elif 76 <= x < 79:
      print("C")
    elif 73 <= x < 76:
      print("C-")
    elif 70 <= x < 73:
      print("D+")
    elif 67 <= x < 73:
      print("D")
    elif 64 <= x < 67:
      print("D-")
    else:
      print("F")
  except:
      input("Smth went wrong!")
  finally:
    x = bool(input("To quit, enter smth."))
while x!= True:
  gradeCalc()
  
