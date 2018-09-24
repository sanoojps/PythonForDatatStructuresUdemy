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
            if AnagramCheck.isAnagramPreferredSolution(word_one=current_word,word_two=element):
                
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
 
print(get_anagrams())
