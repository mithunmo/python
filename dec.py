

def pretty(func):
    def wrapper(*args, **kwargs):
        print "i am pretty here"
        func(*args,**kwargs)        
        print "i made it pretty"
    return wrapper

@pretty
def simple(n):
    print "am simple"
    print n

simple(44)