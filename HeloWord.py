# \n means new line
#input lets you input things when the file is running
#Fibonacci Sequence

def program ():
        x = int(input("\n\nEnter a number"))
        a = 0
        b = 1
        z = a+b
        while b < x:
            z = a + b
            a = b
            b = z
            print(z)

program ()
input("Hit the self destruct button to end. Hit enter")
