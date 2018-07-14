# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 23:32:21 2018

@author: sanooj
"""

"""
Two strings writen using exact same letters

"public relations" -- "crap built on lies"
"clint eastwood" -- "old we st action"
"""

"""
Solution

1. if each letter occurs the same number of times 
    then its an anagram
    
2. 
"""

def _updateDict( 
  word_one_without_spaces:str, 
  word_dict:dict ):

  # loop through both words
    for char in word_one_without_spaces:
      
      # check if char exists 
      if word_dict.get(char) == None:
        # add count as 1
        word_dict[char] = 1
      
      # char exists
      else:
        #increment count
        word_dict[char] = \
        word_dict[char] + 1 


def anagaram_check(word_one:str, word_two:str):
    
    # dictinaries to hold the count 
    # of each letter in the words  
    dict_word_one = {}
    dict_word_two = {}
    
    # strip all spaces from the words
    # convert to lower case
    word_one_without_spaces = \
    word_one.replace(" ","").lower()

    word_two_without_spaces = \
    word_two.replace(" ","").lower()

    #unequal length check
    if  len(word_one_without_spaces) != \
        len(word_two_without_spaces) :
        # unequal length
        # return false 
        return False

    # update dicts with count of words
    # increment count if already present
    # set 1 if key is new
    # update dict_word_one
    _updateDict(word_one_without_spaces,dict_word_one)
    
    # updare dict_word_two
    _updateDict(word_two_without_spaces,dict_word_two)

    # print out dicts
    print("dict_word_one: %s" %(dict_word_one))
    print("dict_word_two: %s" %(dict_word_two))

    # total count_of_equalities
    # if this is eqla to length of dict_word_one
    # and dict_word_two 
    count_of_equalities = 0

    # loop through dict_word_one
    for (key,value) in dict_word_one.items():
      
      # key not in dict_word_two
      if dict_word_two.get(key) == None:
        # break out of loop
        break
      
      # key present in dict_word_two
      # check if the counts are equal  
      elif value == dict_word_two[key]:
        # increment
        count_of_equalities += 1
      
      # counts not equal   
      else:
        # no need for any further comparison
        # break out of the loop
        break

    # "count_of_equalities" should equal 
    # length of dictionaries "dict_word_one" 
    # and "dict_word_two"  
    if  len(dict_word_one) == \
        len(dict_word_two) == \
        count_of_equalities :
        return True
    else:
        return False

      
print(
  "isAnAnagram? %s" %(
          anagaram_check(
  word_one="dog",
  word_two="god"
  )
  )
  )


print(
  "isAnAnagram? %s" %(
  anagaram_check(
  word_one="public relations",
  word_two="crap built on lies"
  )
  )
  )

print(
  "isAnAnagram? %s" %(
  anagaram_check(
  word_one="clint eastwood",
  word_two="old we st action"
  )
  )
  )

print(
  "isAnAnagram? %s" %(
  anagaram_check(
  word_one="madam",
  word_two="madam"
  )
  )
  )
      


"""
2. Solution with sort
.. all leters sorted and check if equal
"""

def isAnagramUsingSort(word_one:str, word_two: str):

  # strip spaces and make lower case 
  # strip all spaces from the words
  # convert to lower case
  word_one_without_spaces = \
  word_one.replace(" ","").lower()

  word_two_without_spaces = \
  word_two.replace(" ","").lower()    
  
  return  sorted(word_one_without_spaces) == \
          sorted(word_two_without_spaces) 
    


def isAnagramPreferredSolution(word_one:str,
                               word_two: str):
    
  # strip spaces and make lower case 
  # strip all spaces from the words
  # convert to lower case
  word_one_without_spaces = \
  word_one.replace(" ","").lower()

  word_two_without_spaces = \
  word_two.replace(" ","").lower()
  
  #unequal length check
  if  len(word_one_without_spaces) != \
      len(word_two_without_spaces) :
          # unequal length
          # return false 
          return False
      
  # dictinaries to hold the count 
  # of each letter in the words  
  dict_with_count = {}
  
  for char in word_one_without_spaces:
      
      if char in dict_with_count:
          dict_with_count[char] += 1
      else:
          dict_with_count[char] = 1
          
  for char in word_two:
      
      if char in dict_with_count:
          dict_with_count[char] -= 1
      else:
          dict_with_count[char] = 1
          
  for key in dict_with_count:
      
      if dict_with_count[key] != 0:
          return False
    
  return True
  
    

