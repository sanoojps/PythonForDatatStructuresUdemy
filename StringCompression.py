# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 05:18:11 2018

@author: sanooj
"""

"""

input AAAABBBBCCCCCCDDEEEEE
output A4B4C5D2E4

input AAB
output A2B1

case sensitive
in: AAAaaa
out: A3a3

"""

# O(2n)
def compress_string(string: str):
    
    # remove all spaces
    
    char_counts_dict = {}
    
    for char in string:
        
        count = char_counts_dict.get(char)
        
        # element not present
        if count == None:
            
            char_counts_dict[char] = 1
            
        else:
            
            char_counts_dict[char] = count + 1
            
    print(char_counts_dict)
    
    compressed_string = ""
    
    for key in char_counts_dict:
        
        compressed_string += (key + str(char_counts_dict[key]))
        
    print(compressed_string)
        
    
compress_string("AAB")
compress_string("AAAABBBBCCCCCCDDEEEEE")
compress_string("AAAaaa")
        

"""
Does not use a data structure

This solution compresses without checking. 
known as the RunLength Compression algorithm

O(n)

"""
def compress_string_preferred_solution(string: str):
    
    compressed_string = ""
    
    length = len(string)
    
    # edge case
    
    # length 0
    if length == 0:
        return ""
    
    # length 1
    if length == 1:
        return string+"1"
    
    count = 1
    
    index = 0
    
    # loop through all chars
    for char in string:
        
        # skip first index
        if index == 0:
            index+=1
            continue
        
        # check for repetition
        if string[index] == string[index -1]:
            
            #repetition
            count+=1
            
        # no repetition
        # new char
        else:
            
            # update string
            compressed_string = \
            compressed_string \
            + string[index - 1] \
            + str(count)
            
            # reset count
            count = 1
    
        print(compressed_string)
        
        # increment index
        index+=1
    
    # add final char
    compressed_string = \
            compressed_string \
            + string[index - 1] \
            + str(count) 
            
    print(compressed_string)
    print(index)
        
print("compress_string_preferred_solution")
compress_string_preferred_solution("AAB")
compress_string_preferred_solution("ABCDE")
    
    
    