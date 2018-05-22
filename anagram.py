
def anagram_solution(s1 , s2):
    slist1 = list(s1.lower())
    slist2 = list(s2.lower())

    slist1.sort()
    slist2.sort()

    print(slist1)
    print(slist2)
    
    found = 0
    for s in slist1:
        if s in slist2:
            continue
        else:
            print(s)
            found =1
            break
    if found == 0:
        print("anagrams")
    else:
        print("not anagrams")


anagram_solution("Georgebush", "hebugsGore")

     