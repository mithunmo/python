def firstMissingPositive(A):
    count = 0
    lst = []
    for i in range(0,len(A)):
        if A[i] > 0:
            count += 1
    if count == 0:
        return 1
    else:
        #max1 = max(A)
        lst = [0] * (len(A)+ 1)
        print(lst)
        for i in range(0,len(A)):
            if A[i] > 0 and A[i] < len(A):
                lst[A[i]] = 1
        print(lst)

        for i in range(1,len(lst)):
            if lst[i] == 0:
                return i
print(firstMissingPositive([3,4,-1,1,8]))