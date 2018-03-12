

def cutRod(price, n):
    val = [0 for x in range(n+1)]
    print val
    #val[0] = 0
    #print val
    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n+1):
        q = -1
        for j in range(i):
            print i,j
            max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
 
    return val[n]

arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is", cutRod(arr,5))