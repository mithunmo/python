

def get_rem(arr, element):
    return [i for i in arr if i != element]

def subset(arr, sum):
    if sum <= 0:
        return []
    if sum in arr:
        return [sum]
    for i in arr:
        elem = []
        if i < sum:
            elem.append(i)
            resum = subset(get_rem(arr,i), sum - i)
            if resum:
                elem = elem + resum
                break
    else:
        return []
    return elem

arr = [3, 34, 4, 12, 5, 2]
sum = 9
print subset(arr, 100)

