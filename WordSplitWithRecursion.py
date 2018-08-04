# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 05:28:50 2018

@author: sanooj
"""

"""

in: list of words with no spaces and set of words
out : valid words contained in the given set of words

eg:
    in   "themanran" [the,man,ran]
    out  the man ran

    in   "ilovedogsjohn" [i,am,a,dogs,lover,love,john]
    out  [i, love, dogs, john]
    
     in   "themanran" [clown,ran,man]
    out  []

""" 

# stupid logic
######STUPID###############
def make_substring_and_match(
        phrase:str,
        word_to_match: str):
    
    length = len(word_to_match)
    
    matches = []
    
    substrings = []
    
    tmp_word = ""
    
    # loop through all chars in phrase
    for char in phrase:
       
        # add to tmp_word 
        # to begin construction of a substring
        # substring would be of the same length as the 
        # "word_to_match"
        tmp_word += char
        
        if len(tmp_word) == length:
            
            # add to substrings
            substrings.append(tmp_word)
            
            # check for match
            if tmp_word == word_to_match:
                matches.append(tmp_word)
            else:
                pass
            
            # reset tmp_word
            tmp_word = ""
            
        else:
            pass
            
            
    return matches
    
def word_split(phrase,list_of_words,output=None):
    
    matches = []
    
    # get each word
    for word in list_of_words:
        
        match = \
        make_substring_and_match(phrase,word)
        
        # add contents
        matches += match
        
    return matches

######STUPID###############

def get_first_char(string: str):
    
    count = 1
    for char in string:
        
        if count == 1:
            return char
        else:
            break

def get_substring(
        string: str, 
        start_index: int,
        length: int
        ):
    
    index = 0
    
    sub_string = ""
    
    first_char_matched = False
    
    for char in string:
        
        # start_index check
        if index == start_index:
            
            first_char_matched = True
        
        else:
            
            pass
        
        # check if first chars matched
        if first_char_matched:
            
            # begin creating the substring
            sub_string += char
        
        else:
            
            #reset substring
            sub_string = ""
            
        # check for end index
        
        if len(sub_string) == length:
            
            return sub_string
        
        else:
            
            index += 1
        
    

def make_substring_and_match_appr(
        phrase:str,
        list_of_words: list):
    
    matches = []
    
    # get each word
    for word in list_of_words:
        
        tmp_substring = ""
        
        # loop through phrase
        phrase_index = 0
        
        # denotes how many characters to skip 
        # after a substring of the length of the word
        # whose first letter matches the word is found
        limit = 0
        
        first_char_matched = False
        
        for char in phrase:
            
            if phrase_index == 0:
                pass
            elif phrase_index == limit:
                first_char_matched = False
                pass
            
            # meaning match found and substring created
            # now the lopp should
            # skip over the chars that make up the substring
            if first_char_matched and limit > 0:
                phrase_index += 1
                continue
            else:
                pass
                
            
            # check if first letter of word
            # matches char
            # we will construct a substring of
            # the same length as the word 
            # from that position
            
            # can also do word[0]
            if get_first_char(word) == char:
                
                first_char_matched = True
                
            else:
                
                pass
            
            
            if first_char_matched:
                
                # construct the substring
                tmp_substring = \
                get_substring(
                        phrase,
                        phrase_index,
                        len(word)
                        )    
                
                print(tmp_substring)
                
                if word == tmp_substring:
                    matches.append(tmp_substring)
                
                # push the index 
                limit += 3
                
            else:
                pass
            
            phrase_index += 1
                
    return matches
        
    
    
phrase = "themanran"
list_of_words = ["the","man","ran"]
#            
#print(
#      make_substring_and_match(
#              phrase,
#              list_of_words[0]
#              )
#      )
#      
#print(
#      word_split(
#              phrase,
#              list_of_words
#              )
#      )

#phrase = "ilovedogsjohn" 
#list_of_words = [
#        "i",
#        "am",
#        "a",
#        "dogs",
#        "lover",
#        "love",
#        "john"
#        ]
#
#print(
#      word_split(
#              phrase,
#              list_of_words
#              )
#      )
#
#print(get_first_char(("")))


#print(
#      make_substring_and_match_appr(
#        phrase = phrase,
#        list_of_words = list_of_words
#        )
#      )
#      
#print(
#      get_substring(
#        phrase,
#        3,
#        3
#        )
#      )
      
#make_substring_and_match_appr(
#        phrase = phrase,
#        list_of_words = list_of_words
#        )

#phrase = "ilovedogsjohn" 
#list_of_words = [
#        "i",
#        "am",
#        "a",
#        "dogs",
##        "lover",
#        "love",
#        "john"
#        ]
#
#make_substring_and_match_appr(
#        phrase = phrase,
#        list_of_words = list_of_words
#        )


phrase = "ilovedogsjohn" 
list_of_words = [
        "i",
        "am",
        "a",
        "dogs",
        "lover",
        "love",
        "john"
        ]

print(make_substring_and_match_appr(
        phrase = phrase,
        list_of_words = list_of_words
        )
        ) # ['i', 'dogs', 'love', 'john']
                    
                    
                    
                    
def make_substring_and_match_appr_using_indexes_and_slices(
        phrase:str,
        list_of_words: list):
    
        matches = []
    
    # get each word
    
        
        for word in list_of_words:
            
            index = 0
            for char in phrase:
                
                if word[0] == char:
                    
                    end_index = index+len(word)
                    
                    if end_index > len(phrase):
                        
                        break
                    
                    else:
                        
                        substring = \
                        phrase[index:index+len(word)]
                        
                        print(substring)
                        
                        if word == substring:
                            matches.append(substring)
            
           
                index += 1
                
        return (matches)
        
phrase = "ilovedogsjohn" 
list_of_words = [
       "i",
        "am",
        "a",
        "dogs",
        "lover",
        "love",
        "john"
        ]

print("make_substring_and_match_appr_using_indexes_and_slices")
print(
      make_substring_and_match_appr_using_indexes_and_slices(
        phrase = phrase,
        list_of_words = list_of_words
        )
        ) # ['i', 'dogs', 'love', 'john'] 
      
      
      
# find a sub array
# with elemnts whose characters match the ones in 
# letters_to_match
def sub_array_with_matches(
        array_of_words: list,
        letters_to_match: str
        ):
    
    match = []
    
    for char in letters_to_match:
        
        matches = set()
        index = 0
        for word in array_of_words:
            
            # start matching
            if word[index] == char:
                matches.add(word)
            else:
                index += 1
                
        
        
    
    
def word_split_matching_order(
        phrase:str,
        list_of_words: list):
    
        matches = []
        
        