def coin(arr, amount):
    if amount <= 0:
        return 0
    else:
        minval = 1000
        for i in arr:
            if i <= amount: 
                minval = min(minval, 1 + coin(arr, amount - i))
        return minval


vl = coin([9,6,5,1], 11)
print vl