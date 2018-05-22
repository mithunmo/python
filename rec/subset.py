

def subset(coins, target):
    ''' returns a list of lists of alternate solutions '''

    if target in coins:
        return [[target]]  # only one possibility, base case

    possibilities = []

    for i in range(len(coins)):
        if coins[i] < target:
            """ unpacking using * """
            rem = coins[:i] + coins[i+1:]
            possibilities += possibilities + [[coins[i], *possibility] for possibility in subset(rem, target - coins[i])]
    return possibilities

print(subset([3, 34, 4, 12, 5, 2], 14))


def subset_sum(seq, target):
    if target == 0:
        return True

    for i in range(len(seq)):
        if subset_sum(seq[:i] + seq[i+1:], target - seq[i]):
            return True
    return False

print(subset_sum([3, 34, 4, 12, 5, 2], 6))


# def subset(arr, sum):
#     if sum in arr:
#         return [sum]
    
#     ll = []
#     for i in range(len(arr)):
#         rem = arr[:i] + arr[i+1:]
#         if sum - arr[i] >= 0:
#             ll = ll + [arr[i]] + subset(rem, sum - arr[i])
#     return ll


# #print(subset([3, 34, 4, 12, 5, 2], 9))