# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 01:05:45 2018

@author: sanooj
"""

"""

Given a string of words
reverse all words

input: "This is the best"

putput: "best the is this"

all trailing an leading white space shoudld be removed

example

in: "Hi John,    are you ready to go?"
out: "go? to ready you are John, hi"

"""

class WordOrder(object):
    
    def __init__(self,word: str, order: int):
        
        self.word = word
        self.order = order
        
    def __repr__ (self):
        return (
                "%s"
                %(self.word)
                )
        
    


def reverse_a_string_of_words(string_of_words: str):
    
    
    #remove trailing and leading white space
    string_of_words = \
    string_of_words.lstrip().rstrip()
    
    
    #enumerate through word
    
    words = []
    
    index = 0
    
    array_of_words = \
    string_of_words.split(" ")
    
    print("array_of_words:  %s" %(array_of_words))
    
    for word in array_of_words:
        
        word_order = \
        WordOrder(
                word,
                index
                )
        
        words.append(word_order)
        
        index+=1
        
        
    words_reversed = []
    
    index = len(words) - 1 
    
    for word in words:
        
        if words[index] != '':
            words_reversed.append(words[index])
        
        index-=1
        
    print(words_reversed)
    
#reverse_a_string_of_words("    the very best    ")

atr = "Hi John,    are you ready to go?"    
reverse_a_string_of_words(atr)
