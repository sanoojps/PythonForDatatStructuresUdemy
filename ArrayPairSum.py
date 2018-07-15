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
 
####################   
# O(n2) with array 
####################
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

####################   
# O(n2) with set 
####################
def pair_sum_with_set(array:list, sum_value:int):
    
    pairs_array = set()
    
    for outer_index in range(0,len(array)):
        
        for inner_index in range(outer_index,len(array)):
            
            #get elements
            element_a = array[outer_index]
            element_b = array[inner_index]
            
            #check for sum
            if element_a + element_b == sum_value:
                
                # make pair
                pair = (element_a,element_b)
                
                # append
                # since set won't allow duplicates 
                pairs_array.add(pair)
                
    print(pairs_array)
    
            
pair_sum_with_set([1,3,2,2] , 4)

####################   
# O(n) with set
# From udemy Course 
####################
def pair_sum_with_sets_udemy(array:list, sum_value:int):
    
    #edge case check
    if len(array) < 2:
        return
    
    #sets for tracking
    seen = set()
    output = set()
    
    for num in array:
        
        # we need to make a tuple
        # 1. first element of that tuple is "num"
        # 2. we expect the sum of the first and second element 
        #    to be sum_value
        # 3. the second elemnt should be sum_value - first i.e "num"
        # 4. find it
        target = sum_value - num
        
        
        # check if the second element has alreday been found
        if target not in seen:
            # if not , add it
            seen.add(num)
        else:
            
            print("target %s" %(target))
            print("num %s" %(num))
            
            # number is already there in the "seen" set 
            # make the tuple
            min_value = min(num,target)
            max_value = max(num,target)
            
            print("min_value %s" %(min_value))
            print("max_value %s" %(max_value))
            
            # add 
            # min max to order the tuple
            output.add( (min_value,max_value) )
            #output.add( (num,target) )
            
    
    print(output)
    
pair_sum_with_sets_udemy([3,2,3,1,2,1,4,0] , 4)
    