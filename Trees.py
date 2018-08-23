# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:35:23 2018

@author: sanooj
"""

"""

root

leaves

node
--- key
--- payload

edge
-----

# connects two nodes

path
-----

# ordered list of nodes that are connected by edges


children
---------

set of nodes "c" -> that have incoming edges from the same node
 

parent
---------

a node is the parent of all the nodes it
connects to with outgoing edges

Sibling
-------

children of the same parent are said to be siblings

Subtree
-------

set of nodes and edges comprised of a parent
and all the descendants of that parent

Leaf node
---------

node with no children

Level
-----

n ->

number of edges on the path from the root node to "n"


Height
-------

maximum level of any node in the tree


"""



"Tree with lists"

"""
Binary Tree
"""
"""
                a
               -  -
               |  |
               b  c  
             --   --
             | |  |
             d e  f 



my_tree = 
[
["a",
[  ["b", [  "d" , [],[] ],[ "e" , [], [] ]  ]  ],
[  "c", [ ["f" , [] , [] ]  ], []   ]
]
]



"""

class BinaryTreeWithList(object):
    
    def __init__(self,payload):
        self._root = self.make_binary_tree(payload)
       
    @property
    def root(self):
        return self._root
    
    @root.getter
    def root(self):
        return self._root
    
    @root.setter
    def root(self,value):
        self._root = value
    
    
    def make_binary_tree(self,payload):
         return [payload, [], []]
     
    def insert_left(self,root: list,new_branch_payload):
        
        # get left branch
        # left_branch at index 1
        # right_branch at index 2
        left_branch = \
        root.pop(1)
        
        new_branch = \
        self.make_binary_tree(new_branch_payload)
        
        new_branch[1] = \
        left_branch
        
        root.insert(1,new_branch)
        
        return new_branch
        
    def insert_right(self,root: list,new_branch_payload):
        
        # get right branch
        # left_branch at index 1
        # right_branch at index 2
        right_branch = \
        root.pop(2)
        
        new_branch = \
        self.make_binary_tree(new_branch_payload)
        
        new_branch[2] = \
        right_branch
        
        root.insert(2,new_branch)
        
        return new_branch
        
    def get_root_val(self):
        return self.root[0]
    
    def set_root_val(self,payload:object):
        self.root[0] = payload
        
    def get_left_child(self,branch:list):
        return branch[1]
    
    def get_right_child(self,branch:list):
        return branch[2]
    
def testBinaryTreeWithList():
    """  
    Binary Tree


                a
               -  -
               |  |
               b  c  
             --   --
             | |  |
             d e  f 
    """
    
    binaryTree = BinaryTreeWithList("a")
    print(binaryTree.root) 
    #['a', [], []]
    
    new_branch = \
    binaryTree.insert_left(binaryTree.root,"b")
    print(binaryTree.root) 
    
#    binaryTree.insert_left(new_branch,"d")
#    print(binaryTree.root) 
    
    new_branch = \
    binaryTree.insert_right(binaryTree.root,"c")
    print(binaryTree.root) 
    
    binaryTree.insert_left(new_branch,"f")
    print(binaryTree.root) 
    
testBinaryTreeWithList()
    


"""

TREE with OOP

"""

class BinaryTree(object):
    
    def __init__(self,root_obj):
        
        self.key = root_obj
        self.left_child = None
        self.right_child = None
        
    def __repr__(self):
        return self.key
        
    def insert_left(self,new_node):
        
        new_child = BinaryTree(new_node)
        
        if self.left_child == None:
            self.left_child = new_child
        else:
            
            new_child.left_child = self.left_child
            
            self.left_child = new_child
        
        
    def insert_right(self,new_node):
        
        new_child = BinaryTree(new_node)
        
        if self.right_child == None:
            self.right_child = new_child
        else:
            
            new_child.right_child = self.right_child
            
            self.right_child = new_child
        
    
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
        
    def set_root_value(self,payload):
        self.key = payload
        
    def get_root_value(self):
        return self



def testBinaryTree():
    """  
    Binary Tree


                a
               -  -
               |  |
               b  c  
             --   --
             | |  |
             d e  f 
    """
    binaryTree = BinaryTree("a")
    print(binaryTree)
    
    binaryTree.insert_left("b")
    print(binaryTree.get_left_child())
    
    binaryTree.insert_right("c")
    print(binaryTree.get_right_child())
    
testBinaryTree()