def solve(A):
    A.sort()
    len_val = len(A)
    for i in range(len_val - 1 ):
        print(i)
        if A[i] == (len_val - i -1 ):
            return 1
    else:
        return -1

print(solve([ -4, -2, 0, -1, -6 ]))