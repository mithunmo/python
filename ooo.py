class A(object):

    def __init__(self,a,b):
        self.a = a 
        self.b = b 

    def get_val(self):
        print self.a,self.b
class B(A):

    def __init__(self,a,b):
        super(B,self).__init__(a,b)

    def get_val(self):
        print self.a


class C(B):
    def __init__(self,a,b):
        super(C,self).__init__(a,b)



b = B(10,20)
b.get_val()

c = C(33,33)
c.get_val()

