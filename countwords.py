def countWords(string):
    wc = 0
    state = 0
    for i in xrange(len(string)):
        if string[i] == " " or string[i] == "\n":
            state = 0 
        elif state == 0:
            state = 1
            wc = wc + 1
    print wc



countWords("twinke twinkle litter start")