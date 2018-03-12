class Singleton(object):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print "here"
            cls._instance =  object.__new__(cls)
        return cls._instance


obj = Singleton()
obj1 = Singleton()
obj2 = Singleton()
obj3 = Singleton()
obj4 = Singleton()
