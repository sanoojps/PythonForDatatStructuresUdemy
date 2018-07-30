# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 03:38:13 2018

@author: sanooj
"""

"""
DeQue - doube endedd Queue

1. ordered collection
2. two end "front and rear"
3. item scab added at font or rear
4. remove from both rear or rear

"""


class DeQue(object):
    
    def __init__(self):
        self.items = []
    
     # at bottom so index 0
    def _get_rear_index(self):
        return 0
    
    # at array size
    def _get_front_index(self):
        return len(self.items) -1
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def add_rear(self, item):
        self.items.insert(
                self._get_rear_index(),
                item)
    
    def remove_rear(self):
        return self.items.pop(
                self._get_rear_index())
    
    def add_front(self,item):
        self.items.insert(
                self._get_front_index(),
                item)
        
    def remove_front(self):
        return self.items.pop(self._get_front_index())
        
        
d = DeQue()

d.add_front("hello")
d.add_rear("world")

print(d.size())

print(d.remove_front() + (" ") + d.remove_rear())

print(d.size())

print(d.is_empty())