# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 21:17:58 2018

@author: sanooj
"""

"""

Fibonacci

"""
#( 1 + 1 + 2 + 3  )

"""

F(4) = 1 + 1 + 2 + 3 = 7

"""

#F(n+2) = F(n) + F(n+1) 
def fibonacci(number:int):
    
    sum = 0
    
    seed_one = 1
    seed_two = 1
    
    fibonacci= []
    
    for index in range(0,number):
        
        print("index: %s sum: %s" %(index,sum))
        
        if sum == 0:
         
            sum = seed_one + seed_two
            
            fibonacci += [seed_one , seed_two, sum]
            
        else:
        
            if number == len(fibonacci):
                break
            
            sum = seed_one  + seed_two
            
            fibonacci.append(sum)
            
        seed_one = seed_two
        seed_two = sum
        
        
    print("sum %s" %(fibonacci))
    
    sum = 0
    for element in fibonacci:
        sum += element
        
    print("sum = %s" %(sum))
        
    
        
print(fibonacci(number=3)) #(1 + 1 + 2)
print(fibonacci(number=4)) #(1 + 1 + 2 + 3)
print(fibonacci(number=5)) #(1 + 1 + 2 + 3 + 5)
print(fibonacci(number=6)) #(1 + 1 + 2 + 3 + 5 + 8)
print(fibonacci(number=7)) #(1 + 1 + 2 + 3 + 5 + 8 + 13)
print(fibonacci(number=8)) #(1 + 1 + 2 + 3 + 5 + 8 + 13 + 21)
print(fibonacci(number=10)) 
#(1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34 + 55)


"""


Non RECURSION


"""


def fib_iter(number:int):
    
    a,b = 0,1
    
    for i in range(number):
        
        a,b = b,a+b
        
    return a


print(fib_iter(number=10)) #55



"""


RECURSION


"""


def fib_rec(n):
    
    # base
    if n <= 1:
        return n
    
    
    #recurse
    else:
        return fib_rec(n-1) + fib_rec(n-2)
        
print("fib_rec")        
print(fib_rec(10)) #55
    



"""


Memoize RECURSION


"""

# Cache
n = 10
cache = [None] * (n+1)

def fib_dyn(n):
    
    # Base Case
    if n <= 1:
        return n 
    
    # Check Cache
    
    if cache[n] != None:
        return cache[n]
    
    # Keep Setting Cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2) 
    
    return cache[n]
