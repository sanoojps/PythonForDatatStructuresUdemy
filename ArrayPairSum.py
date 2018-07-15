# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 19:35:25 2018

@author: sanooj
"""

"""
Array Pair sum
Given an ineger array 
output all the unique pairs that sum up to a specific value

so 

pair_sum([1,3,2,2] , 4)

would return 
(1,3)
(2,2)

that sums up to 4

"""

#def get_index_with_placeholder(
#        placeholder: str,
#        array: list,
#        ):
#    
#    index = None
#    
#    try:
#        
#        element_with_placeholder = \
#        [x for x in array if x[1] == placeholder][0]
#        
#        index = array.index(element_with_placeholder)
#        
#    except (ValueError, IndexError) as exception:
#        
#        index = None
#        
#    return index
#        
#
#def make_pairs_with_placeholder(array:list, sum_value:int):
#    
#    pairs_array = []
#    placeholder = "0_0_0"
#    
#    for element in array:
#        
#        index = \
#        get_index_with_placeholder(
#                placeholder,
#                pairs_array
#                )
#        
#        if index != None:
#            pairs_array[index] = \
#            (pairs_array[index][0],element)
#            
#        else:
#            pairs_array.append((element,placeholder))
#           
#    print(array)
#    print(pairs_array)
    

def pair_sum(array:list, sum_value:int):
    
    pairs_array = []
    
    for outer_index in range(0,len(array)):
        
        for inner_index in range(outer_index,len(array)):
            
            #get elements
            element_a = array[outer_index]
            element_b = array[inner_index]
            
            #check for sum
            if element_a + element_b == sum_value:
                
                # make pair
                pair = (element_a,element_b)
                
                #eliminate duplicates
                if pair in pairs_array:
                    #duplicate
                    #nop
                    pass
                else:
                    #unique
                    #append
                    pairs_array.append(pair)
                
    print(pairs_array)
    
            
pair_sum([1,3,2,2] , 4)