def slist(ll,sum):

    if sum == 0:
        return ll.append(0)
    else:
        ll.append(sum)
        return slist(ll, sum-1)


ll = []
print slist(ll, 10)
print ll