def find_subset(weight , req_sum):
    l = len(weight)

    # ROWS : array
    # COL : range(sum)
    row = l
    col = req_sum + 1

    # 2d array storing Sum
    dp_array = [[False] * col for i in range(row)]

    for i in range(row):
        dp_array[i][0] = True

    print dp_array

    #col = 0,1,2,3,4,5
    #row = 2,3,7,8,10

    for i in range(row):
        for j in range(1,col):
            #if j - weight[i] >= 0:
            dp_array[i][j] = dp_array[i - 1][j] or dp_array[i - 1][j - weight[i]]
            #else:
            #dp_array[i][j] = dp_array[i-1][j]

    print dp_array

array = [2,3,7,8,10]
req_sum = 13

array.sort()
sum_subset = find_subset(array, req_sum)

