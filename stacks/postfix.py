

exp = "4 5 6 * +"
stack = []
for x in exp.split(" "):
    if x in ["+","*"]:
        a = stack.pop()
        b = stack.pop()
        total = eval(a+x+b)
        stack.append(str(total))
    else:
        stack.append(x)

print(stack)