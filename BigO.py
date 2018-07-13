# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 05:09:04 2018

@author: sanooj
"""

"""
python lists

1. indexing O(1)
"""

def method1():
    
    l = []
    
    for n in range(10000):
        l = l + [n]
        
def method2():
    
    l = []
    
    for n in range(10000):
        l.append(n)
        
        
def method3():
    
    l = [n for n in range(10000)]
    
    
#most efficient    
def method4():
    
    l = list(range(10000))
    
    
#Dictionaries
    
    d = { "k":1, "kk":2 }
    
    
    
    
x = 10
count = 0
while x > 0:
    count += 1
    print(count)
    y = 2 + 2
    x = x // 2
    
print(count)