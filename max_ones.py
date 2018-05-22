
max_one = [
          [0,0,1,1],
          [0,0,0,0],
          [0,0,0,1] 
          ]

def findIndex(arr):
    min = 0
    max = len(arr) - 1
    while(min <= max):
        mid = ( min + max ) // 2
        if arr[mid] == 1 and arr[mid-1] == 0:
            return mid
        if arr[mid] == 1:
            max = mid - 1
        else:
            min = mid + 1
    else:
        return -1

for i in max_one:
    print(i)
    print(findIndex(i))