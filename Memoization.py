# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 04:35:35 2018

@author: sanooj
"""

def reverse_a_string_with_recursion(string: str):
    
    length = len(string)
    
    if length <= 1:
        return string
    
    return string[length-1] + \
reverse_a_string_with_recursion(
            string[ 0 : (length - 1) ], 
            )
    
print(reverse_a_string_with_recursion("frog")) # gorf

print(reverse_a_string_with_recursion("hello world")) # dlrow olleh


def reverse_a_string_with_recursion_with_first_index(string: str):
    
    print("string")
    print(string)
    
    length = len(string)
    
    if length <= 1:
        return string
    
    return \
reverse_a_string_with_recursion_with_first_index(
        string[1:]
        ) + string[0]

print(reverse_a_string_with_recursion_with_first_index("frog"))
# # gorf
#
#print(reverse_a_string_with_recursion_with_first_index("hello world"))
# # dlrow olleh




