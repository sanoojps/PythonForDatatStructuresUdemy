# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:36:23 2018

@author: sanooj
"""

"""
NSArray*  a = @[
                   @"pear",
                   @"amleth",
                   @"dormitory",
                   @"tinsel",
                   @"dirty room",
                   @"hamlet",
                   @"listen",
                   @"silent",
                   
                   ];

        output =
        @[
        
        @"amleth,hamlet",
        @"dirty room,dormitory,",
        @"listen,silent,tinsel",
        @"pear"
        
        ]
        

1



"""

import AnagramCheck


NSArray = [
           "pear",
           "amleth",
           "dormitory",
           "tinsel",
           "dirty room",
           "hamlet",
           "listen",
           "silent",
                   ];

        
# TRIAL SOLUTION        
def get_anagrams(word_list:list = NSArray):
    
    current_index = 0
    current_word = None
    current_word_processed = False
    
    
    anagrams = {}
    
    while(current_index < len(word_list)):
        
        current_word = word_list[current_index]
        current_word_processed = False
        
        for element in word_list:
            
            # check if current word and element are anagrams
            if AnagramCheck.isAnagramPreferredSolution(
                    word_one=current_word,
                    word_two=element
                    ):
                
                # check if the word is in the set
                anagram_set = anagrams.get(element)
                
                if anagram_set != None:
                    
                    if current_word in anagram_set:
                        pass
                    else:
                        anagram_set.add(current_word)
                        anagrams[element] = anagram_set
                
                else:
                    anagram_set = set()
                    anagram_set.add(current_word)
                
                    anagrams[current_word] = anagram_set
                pass
                current_word_processed = True
            
            else:
                pass
        
        
        if not current_word_processed:
            # check if the word is in the set
            anagram_set = anagrams.get(current_word)
            if anagram_set != None:
                pass
            
            else:
                anagram_set = set()
                anagrams[current_word] = anagram_set
        
        current_index+=1
    return anagrams
 
# print(get_anagrams())

"""
###############################
# FINAL WORKING SOLUTION
 
# make a dictionary of words
    dict_key = word
    dict_value = set(words/anagrams)
        
# 1. loop through each word
# 2. lopp through all keys on the dict
# 3. check if the current_word is an anagram of any key
       a word is an anagram to itself so no need to check for equality
       
# 4. if anagram 
    .. add the current_word to the "set" associated with the dict_key
# 5. else.. ..
        add the word to the set and add the word to the dict
############################    

"""
    
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

def get_anagrams_(word_list:list = NSArray):
    
    current_index = 0
    current_word = None
    # flag to inidcate if current word is processed
    # used to check if the word or its anagram is present in the dictionary
    current_word_processed = False
    
    
    anagrams = {}
    
    while(current_index < len(word_list)):
        
        current_word = word_list[current_index]
        
        # check if current word is
        # an anagram
        
        # check if the word is in the dict
        for key in anagrams.keys():
            
            if isAnagramPreferredSolution(
                    word_one=current_word,
                    word_two=key
                    ):
                
                anagram_set = anagrams.get(key)
                
                if anagram_set is None:
                    
                    key_set = set()
                    key_set.add(current_word)
                    
                    anagrams[key] = \
                    key_set
                    
                else:
                    if not current_word in anagram_set:
                        anagram_set.add(current_word)
            
                current_word_processed = True
            # current_word .. not an anagram    
            else:
                pass
            
            
        if current_word_processed:
            pass
        else:
            
            key_set = set()
            key_set.add(current_word)
                    
            anagrams[current_word] = \
            key_set
            
        current_index+=1
        current_word_processed = False
    
    # sort anagram dict keys
    anagram_keys = anagrams.copy().keys() 
    
    sorted_anagram_strings = []
    
    for anagram_key in anagram_keys:
        
        key_set = anagrams[anagram_key]
        
        anagram_string = ""
        
        if key_set:
            sorted_key_set = sorted(key_set)
            
            for index,key in enumerate(sorted_key_set):
                anagram_string = \
                anagram_string + key + \
                ("" if index == len(sorted_key_set) - 1 else ",") 
                
            sorted_anagram_strings.append(anagram_string)
            
    sorted_anagram_strings.sort()
    
    return sorted_anagram_strings



print(get_anagrams_()) 
#['amleth,hamlet', 'dirty room,dormitory', 'listen,silent,tinsel', 'pear']