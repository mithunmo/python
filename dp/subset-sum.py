def find_subset(weight , req_sum):
    l = len(weight)

    # ROWS : array
    # COL : range(sum)
    row = l
    col = req_sum + 1

    # 2d array storing Sum
    dp_array = [[0] * col for i in range(row)]




    for i in range(row):
        for j in range(1, col):
            # Row 0
            if i == 0:
                if j >= weight[i]:
                    dp_array[i][j] = weight[i]
                else:
                    continue
            else:
                if j - weight[i] >= 0:
                    dp_array[i][j] = max(dp_array[i - 1][j], (weight[i] + dp_array[i - 1][j - weight[i]]))
                elif j >= weight[i]:
                    # take from row above it
                    dp_array[i][j] = max(dp_array[i - 1][j], weight[i])
                else:
                    dp_array[i][j] = dp_array[i - 1][j]
    print dp_array
    # Find out which Numbers should be in the subset
    # give from index 0
    row -= 1
    col -= 1
    sum_subset = []

    # check if the Subset is possible : if not, return None
    if dp_array[row][col] != req_sum:
        return None

    # get the subset
    while col >= 0 and row >= 0 and req_sum > 0:
        # First Row
        if (row == 0):
            sum_subset.append(weight[row])
            break

        # Bottom-Right most ele
        if (dp_array[row][col] != dp_array[row - 1][col]):
            # print(req_sum,' : ',dp_array[row][col],dp_array[row-1][col],' : ',weight[row])
            sum_subset.append(weight[row])
            req_sum -= weight[row]
            col -= weight[row]
            row -= 1
        else:
            row -= 1

    return sum_subset

# main
if __name__ == "__main__":
    array = list(map(int, input().split()))
    req_sum = int(input())

    # Sort by ascending order
    array.sort()
    sum_subset = find_subset(array, req_sum)

    # If Sum is not possible
    if sum_subset is None:
        print("Sum :", req_sum, "is not possible")
    else:
        print("Subset for sum", req_sum, ' :')
        print(' '.join(str(x) for x in sum_subset))
