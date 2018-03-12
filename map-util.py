

x = [1,2,3,4,5]

def two(x):
    print "here"
    return x*2

print map(two, x)


class PureMap:
    def __init__(self, function, sequence):
        self._f = function
        self._sequence = sequence
        self.i = 0
        self.n = len(sequence)

    def __iter__(self):
        return map(self._f, self._sequence)

    def __getitem__(self, i):
        return self._f(self._sequence[i])
        
    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return self._f(self._sequence[self.i])

        else:
            raise StopIteration()



m = PureMap(two, x)
print m.next()
print m.next()
print m.next()



