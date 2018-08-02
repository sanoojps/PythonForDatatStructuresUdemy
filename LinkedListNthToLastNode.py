# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 01:25:34 2018

@author: sanooj
"""

"""

Linked List Nth to last Node

in: head node , index n
out: nth to last node in linked list

1->2->3->4

size = 4

n = 1

index = size - n

"""


from SinglyLinkedList import SinglyLinkedList


def nth_to_last_node(
        linked_list:SinglyLinkedList,
        nth_index: int):
    
    size = linked_list.size()
    
    # edge case
    if nth_index > size:
        return None
    
    # + 1 as we need the exact index
    # eg: 
    """
    1->2->3->4

    size = 4

    n = 1

    index = size - n = 4-1 = 3
    
    we need 1st index from bottom.. so 4
    
    hence index = (size - n) + 1
    
    ideally index = size - (n-1)
    
    """
    index = (size - nth_index) + 1 
    
    count = 0
    
    current_node = linked_list.head
    
    while current_node != None:
        
        count += 1
        
        if count == index:
            
            return current_node.get_value()
        
        else:
            
            current_node = \
            current_node.get_next()
            
def test_nth_to_last_node():
    
    a = SinglyLinkedList()
    
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    a.add(5)
    a.add(6)
    
    
    print("test_nth_to_last_node")
    print(nth_to_last_node(a,2)) # 5

test_nth_to_last_node()
        
def nth_to_last_node_2_pointer(
        linked_list:SinglyLinkedList,
        nth_index: int):
    
    left_pointer = linked_list.head
    right_pointer = linked_list.head
    
    for index in range(0,nth_index - 1):
        
        # start moving  right_pointer
        
        # edge case
        # if nth_index > size:
        if right_pointer.get_next() == None:
            return None
        
        right_pointer =\
        right_pointer.get_next()
        
    """
    so far
   
    1->2->3->4

    size = 4

     n = 2  # return 3
   
     range(0,1)
     
     right_pointer = 2
     left_pointer = 1
   
    """
    
    # loop to end
    while right_pointer != None:
        
        left_pointer = \
        left_pointer.get_next()
        
        right_pointer = \
        right_pointer.get_next()
        
    """
     right_pointer = 2
     left_pointer = 1
     
     right_pointer = 3
     left_pointer = 2
     
     right_pointer = 4
     left_pointer = 3
    
     right_pointer = None
     
     return left_pointer = 3   
    
    """
        
    
    return left_pointer.get_value()
            
    
    
    
    
