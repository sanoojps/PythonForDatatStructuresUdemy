# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:32:57 2018

@author: sanooj
"""

from Stack import Stack

"""
Implemnet a Queue FIFO structure

"""

class Queue2Stacks(object):
    
    # stacks
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def enqueue(self, element):
        
        # clear stack2
        #self.stack2.items.clear()
        
        # copy to stack 2
        # order reversed
        size_stack1 = \
        self.stack1.size()
        
        for member in range(0,size_stack1):
            
            peeked = \
            self.stack1.pop()
            
            self.stack2.push(peeked)
        
        # insert to stack 2
        # gets added to last index
        self.stack2.push(element)
        
        print("enqueue")
        print(self.stack1.items)
        print(self.stack2.items)
        
            
    def dequeue(self):
        
        
        # clear stack 1
        # self.stack1.items.clear()
        
        size_stack2 = \
        self.stack2.size()
        
        # copy stack 2 to stack 1
        for member in range(0,size_stack2):
            
            peeked = \
            self.stack2.pop()
            
            self.stack1.push(peeked)
            
    
        # pop from stack 2
        # pops last index
        popped = \
        self.stack1.pop()
        
        print("dequeue")
        print(self.stack1.items)
        print(self.stack2.items)
        
        return popped
    

s = Queue2Stacks()

#print(s.is_empty())

s.enqueue("one")    
s.enqueue("two")
s.enqueue("three")

#print(s.items)

#print(s.peek())

#print(s.size())

#print(s.is_empty())  

print(s.dequeue()) # "one"
s.enqueue("four")
print(s.dequeue()) # "two"
print(s.dequeue()) # "three"
s.enqueue("five")
print(s.dequeue()) # "four"



#print(s.size())   
#print(s.peek())


def q():
  
    print("Q()")
    
    from Queue import Queue
    
    s = Queue()

    #print(s.is_empty())
    
    s.enqueue("one")    
    s.enqueue("two")
    s.enqueue("three")
    
    print(s.items)
    
    #print(s.peek())
    
    #print(s.size())
    
    #print(s.is_empty())  
    
    print(s.dequeue()) # "one"
    print(s.items)
    
    s.enqueue("four")
    print(s.items)
    
    print(s.dequeue()) # "two"
    print(s.items)
    print(s.dequeue()) # "three"
    print(s.items)
   
    s.enqueue("five")
    print(s.items)
    
    print(s.dequeue()) # "four"
    print(s.items)
    
q()


def test_Q2S():
    
    q = Queue2Stacks()
    
    for i in range(5):
        q.enqueue(i)
        
    for i in range(5):
        print(q.dequeue())


test_Q2S()        
    


class Queue2StacksP(Queue2Stacks):
        
    def __init__(self):
        
        self.instack = []
        self.outstack = []
        
        
    # @override
    def enqueue(self,element):
        
        self.instack.append(element)
    
    # @override
    def dequeue(self):
        
        if not self.outstack:
            
            while self.instack:
                
                self.outstack.append(
                        self.instack.pop()
                        )
                
        return self.outstack.pop()
    
def test_Q2SP():
    
    q = Queue2StacksP()
    
    for i in range(5):
        q.enqueue(i)
        
    for i in range(5):
        print(q.dequeue())


test_Q2SP()     