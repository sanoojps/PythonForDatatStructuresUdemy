# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 03:58:03 2018

@author: sanooj
"""

"""
Recursion

"""

def factorial(number):
    
    # 4! = 4 x 3 x 2 x 1 = 24
    # ie. 4 x (3 x 2 x 1) = 24
    # ie. 4 x 3! = 24
    # ie. 4 x 3 x (2 x 1) = 24
    # ie. 4 x 3 x 2! = 24
    # ie. 4 x 3 x 2 x (1) = 24
    # ie. 4 x 3 x 2 x 1! = 24
    # n! = n X (n-1)!
    # n = 0 = n! = 1
    
    # base case
    if number == 0:
        
        return 1
    
    else:
        
        return number * factorial(number -1)
    
    
print(factorial(4)) # 24
print(factorial(0)) # 1
print(factorial(1)) # 1 


"""

Write a recursive function which takes 
an integer and computes the cumulative sum of
0 to that integer


in: n = 4
out = 4+3+2+1+0 = 10

"""

def cumulative_sum_with_0(integer):
    
    # base
    if integer == 0:
        return 0
    
    else:
        return \
    integer + cumulative_sum_with_0(integer - 1)
    
print(cumulative_sum_with_0(4)) # 10
print(cumulative_sum_with_0(0)) # 0
print(cumulative_sum_with_0(1)) # 1



"""
Given an integer ,
create a function which returns the sum
of all individual digits in the integer

in   64321
out  5+4+3+2+1 = 15
""" 
    
# need to extractnumber in each position
# by dividing it with its postion
"""
        10 | 4321    1
            ------
        10 | 432    2
            ------
        10 | 43    3
            ------
        10 | 4     return 4
            ------

"""
def sum_of_digits(number):
    
    # base
    if number // 10 == 0:
        return number
    
    else:
        mod_number_reminder = number % 10
        mod_number_quotient = number // 10
        
        return \
    mod_number_reminder + \
    sum_of_digits(mod_number_quotient)
    
print(sum_of_digits(4321)) # 10
print(sum_of_digits(321)) # 6
print(sum_of_digits(1)) # 1

