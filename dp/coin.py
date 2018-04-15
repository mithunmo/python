def coin(arr, amount):
    if amount <= 0:
        return 0
    else:
        minval = 1000
        for i in arr:
            print i
            if i <= amount: 
                minval = min(minval, 1 + coin(arr, amount - i))
        return minval


vl = coin([9,6,5,1], 9)
print vl