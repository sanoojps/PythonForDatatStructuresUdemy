# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 06:58:58 2018

@author: sanooj
"""

"""

Cycle check

when next points to previous node

"""


from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import printSinglyLinkedList

def cycle_check(linked_list:SinglyLinkedList):
   
    node = \
    linked_list.head
    
     # get successor
    successor_one_node = node
    
    # get successor
    # two nodes behind
    successor_two_nodes = node
    
    # begin loop
    # with both markers at same node
    while successor_one_node != None \
    and successor_two_nodes.get_next() != None :
        
        # marker 1 -> next node
        successor_one_node = \
        successor_one_node.get_next()
        
        #marker 2 -> two nodes ahead of current node
        successor_two_nodes = \
        successor_two_nodes.get_next().get_next()
        
        print("successor_two_nodes")
        print(successor_two_nodes.get_value())
        print("successor_one_node")
        print(successor_one_node.get_value())
        
        # check if they are equal
        if successor_two_nodes.get_value() == \
        successor_one_node.get_value() :
            
            return True

    return False
        
                        
   
def test_cycle():
    
    a = SinglyLinkedList()
    
    a.add(1)
    a.add(2)
    a.add(3)
    
    predecessor = \
    a.predecessor(2) #2
    
    # set 3's next as 2
    a.tail.set_next(
            predecessor
            )
    
    
    #printSinglyLinkedList(a)
    
    print("test_cycle")
    print(cycle_check(a))

test_cycle()