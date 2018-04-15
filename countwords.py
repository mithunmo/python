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

def reverse(str):
    return str[::-1]


countWords("twinke twinkle litter start ")

word = "mithun is the best"
words = word.split(" ")
word =  [word[::-1]for word in words]
word = " ".join(word)
print word