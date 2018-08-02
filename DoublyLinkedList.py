# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 01:14:49 2018

@author: sanooj
"""

"""
Singly linked list

head = first noe
tail = last node

"""

class DoublyLinkedListOperations(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def is_empty(self):
        pass
    
    def add(self, item):
        pass
    
    def size(self)-> int:
        pass
    
    def search(self, item)-> bool:
        pass
            
    def predecessor(self,item):
        pass    
    
    def remove(self,item):
        pass
    
    
class Node(object):
    
    def __init__(self,element):
        self.element = element
        self.next = None
        self.previous = None
        
    def __expr__(self):
        return self.element
    
    def get_value(self):
        return self.element
    
    def get_next(self):
        return self.next
    
    def get_previous(self):
        return self.previous
    
    def set_value(self,value):
        self.element = value
        
    def set_next(self,new_node):
        self.next = new_node
        
    def set_previous(self,new_node):
        self.previous = new_node
        
        
class DoublyLinkedList(DoublyLinkedListOperations):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def is_empty(self):
        return self.head == None
    
    # add to tail
    def add(self, item):
        
        new_node = \
        Node(item)
        
        # first element
        if self.head == None:
            
            self.head = \
            new_node
            
            self.tail = \
            self.head
            
        # list has more elements
        else:
            
            self.tail.set_next(
                    new_node
                    )
            
            # set previous
            new_node.set_previous(
                    self.tail
                    )
            
            # rest tail
            self.tail = \
            new_node
            
        # update count 
        self.count =\
        self.count + 1
        
        pass
    
    def size(self)-> int:
        
        node = self.head
        
        count = 0
    
        while node != None:
            
            count += 1
            
            node = node.next
        
        return count
    
    def search(self, item)-> bool:
        
        node = self.head
        
        found = False
    
        while node != None and found == False:
            
            if node.get_value() == item:
                    
                found = True
            
            else:
                
                node = node.next
        
        return found

            
    def predecessor(self,item):
        
        node = self.head
        
        found = False
    
        while node != None and found == False:
            
            if node.get_value() == item:
                    
                found = True
            
            else:
                
                node = node.next
        
        return node.get_previous()
        
    
    def remove(self,item):
        
        node = self.head
        
        found = False
    
        while node != None and found == False:
            
            if node.get_value() == item:
                    
                found = True
                
                # re-arrange
                
                # head
                if node.get_value() == self.head.get_value():
                    
                    # remove head
                    
                    # get next node
                    next_node = \
                    self.head.get_next()
                    
                    # reset previous
                    # as previous would be "head"
                    next_node.set_previous(
                            None
                            )
                    # reset head
                    self.head = \
                    next_node
                    
                # tail
                elif node.get_value() == self.tail.get_value():        
    
                    
                    predecessor_node = \
                    self.tail.get_previous()
                    
                    # reset next
                    predecessor_node.set_next(
                            None
                            )
                    
                    # reset tail
                    self.tail = \
                    predecessor_node
                    
                else:
                    
                    # get predecessor
                    predecessor_node = \
                    node.get_previous()
                    
                    # get next
                    next_node = \
                    node.get_next()
                    
                    # reset
                    # node->previos->next = node->next
                    # node->next->previous = node->previous
                    predecessor_node.set_next(
                            next_node
                            )
                    
                    next_node.set_previous(
                            predecessor_node
                            )
                    
                # update count
                self.count =\
                self.count - 1
            
            else:
                
                node = node.next
        
        
    
def printDoublyLinkedListForward(linked_list):
    
    node = linked_list.head
    
    while node != None:
        
        print(node.get_value())
        
        node = node.next
        
def printDoublyLinkedListBackwards(linked_list):
    
    node = linked_list.tail
    
    while node != None:
        
        print(node.get_value())
        
        node = node.get_previous()
    

           
def testSinglyLinkedList():
    
    mylist = DoublyLinkedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    
    print("printDoublyLinkedListForward")
    printDoublyLinkedListForward(mylist)
    
    print("printDoublyLinkedListBackwards")
    printDoublyLinkedListBackwards(mylist)
    
    print(mylist.count)
    print(mylist.size())
    
    print(mylist.search(17))
    print(mylist.search(7))
    
    mylist.remove(17)
    
    print("printDoublyLinkedListForward")
    printDoublyLinkedListForward(mylist)
    
    print("printDoublyLinkedListBackwards")
    printDoublyLinkedListBackwards(mylist)
    
    print(mylist.count)
    print(mylist.size())


testSinglyLinkedList()