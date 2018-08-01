# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 00:08:14 2018

@author: sanooj
"""

"""
Singly linked list

head = first noe
tail = last node

"""


class Node(object):
    
    def __init__(self,element):
        self.element = element
        self.next = None
        
    def __expr__(self):
        return self.element
    
    def get_value(self):
        return self.element
    
    def get_next(self):
        return self.next
    
    def set_value(self,value):
        self.element = value
        
    def set_next(self,next_node):
        self.next = next_node
        
    
class SinglyLinkedList(object):
    
    def __init__(self,):
        self.head = None
        self.tail = None
        self.count = 0
        
    def is_empty(self):
        return self.head == None
    
    # add to tail
    def add(self, item):
        
        # make new node
        new_node = Node(item)
        
        # set head
        # set tail
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            
        else:
            
            # add new node to tail
            self.tail.set_next(new_node)
            
            # rest tail
            self.tail = new_node
            
        # update count 
        self.count =\
        self.count + 1
            
    # size with traversal
    # could also use a variable to make this
    # O(1)
    def size(self)-> int:
        
        node = self.head
        
        count = 0
    
        while node != None:
            
            count+=1
            
            node = node.get_next()
        
        return count
    
    
    def search(self, item)-> bool:
        
        node = self.head
        found = False
        
        while node != None and found == False:
            
            if node.get_value() == item:        
                found = True
            else:
                node = node.get_next()
        
        return found
    
    
    def predecessor(self,item):
        
        node = self.head
        found = False
        predecessor_node = None
       
        while node != None and found == False:
            
            if node.get_value() == item:        
                
                found = True
                
            else:
                
                # cache previous node
                predecessor_node = node
                
                node = node.get_next()
         
        return predecessor_node    
        
    
    def remove(self,item):
        
        node = self.head
        found = False
       
        while node != None and found == False:
            
            if node.get_value() == item:        
                
                found = True
                
                # reset nodes
                
                # check if head
                if node.get_value() == \
                self.head.get_value():
                    # head
                    # reset
                    self.head = \
                    self.head.get_next()
                    
                # check for tail
                elif node.get_value() == \
                self.tail.get_value():
                    # tail
                    # reset
                    
                    # predecessor node
                    predecessor_node = \
                    self.predecessor(item)
                    
                    predecessor_node.set_next(None)
                    
                    self.tail = \
                    predecessor_node
                
                else:
                    
                    # rearrange nodes
                    
                    # predecessor node
                    predecessor_node = \
                    self.predecessor(item)
                    
                    # next_node
                    next_node = \
                    node.get_next()
                    
                    # rearrange
                    predecessor_node.set_next(
                            next_node
                            )
                    
                # reset count
                self.count = \
                self.count - 1
                
            else:
                node = node.get_next()
        
        
        
        
def printSinglyLinkedList(linked_list):
    
    node = linked_list.head
    
    while node != None:
        
        print(node.get_value())
        
        node = node.next
    

           
def testSinglyLinkedList():
    
    mylist = SinglyLinkedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    
    printSinglyLinkedList(mylist)
    
    print(mylist.count)
    print(mylist.size())
    
    print(mylist.search(17))
    print(mylist.search(7))
    
    mylist.remove(17)
    
    printSinglyLinkedList(mylist)
    print(mylist.count)
    print(mylist.size())


testSinglyLinkedList()
            