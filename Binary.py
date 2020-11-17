highNum = int(input("How high are we going?")) + 1
BaseTenNums = list(range(1,highNum))
BinaryNums = list()
x = 0
lengthBaseTen = len(BaseTenNums)
while lengthBaseTen - x > 0:
    BinaryNums.insert(x,bin(BaseTenNums[x])[2:])
    print(BinaryNums[x])
    x = x + 1