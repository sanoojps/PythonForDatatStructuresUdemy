# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 03:22:16 2018

@author: sanooj
"""

"""
Queue

1. ordered collection
2. add and remove happens at different end
3. add end is "rear"
4. retrieve end is "front"
6. FIFO
7. ordering based on length of time in collection
8. older on top 
9. newer at base


"""

class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    # added to rear 
    def enqueue(self, item):
        self.items.append(item)
        
    # dequeue from front
    # pop index = 0
    def dequeue(self):
        return self.items.pop(0)
        
    # return top    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
s = Queue()

print(s.is_empty())

s.enqueue("one")    
s.enqueue("two")

print(s.items)

print(s.peek())

print(s.size())

print(s.is_empty())  

print(s.dequeue())

print(s.size())   
print(s.peek())