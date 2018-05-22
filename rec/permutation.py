

def perm(A):
    if len(A) == 0:
        return ""

    if len(A) == 1:
        return [A]

    list = []
    for i in range(0, len(A)):
        rem = A[:i] + A[i+1:]
        for p in perm(rem):
            list.append(A[i]+p)
    return list


print(perm("abc"))
