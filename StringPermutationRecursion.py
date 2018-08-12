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
    
    print("string %s" %(string))
    
    out = []
     
    if len(string) == 1:
        out = [string]
    
   
    else:
        
        for index,char in enumerate(string):
            
            print("char %s" %(char))
            
            tmp_holder = \
            string[:index] + string[index + 1:]
            
#            print(
#                    "string[:%s] %s" %(index , string[:index]
#                    ))
#            print(
#                    "string[%s + 1:] %s" %(
#                            index,string[index + 1:]
#                            )
#                    )
            
            print(
                    "tmp_holder %s" %(tmp_holder
                    ))
            
            for elem in permute(tmp_holder):
                
                out += [char + elem]
            
    return out
        
    
        
print(permute("abc"))
    
            
     