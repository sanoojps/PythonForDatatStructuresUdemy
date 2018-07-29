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
    #string_of_words = \
    #string_of_words.lstrip().rstrip()
    
    
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
        
        if len(word_order.word) != 0:
            words.append(word_order)
        
        index+=1
        
    print("_words:  %s" %(words))
    
    # reversing
    words_reversed = []
    
    index = len(words) - 1 
    
    for word in words:
        
        if len(words[index].word) != 0:
            words_reversed.append(words[index])
        
        index-=1
        
    print(words_reversed)
    
#reverse_a_string_of_words("    the very best    ")

atr = "    Hi John,    are you ready to go?"    
reverse_a_string_of_words(atr)



def reverse_word_preferred(s):
    
    words = []
    length = len(s)
    spaces = [' ']

    i = 0
    
    while i < length:
        
        # check if char is space
        if s[i] not in spaces:
          
            # start counting the word
            word_begin = i
            
            # find the end of the word
            # lopp till another space is found
            while i < length and s[i] not in spaces:
                
                #kep looping
                i += 1
                
            # space found
            # word ended
            words.append(s[word_begin:i])
            
        # keep looping    
        i += 1
        
    return " ".join(reversed(words))

print("reverse_word_preferred")
print(reverse_word_preferred(atr))
                
def reverse_word_preferred_for_loop(string_of_words: str):
    
    words = []
    length = len(string_of_words)
    spaces = [' ','']

    # index to detect end of string
    i = 0                
    
    # each word in the string
    word_substring = ""
    
    print("length %s" %(length))
    
    for char in string_of_words:
        
        i += 1
        
        # check if it is space
        if char not in spaces:
            # not space

            # add to word array 
            word_substring += char
        
            print(word_substring)
            print(i)
            
            # last word
            if i == length:
                 words.append(word_substring)
        
        # go till next space
        else:
            
            # add word to dict
            if len(word_substring) > 0:
                words.append(word_substring)
            
            # reset substring
            word_substring = ""
            
    print(words)
    print(" ".join(reversed(words)))
         
print("reverse_word_preferred_for_loop")
reverse_word_preferred_for_loop(atr)