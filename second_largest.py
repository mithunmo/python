

a = [10,2,45,1,-10, 100000,22,999]

m1 = m2 = float("-inf")
print(m1)
for i in a:
    if i > m2:
        if i > m1:
            m2 = m1
            m1 = i
        else:
            m2 = i

print(m1)
print(m2)

print(len("87eee136f73cd0a771068277f170bd4ad82d929fd17507e3939a5182186d40c1"))