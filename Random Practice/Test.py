f = open("test.txt")
input("file opened.")
lineNum = 0

ans = input("Would you like to know how many lines there are?")
if ans == "y":
    for x in f:
        lineNum=lineNum+1
    print("There are " + str(lineNum) + " lines in the file. ")
else:
    f.close
