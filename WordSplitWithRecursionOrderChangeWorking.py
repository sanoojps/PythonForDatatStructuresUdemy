# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 04:41:47 2018

@author: sanooj
"""

def get_first_char(string: str):
    
    count = 1
    for char in string:
        
        if count == 1:
            return char
        else:
            break


"""
make a susbtring from a given string
using the range (star_index, start_index + length)

"""
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
                
                if tmp_substring == None:
                    pass
                
                print(tmp_substring)
                
                if word == tmp_substring:
                    matches.append(tmp_substring)
                
                # substrings don't match
                # so keep moving forward
                else:
                    pass
                
                # push the index
                
                tmp_substring_length = \
                0 if tmp_substring is None  else (len(tmp_substring) - 1)
                
                limit = \
                limit + tmp_substring_length + phrase_index
                
                print("limit %s" %(limit))
                
            else:
                pass
            
            phrase_index += 1
                
    return matches
        
    
    
phrase = "themanran"
list_of_words = ["the","man","ran"]

print("get_substring")
print(
      get_substring(
        phrase,
        3,
        3
        )
      )


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


phrase = "ilovedogsjohngerrard" 
list_of_words = [
        "i",
        "am",
        "a",
        "dogs",
        "gerrard",
        "lover",
        "love",
        "john"
        ]

print(make_substring_and_match_appr(
        phrase = phrase,
        list_of_words = list_of_words
        )
        ) # ['i', 'dogs', 'love', 'john']
