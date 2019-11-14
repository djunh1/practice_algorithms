from platform import node
class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.next = None
        
        
class SingleLinkedList(object):
    
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
        
def cycle_check(node):
    
    m1 = node
    m2 = node
    
    while m2 != None and m2.next != None:
        m1 = m1.next
        m2 = m2.next.next
        
        if m2 == m1:
            return True
        
    return False
        
  
def reverse(a):
       
    previous = None
    current = a 
    next = None
    
    while (current != None):
        next = current.next #b, c , d , None
        current.next = previous #None, a, b
        
        previous = current #a, b, c
        current = next #b, c , d
    return previous
       
def returns_nth_toLast_node(targetNumber, head):
    num = get_count(head)-targetNumber
    
    #edge case
    if head.next == None:
        raise LookupError('Error')
    
    for i in range(num):
        head = head.next
        
        
    return head
    
    
def get_count(node):
    count = 0
    
    while(node):
        count +=1
        node = node.next
        
    return count

def nth_to_last_node2(n, head):

    left_pointer  = head
    right_pointer = head

    for i in range(n-1):
        if not right_pointer.next:
            raise LookupError('Error: n is larger than the linked list.')
        right_pointer = right_pointer.next

    while right_pointer.nextnode:
        left_pointer  = left_pointer.next
        right_pointer = right_pointer.next

    return left_pointer
    
    
if __name__ == '__main__': 
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node (5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    
    #reverse(a)
    #print(d.next.value)
    #print(c.next.value)
    #print(b.next.value)
    
    print(returns_nth_toLast_node(2,a))
    
    