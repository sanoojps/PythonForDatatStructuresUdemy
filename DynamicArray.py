# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 00:41:38 2018

@author: sanooj
"""

"""
Classes
"""
class Sample(object):
    
    def public(self):
        print("Use Tab to see me")
        
    def _private(self):
        print("won't be ale to see me on tab")
        
        
import ctypes

class DynamicArray(object):
    
    def __init__(self):
        
        #count
        self.n = 0
        
        #array capacity
        self.capacity = 1
        
        #
        self.A = self.make_array(self.capacity)
        
        
    #length    
    def __len__(self):
        return self.n
    
    #indexed access syntax 
    def __getitem__(self, k):
        
        if not 0 <= k < self.v:
            return IndexError("K is out of bounds!")
        
        return self.A[k]
    
    #add to end
    def append(self,element):
        
        if self.n == self.capacity:
            # 2X if capacity isn't enough
            self._resize(2 * self.capacity)
             
        self.A[self.n] = element
        self.n += 1
        
    def _resize(self,new_cap):
        
        B = self.make_array(new_cap)
        
        for k in range(self.n):
            B[k] = self.A[k]
            
        self.A = B
        
        self.capacity = new_cap
        
        
    #makes an array of capcity max_cap
    def make_array(self,new_cap):
        
        return (new_cap * ctypes.py_object)() 
      
        
    
array = DynamicArray()

array.append(1)