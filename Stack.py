# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 01:30:23 2018

@author: sanooj
"""

"""
STACK

1. ordered collection
2. add and remove happens at same end
3. that end is "top"
4. oppposite end is "base"
6. LIFO
7. ordering based on length of time in collection
8. newer on top 
9. older at base
10. used for reversal

"""

class Stack(object):
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    # added to bottom 
    def push(self, item):
        self.items.append(item)
        
    # pop from top
    # pop index = len(self.items) - 1 
    def pop(self):
        return self.items.pop()
        
    # return top    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)


s = Stack()

print(s.is_empty())

s.push("one")    
s.push("two")

print(s.items)

print(s.peek())

print(s.size())

print(s.is_empty())  

print(s.pop())

print(s.size())   
print(s.peek())   