# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 02:41:04 2018

@author: sanooj
"""

"""

array of non-negetive number

a new array created by 
shuffling and deleting at random indexes from the first array

find elements missing in the array 

finder([1,2,3,4,5,6,7] , [3,7,2,1,4,6])

"""

# duplicates should be considered


##
### using sets
##  O(n) n = length of largest set
##
def finder_set_logic_no_duplicates(
        array: list, 
        shuffled_array: list
        ):
    
    array_set = \
    set(array)
    
    shuffled_array_set = \
    set(shuffled_array)
    
    elements_not_present_in_shuffled_srray = \
    array_set.difference(shuffled_array_set)
    
    print(elements_not_present_in_shuffled_srray)
    
    
finder_set_logic_no_duplicates([1,2,3,4,5,6,7] , [3,7,2,1,4,6])


from nose.tools import assert_equal

class TestFinder(object):
    
    def test_finder(self,sol):
        
        assert_equal(
                sol(
                        [5,5,7,7] ,
                        [5,7,7]
                    ) ,
                5
                )
                
        assert_equal(
                sol(
                        [1,2,3,4,5,6,7] ,
                        [3,7,2,1,4,6]
                    ) ,
                5
                )
                
        assert_equal(
                sol(
                        [9,8,7,6,5,4,3,2,1] ,
                        [9,8,7,5,4,3,2,1]
                    ) ,
                6
                )
                
        print("All tests passed")
        
# Run test
        
test = TestFinder()
#test.test_finder(finder_set_logic_no_duplicates) 




###########################
# With zip and tuples logic
###########################
# 1. sort both arrays
# 2. use two loops 
# 3. iterate through both
# 4. compare each element
# 5. whichever doesn't match stop looping
# 6. element in the first loop being compared 
#    is the missing element  
#7. O(NlogN)
##########################

def finder_sort_and_zip(array: list, shuffled_array: list):
    
    #sorted_array
    array.sort()
    
    #sorted_shuffled_array
    shuffled_array.sort()
    
    # combines but arrays into tuples
    # groups elemente at same indexes
    zipped_array = \
    zip(array,shuffled_array)
    
    # tuple unpacking
    for element_one, element_two in zipped_array:
        
        if not element_one == element_two:
            print(element_one)
            
            
    print(array[-1])

finder_sort_and_zip(
        [1,2,3,4,5,6,7] ,
        [3,7,2,1,4,6])
        


###########################
# Binary search solution
###########################
# 1. sort the array
# 2. perform binary search
# O(NlogN)
###########################



###########################
# Dictionary solution
###########################
# 1. make two dictionaries
#     key = element in array
#     value = number of occurances        
# 2. look for keys
# O(3n + 2)
# detects duplicates
###########################

def make_counts_dict(array: list) -> dict:
    
    array_dict = {}
    
    for element in array:
        
        #get from dict
        value = array_dict.get(element)
        
        #check in dict
        if value == None:
            
            # add value
            array_dict[element] = 1
            
        else:
            
            #increment
            array_dict[element] = value + 1
    
    return array_dict
    

def finder_dictionary(array: list, shuffled_array: list):
    
    # O(n)
    array_dict = \
    make_counts_dict(array)
    
    # O(n)
    shuffled_array_dict = \
    make_counts_dict(shuffled_array)
    
    larger_dict = \
    array_dict if len(array_dict) > len(shuffled_array_dict) \
    else shuffled_array_dict
    
    smaller_dict = \
    array_dict if len(array_dict) < len(shuffled_array_dict) \
    else shuffled_array_dict
    
    elements = []
    
    # O(n)
    for key in larger_dict:
        
        # O(1)
        value_in_smaller_dict = \
        smaller_dict.get(key)
        
        # O(1)
        value_in_larger_dict = \
        larger_dict.get(key)
        
        # make sure key in not none
        if value_in_smaller_dict == None:
            elements.append(key)
        elif value_in_smaller_dict < value_in_larger_dict:
            elements.append(key)
        else:
            pass
        
    
    # O(n + n + n + 1 + 1) = ) = O(3n + 2)

    
    print(elements)
            

finder_dictionary(
        [1,2,3,4,5,6,7] ,
        [3,7,2,1,4,6])
            
        
finder_dictionary(
        
                [1,2,3,4,5,6,7] ,
                [3,7,2,1,4,6]
        )
        
finder_dictionary(
                [9,8,7,6,5,4,3,2,1] ,
                [9,8,7,5,4,3,2,1]
        )

finder_dictionary(
                [9,8,7,6,5,4,3,2,1,1] ,
                [9,8,7,5,4,3,2,1]
        )

###########################
# Dictionary solution - collections module
###########################
# 1. make two dictionaries
#     key = element in array
#     value = number of occurances        
# 2. look for keys
# O(1)
# 4. if key not present "defaultdict" will add it 
# 5. won't detect duplicates 
###########################

def finder_with_defaultdict_no_duplicates(
        array: list, 
        shuffled_array: list):
    
    import collections
    
    default_dict = collections.defaultdict(int)
    
    # loop through shuffled array
    for number in shuffled_array:
        
        # will add key if not present
        # and set to 0
        # and increment it by 1
        default_dict[number] += 1
    
    # loop through array
    for number in array:
        
        #check if element is present
        if default_dict[number] == 0:
            
            # not present
            # return
            return number
            
            # element present 
        else:
            
            # decrement count by 1
            default_dict[number] =- 1
            
    
        
print(
      finder_with_defaultdict_no_duplicates(
        [1,2,3,4,5,6,7] ,
        [3,7,2,1,4,6])
    )
            

print(     
finder_with_defaultdict_no_duplicates(
        
                [1,2,3,4,5,6,7] ,
                [3,7,2,1,4,6]
        )
)
  
print(      
finder_with_defaultdict_no_duplicates(
                [9,8,7,6,5,4,3,2,1] ,
                [9,8,7,5,4,3,2,1]
        )
)

print(
finder_with_defaultdict_no_duplicates(
                [9,8,7,6,5,4,3,2,1,1] ,
                [9,8,7,5,4,3,2,1]
        )
)

def finder_with_defaultdict_with_duplicates(
        array: list, 
        shuffled_array: list):
    
    import collections
    
    default_dict = collections.defaultdict(int)
    
    # loop through shuffled array
    for number in array:
        
        # will add key if not present
        # and set to 0
        # and increment it by 1
        default_dict[number] += 1
    
    
    #print(default_dict)
    
    omitted_members = []
    
    # loop through array
    for number in shuffled_array:
        
        #check if element is present
        if default_dict[number] == 0:
            
            # not present
            # add to omitted_members
            omitted_members.append(number)
            
            # element present 
        else:
            
            #print(default_dict)
            
            # decrement count by 1
            default_dict[number] -= 1
            
            #print(default_dict)
    

    print(default_dict)
        
    # handling duplicates    
    for key in default_dict:
        
        if default_dict[key] != 0:
            omitted_members.append(key)
            
    
            
    return omitted_members
            
print(
      finder_with_defaultdict_with_duplicates(
        [1,2,3,4,5,6,6,7] ,
        [3,7,2,1,4,6])
    )
            