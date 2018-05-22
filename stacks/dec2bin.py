
n = 7
bin = []
while n >0:
    rem = n % 2
    bin.insert(0,rem)
    n = n // 2

print("".join(str(x) for x in bin))


