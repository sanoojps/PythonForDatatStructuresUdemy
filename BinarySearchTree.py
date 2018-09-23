# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 03:57:41 2018

@author: sanooj
"""

"""
BINARY SEARCH TREE
--------------------

1. keys smaller that parent on left
2. keys greater than parent on the right 
3. bst property
4. we use MAP interface 


             70    
      31              93                   
  14              73      94 
      23
      
5. inserting [70,31,93,94,14,23,73]
6. 70 is the first key so it is the root
7. 31 is the next key 
    7.1 31 < 70 so 31 goes to left child of 70
8. 93 is the next key 
    8.1 93 > 70 so 93 goes to right child of 70
    
                70    
         31              93   
    
9. 94 is the next key 
    8.1 94 > 70 and 94 > 73 so 94 goes to right child of 93
    
                70    
        31              93   
                               94 
    
9. 14 is the next key 
    9.1 14 < 70 and 14 < 31 so 14 goes to left child of 31
    
            70    
        31       93   
   14                     94 
    
10. 23 is the next key 
    8.1 23 < 70 and 23 < 31 but 23> 14 so 23 goes to right of 14
    
            70    
        31       93   
   14                     94 
        23
        
10. 73 is the next key 
    8.1 73 > 70 but 73 < 93  so 73 goes to left of 93
    
            70    
      31              93                   
  14              73      94 
      23
"""


class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()


