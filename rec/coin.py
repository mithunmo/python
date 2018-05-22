import sys
def coin_change(coins, target):
    ''' returns a list of lists of alternate solutions '''

    if target in coins:
        return [[target]]  # only one possibility, base case

    possibilities = []

    for coin in coins:
        if coin < target:
            """ unpacking using * """
            possibilities += possibilities + [[coin, *possibility] for possibility in coin_change(coins, target - coin)]
    return possibilities

def coin_change1(A, target):
    if target in A:
        return [target]
    ll = []
    for i in A:
        if i < target:
            ll = ll + [i] + coin_change(A, target - i) 
        else:
            ll = ll +  [-1]
    return ll

coins = [1,3,5,10,25]
target = 21
print(coin_change(coins, target))



def minCoins(coins, m, V):
 
    # base case
    if (V == 0):
        return 0
 
    # Initialize result
    res = sys.maxsize
     
    # Try every coin that has smaller value than V
    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V-coins[i])
 
            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
 
    return res
