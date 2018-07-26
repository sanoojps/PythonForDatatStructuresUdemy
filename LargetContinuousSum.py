# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:43:46 2018

@author: sanooj
"""

"""
Largest continuous sum

given an array find the subsequence
 that whne added up gives the largets sum
 
 report start and end points

"""

def large_count_sum(array: list):
    
    """
    1. array positive.. simply sum all
    
    2. 
    
    """
    
    # check for empty array
    if len(array) == 0:
        return 0
    
    max_sum = current_sum = array[0]
    
    for number in range(1,len(array)):
        
        current_sum = \
        max(
                current_sum 
                + array[number] , 
                array[number]
                )
        
        max_sum = \
        max(current_sum, max_sum)
        
        
    print(max_sum)
    #print("start_point %d" %(start_point))
    #print("end_point %d" %(end_point))
    
    return max_sum
    
    
    
#large_count_sum([2,3,4,5])

large_count_sum([-2,1,-2,3,4,2]) #9
large_count_sum([1,2,-1,3,4,10,10,-10,-1]) #29


# still no able to find the actual sub sequence    
def large_count_sum_my_way(array: list):
    
    # check for empty array
    if len(array) == 0:
        return 0
    
    max_sum = current_sum = 0
    
    max_sub_sequence = set(array)
    
    for number in array:
        
        current_sum = \
        current_sum + number
        max_sub_sequence.add(number)
        
        # -ve current sum
        if current_sum < 0:
            current_sum = 0
            max_sub_sequence.clear()
            
        # max_sum < current_sum
        elif max_sum < current_sum:
            max_sum = current_sum
            max_sub_sequence.add(number)
            
        
    print(max_sum)
    print(max_sub_sequence)
            
            
large_count_sum_my_way([1,2,-1,3,4,10,10,-10,-1])        
# Output 
# 29
#[1, 2, 3, 4, 10, 10]        
        
def large_count_sum_hash(array: list):
     
     ## sort the array 
     #array.sort()
     
     set_s = set(array)
     
     for number in array:
         # add them to a hash or Set
         set_s.add(number)
     
     max_sum = current_sum = 0
     
     for number in array:
         
         current_sum = \
         current_sum + number
         
         if current_sum > max_sum:
             max_sum = current_sum
             
         # -ve number
         if current_sum < 0:
             current_sum = 0
             
     print(
             "large_count_sum_hash %s" %(max_sum)
             )
         
         
large_count_sum_hash([1,2,-1,3,4,10,10,-10,-1]) 
          
         
        
def large_count_sum_preferred_solution(array: list):
     
    if len(array) == 0:
        return 0
    
    max_sum = current_sum = array[0]
    
    for number in array[1:]:
        
        # restting is current_sum is less than
        # current number
        current_sum = \
        max(current_sum + number , number)
        
        # find max sum
        # get larger
        max_sum = \
        max(max_sum , current_sum)
        
    return max_sum
     

print(large_count_sum_preferred_solution(
        [1,2,-1,3,4,10,10,-10,-1]
        )
         ) #29