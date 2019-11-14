class Stack(object):
    def __init__(self):
        self.items = []
        
    def empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    
class Que(object):
    def __init__(self):
        self.items = []
        
    def empty(self):
        return self.items == []
    
    def enque(self,item):
        self.items.insert(0, item)
        
    def deque(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
class deQue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    

    
    