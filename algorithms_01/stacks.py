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


def balance_check(s):
    

    if len(s)%2 != 0:
        return False
    

    opening = set('([{') 
    matches = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    
    stack = []
    
    for paren in s:
        
        if paren in opening:
            stack.append(paren)
        
        else:
        
            if len(stack) == 0:
                return False
            
            last_open = stack.pop()
            
            if (last_open,paren) not in matches:
                return False
            
    return len(stack) == 0


class Queue2Stacks(object):
    
    def __init__(self):
        self.instack = []
        self.outstack = []
     
    def enqueue(self,element):
        self.instack.append(element)
      
    
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
        pass
        

if __name__ == '__main__': 
    
    
    q = Queue2Stacks()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    
    print(q.dequeue())
    
    
    