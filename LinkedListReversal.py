# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 15:03:59 2018

@author: sanooj
"""

"""

LinkedListReversal

when next points to previous node

"""
from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import printSinglyLinkedList

a = SinglyLinkedList()
    
a.add(1)
a.add(2)
a.add(3)
a.add(4)

    
def reverse_list(linked_list:SinglyLinkedList):
    
    current_node = linked_list.head
    
    previous_node = None
    
    next_node = None
    
    while current_node != None:
        
        # logic
        # 1. current nodes next node's next will be  
        #    current node
        #
        #
        #
        #
        
        # get current node's next
        next_node = current_node.get_next()
        
        # next node's next is previous node
        current_node.set_next(
                previous_node
                )
        
        # previous node
        previous_node = current_node
        
        # loop increment
        current_node = next_node
        
        # reset list
        linked_list.head = \
        previous_node
        
    return linked_list
   
    

print("reverse_list")
printSinglyLinkedList(reverse_list(a))
    