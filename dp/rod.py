import sys
"""
def cutRod(price, n):
    if(n <= 0):
        return 0
    max_val = -sys.maxsize-1
     
    # Recursively cut the rod in different pieces  
    # and compare different configurations
    for i in range(1, n):
        max_val = max(max_val, price[i] +
                      cutRod(price, n-i-1 ))
    return max_val
"""
INT_MIN = -32767

def cutRod(price, n):
    val = [0 for x in range(n+1)]
    print val
    #val[0] = 0
    #print val
    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
 
    return val[n]
  
# Driver code
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is", cutRod(arr,5))