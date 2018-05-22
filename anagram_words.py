

from collections import defaultdict

with open("words.txt", "r") as words:
    hash_map = defaultdict(list)
    for word in words:
        word = word.lower().strip("").strip("\n")
        wlist = list(word)
        wlist.sort()
        val = "".join(wlist)
        hash_map[val].append(word)
    
    for i,v in hash_map.items():
        print(v)