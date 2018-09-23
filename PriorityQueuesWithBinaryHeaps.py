# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 00:43:44 2018

@author: sanooj
"""

"""
PRIORITY QUEUE with BINARY HEAPS

1. Highest priority at the front of the queue
2. lowest priority at the back 
3. dequeue fron front
4. order of items is determined by the priority
5. enqueue .. new item moves to front based on priority
6. uses Binary Heap 
    6.1 enqueue and dequeue O(log n)
    6.2. two varitons 
        6.2.1 Min heap
            6.2.1.1 Smallest key always on front
        6.2.2 max heap
            6.2.2.1 Largest key always on front
"""

"""
Min Heap

Considerations
--------------
1. we use Binary Tree cos of logaritmic complexity
2. to keep it that we need to balance the tree
3. a "balanced tree" has roufghly the same number of nodes on both sides
4. we keep the tree balanced by implementing a Complete Binary tree
5. A complete binary tree is a tree in which each level has its own nodes
5. 2p and 2p+1 position of elementes
"""

class BinaryHeapADT(object):
    
    def __init__(self):
        pass
    
    def insert(self,value):
        pass
    
    def find_min(self):
        pass
    
    def del_min(self):
        pass
    
    def is_empty(self):
        pass
    
    def size(self):
        pass
    
    def build_heap(self,list):
        pass
    
"""
                 5
       9                     11

     14      18            19     21
     
   33  17  27              
     
   
   0  1  2  3   4  5   6   7   8   9   10  11
   0  5  9  11 14  18  19  21  33  17  27   
   
   5 is at index 1
   5's children are 9 at index 2 and 11 at index 3
   so 5's children are at 2 times 5's index and 2times 5's index + 1
   left child at 2p  where p is position of parent
   right child at 2p+1
         
"""    
class BinaryHeap(BinaryHeapADT):
    
    def __init__(self):
        
        self.heap_list = [0]
        self.current_size = 0
        
        
    """
    1. efficient way is to add item to end of list
    2. this gaurantees the binary tree i always complete
    3. will likely violate the heap structure property
    4. to fix this 
        4.1 compare newly added item to its parent
            4.1.1 if new_item < parent -> swap both and continue till that is 
                    no longer necessary
            4.1.2 
    """    
    def insert(self,value):
        # add to bottom
        self.heap_list.append(value)
        
        #increment current size
        self.current_size+=1
        
        # balance the tree by moving it to position
        # as min elements go to the beginning of the array
        # this is a min heap
        # we beging with and element in index 0
        # that is not included in the size of the heap
        self.percolate_up(index=self.current_size) 
    
    
    
    
    """
    Moving Element based on its value
    Min heap
    Rule: Smaller values at top
    
               5
       9                     11

     14      18            19     21
     
   33  17  27    7 -> added          
     
   
   0  1  2  3   4  5   6   7   8   9   10  11
   0  5  9  11 14  18  19  21  33  17  27   7 -> added
   
   7 -> new element added as right child of 8
   
   find 7's parent -> index of 7 / 2 (integer division -> 11//2 = 5)
   
   7's parent is at index 5 which is 18
   
   18's parent is at index 5 // 2 = 2 which is 9 
   
    """
    
    def percolate_up(self,index: int):
        
        while index // 2 > 0:
            
            # comparing new element and it's parent
            if self.heap_list[index] < self.heap_list[index // 2]:
                
                tmp =  self.heap_list[index // 2]
                
                self.heap_list[index // 2] =  self.heap_list[index]
                
                self.heap_list[index] = tmp
                 
            index = index // 2 # parent of parent
        
      
    """
    Min heap 
    -- so min element will always be root element
    -- this requires getting back the structure of the tree/heap
        1. move last element in the list to the root
        2. Now heap structure is restored
        3. but heap order is destroyed
        4. we restore heap order by pushing the root node down the tree
            to its proper position
            4.1 first swap the root with the smallest child 
                less than the root
            4.2 repeat untill we reach a node 
                which is less that both its children    
        
    """
    def del_min(self):
        
        # get root element
        root = self.heap_list[1]
        
        # swap last element with root
        self.heap_list[1] = \
        self.heap_list[self.current_size]
         
        #pop i.e remove last elment
        self.heap_list.pop()
       
         # adjust size
        self.current_size-=1 
        
        # adjust position of current root node
        # so that min elements are always on the top
        self.percolate_down(index=1)
        
        return root
        
    
    
    """
    1. Mostly starts at root
    2. Check if it has children
    3. loop as long as it has children ie. 2p reaches last element
    4. find minChild
    """
    def percolate_down(self,index: int):
        
        index = index
        
        while (index * 2) <= self.current_size:
            
            min_child_index = self.min_child_index(index)
            
            # compare this node and min index
            if self.heap_list[index] > \
               self.heap_list[min_child_index]:
                   
                   tmp = self.heap_list[index]
                   
                   self.heap_list[index] = \
                   self.heap_list[min_child_index]
                   
                   self.heap_list[min_child_index] = \
                   tmp
                   
            index = min_child_index
                   
    
    def min_child_index(self,i):
        
        # sanity check
        # as we are finding all children using  
        # 2p and 2p+1 formula
        if (i * 2) + 1 > self.current_size:
            return i * 2
        
        else:
            
            # checking children
            # they are at 2p and 2p+1
            left_child_index  = i*2
            right_child_index = (i*2) + 1
            
            if self.heap_list[left_child_index] < \
               self.heap_list[right_child_index]:
               
                return left_child_index
            
            else:
                
                return right_child_index
    
    
    """
    1. insert each key one a time from a list
    2. since you start the list of one item, the list is sorted
    3. you could use binary search 
        to find the right position to insert the next key
    4. O(log n)
    5. inserting an item in the middle of the list
        may require O(n) operations to shift the rest of the list
        over to make room for new key
    6. so insert to Binary heap is (O(n log n))
    7. if we get an entire list at first then 
        we can build the whole heap in O(n) opertaions
    """
    def build_heap(self,a_list: list):
        
        list_count = len(a_list)
        
        self.current_size = list_count
        
        self.heap_list = [0] + a_list[:] # copy of list
        
        #sort 
        count = list_count
        while (count > 0):
            self.percolate_down(count)
            count-=1
        
    
def print_binary_heap(binary_heap):
        print(binary_heap.heap_list)
        print(binary_heap.current_size)
        
def binary_heap_normal_test():

    binary_heap = BinaryHeap()
    print_binary_heap(binary_heap)
    
    # insert 2 values ,14,18,19,21,33,17,27
    """
    
        0
        2    
    5      11    
  9  12   
    """
    for element in [5,9,11,2,12]:
        binary_heap.insert(element)
    
    print_binary_heap(binary_heap) #[0, 2, 5, 11, 9,12]
    
    print("binary_heap.del_min()")
    binary_heap.del_min()
    
    print_binary_heap(binary_heap)
    
binary_heap_normal_test()


print("binary_heap_build_test")
def binary_heap_build_test(list_a=[5,9,11,2,12]):
     
    binary_heap = BinaryHeap()
    binary_heap.build_heap(a_list=list_a)
    print_binary_heap(binary_heap)
    
binary_heap_build_test()

"""
        0
        9    
    6      5                   
  2   3   
  
  --------- 2<-->6
        0
        9    
    2      5    
  6  12   
  
  --------------2<-->9
          0
        2    
    9      5    
  6  12

------------------3<-->9

        0
        2    
    3      5    
  6  9   
   
"""

binary_heap_build_test([9,6,5,2,3])
    