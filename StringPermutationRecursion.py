# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 08:38:25 2018

@author: sanooj
"""

"""
in : "abc"

out :  ["abc", "acb","bac","bca,"cab","cba"]

a bc
a cb

a b c
c b a

ab c
ba c

 
in xxx
out ["xxx","xxx","xxx","xxx","xxx","xxx"]

"""

def permute(string: str):
    
    if string == None or string[1:] == None:
        return ""
    
    for main_char in string:
        
        for perm_char in string[1:]:
            
            return main_char + permute(string[1:])
            
        
        
        
print(permute("abc"))
    
            
     