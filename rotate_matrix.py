
def rotate(A):
    B = [[0 for j in range(len(i))] for i in A]
    i = 0
    j = len(A) - 1
    for a in A:
        for b in a:
            B[i][j] = b
            i = i + 1
        i = 0
        j = j - 1
        
        

    print(B)
A = [
    [1, 2, 4],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(A)
