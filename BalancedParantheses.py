# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 01:36:22 2018

@author: sanooj
"""

"""
Balanced Parantheses

3 types
{}
[]
()

1. given a string of opening and closing parantheses
    check if balanced
2. every opening parantheses to be closed in reverse order
    opened

in: {[]}
out: balanced

in {[}]
out: un-balanced
"""

open_braces = \
[
  "{",
  "[",
  "("
 ]

closed_braces = \
[
  "}",
  "]",
  ")"
 ]

DEBUG = False

def debug_print(log: str , flag: bool = DEBUG):
    
    if flag:
        print(log)

def make_braces_order_dict(braces: list):
    
    order = 0
    
    order_dict = {}
    
    for brace in braces:
        
        order += 1
        
        order_dict[brace] = \
        order
        
    return order_dict

def balance_check(string: str):
    
    print("is_balanced %s" %(string))
    
    # opening and closing braces
    # given same number
    # dictionary for O(1) search
    
#    open_braces_order_dict = \
#    {
#      "{" : 1,
#      "[" : 2,
#      "(" : 3
#    }
    open_braces_order_dict = \
    make_braces_order_dict(open_braces)
    
#    closed_braces_order_dict = \
#    {
#      "}" : 1,
#      "]" : 2,
#      ")" : 3 
#    }
    closed_braces_order_dict = \
    make_braces_order_dict(closed_braces)
    
    debug_print("open_braces_order_dict")
    debug_print(open_braces_order_dict)
    debug_print("closed_braces_order_dict")
    debug_print(closed_braces_order_dict)
       
    from Stack import Stack
    
    # LIFO structure 
    # can use an array too
    stack = Stack()
    
    
    # lopp through all characters
    for char in string:
        
        debug_print("char")
        debug_print(char)
        
        debug_print("stack.items")
        debug_print(stack.items)
        debug_print(stack.peek())
        
        # check if opening or closing  braces
        order_in_open_braces = \
        open_braces_order_dict.get(char)
        
        # opening braces found
        if order_in_open_braces != None:
            
            #push to stack    
            stack.push(char)
        
        #closing braces of any other character
        else:
        
            # check if closing braces
            order_in_closed_braces = \
            closed_braces_order_dict.get(char)
            
            # not a closing braces
            if order_in_closed_braces == None:
                
                # perform the next loop iteration
                continue
            
            # Closing brace found
            
            # get the last elment of the stack
            # as the braces need to be closed in the
            # order opened
            order_of_last_element = \
            open_braces_order_dict.get(stack.peek())
            
            # last element in stack is matching the 
            # element
            if order_in_closed_braces == \
            order_of_last_element :
                
                # paprantheses match
                # so remove them
                debug_print("stack pop")
                debug_print(stack.pop())
            
            # order doesn't match
            # meaning parantheses are not balanced
            else:
                
                # break out of loop
                # break
                return False
                break
                
    
    return len(stack.items) == 0
    
    # stack should be empty 
    # if all braces match
    print("is_balanced %s" %(string))                
    print(len(stack.items) == 0)

def test_balanced_braces():     
#    print("balance_check")
#    str1 = "[ss(s)s]"
#    print(balance_check(str1))
#    str1 = "([]"
#    print(balance_check(str1))
#    str1 = "([)]"
#    print(balance_check(str1))
#    str1 = "[](){([[[]]])}"
#    print(balance_check(str1))
#    str1 = "()(){]}"
#    print(balance_check(str1))
    
    
    for string in [
            "{}",
            "}([[{)[]))]{){}[",
      "{]]{()}{])",
      "(){}",
      "{}{()}{{}}",
     '[](){([[[]]])}(',
        '[{{{(())}}}]((()))',
        '[[[]])]'
      ]:

        print(balance_check(string))
    
#    str1 = "}([[{)[]))]{){}["
#    print(balance_check(str1))        

test_balanced_braces()


def balance_checks_preferred(string: str):
    
    print(
            "is_balanced_balance_checks_preferred %s" 
            %(string)
            )
    
    from Stack import Stack
    
    # LIFO structure 
    # can use an array too
    chars = Stack()
    
    matches = \
    {
     ")" : "(" ,
     "]" : "[" ,
     "}" : "{" ,
     ">" : "<"
     }
    
    for char in string:
        
        if char in matches:
            
            if chars.pop() != matches[char]:
                
                return False
        else:
            
            chars.push(char)
            
    return chars.is_empty()




def test_balance_checks_preferred():     
#    print("balance_check")
#    str1 = "[ss(s)s]"
#    print(balance_check(str1))
#    str1 = "([]"
#    print(balance_check(str1))
#    str1 = "([)]"
#    print(balance_check(str1))
#    str1 = "[](){([[[]]])}"
#    print(balance_check(str1))
#    str1 = "()(){]}"
#    print(balance_check(str1))
    
    
    for string in [
            "{}",
            "}([[{)[]))]{){}[",
      "{]]{()}{])",
      "(){}",
      "{}{()}{{}}",
     '[](){([[[]]])}(',
        '[{{{(())}}}]((()))',
        '[[[]])]'
      ]:

        print(balance_checks_preferred(string))
    
#    str1 = "}([[{)[]))]{){}["
#    print(balance_check(str1))        

test_balance_checks_preferred()



def balance_checks_best_sln(string: str):
    
    print(string)
    
    # odd length check
    # odd -> unbalanced
    if len(string) % 2 != 0:
        return False
    
    opening = \
    set("([{")
    
    matches = \
    set(
        [
                ("(",")"),
                ("[","]"),
                ("{","}"),
        ]
        )
    
    stack = []
    
    
    for char in string:
        
        if char in opening:
            stack.append(char)
            
        else:
            
            # first char is a closing braces
            if len(stack) == 0:
                return False
            
            last_open = \
            stack.pop()
            
            if (last_open,char) not in matches:
                return False
            
    return len(stack) == 0
            
print("balance_checks_best_sln")  
print(balance_checks_best_sln("[]"))
print(balance_checks_best_sln(
        "[](){([[[]]])}"
        )
        )