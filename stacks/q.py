

class queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.insert(0 , item)
    
    def pop(self):
        self.items.pop()