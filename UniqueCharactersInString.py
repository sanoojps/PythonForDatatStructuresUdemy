# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:38:34 2018

@author: sanooj
"""

"""

in: abcde
out: true 

in aabcde
out: false

"""


def contains_unique_chars_dict_sln(string: str):
    
    char_counts_dict = {}
    
    for char in string:
        
        count = char_counts_dict.get(char)
        
        # element not present
        if count == None:
            
            char_counts_dict[char] = 1
            
        else:
            
            if count + 1 > 1:
                return False
            
            char_counts_dict[char] = count + 1
         
    print(char_counts_dict)
    
    return True

print("contains_unique_chars_dict_sln")
print(contains_unique_chars_dict_sln("abcde"))
print(contains_unique_chars_dict_sln("abcdee"))
        
        
def contains_unique_chars_more_sln(string: str):
    
    #length = len(string)
    
    #count = 1
    
    index = 0
    
    for char in string:
        
        #skip first index
        if index == 0:
            index += 1
            continue
        
        # looking for duplicates
        if string[index] == string[index - 1]:
            # duplicate found
            return False
        # no duplicate
        else:
            index += 1
        
    
    return True

print("contains_unique_chars_more_sln")
print(contains_unique_chars_more_sln("abcde"))
print(contains_unique_chars_more_sln("abcdee"))


def contains_unique_chars_more_set(string: str):
    
    char_set = set()
    
    for char in string:
        if char in char_set:
            return False
        else:
            char_set.add(char)
            
    return True
        