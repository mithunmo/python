

print [1 if x%2 == 0 else 9 for x in xrange(10)]


print [1 for x in xrange(10) if x % 2 ==0 ]

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print reduce(lambda x, y: x + y , foo)