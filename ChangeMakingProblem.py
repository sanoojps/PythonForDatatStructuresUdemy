# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:29:57 2018

@author: sanooj
"""

"""

Change-Making problem

Given a target amount n and a list (array) 
of distinct coin values,
what's the fewest coins needed to make the change amount

n = 10
coins = [1,5,10]

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 

1 + 1 + 1 + 1 + 1 + 5

5 + 5

10

minimum number of coins = 1

"""


#def dynamicCoinChange( T:list, L:int ):
#
#	
#    Opt = [0 for i in range(0, L+1)]
#	
#    n = len(T)
#	
#    for i in range(1, L+1):
#        
#        smallest = float("inf")
#        
#        for j in range(0, n):
#            
#            if (T[j] <= i):
#                
#                smallest = min(smallest, Opt[i - T[j]]) 
#		
#        Opt[i] = 1 + smallest 
#	
#    print(Opt)
#    return Opt[L]
#
#print(dynamicCoinChange([1,5,10],9))
    

def coin_change(coins: list = [1,5,10], change: int = 9):
    
    options = \
    [0 for i in range( 0, change + 1)]
    
    coin_count = \
    len(coins)
    
    for index in range(1,change + 1):
        
        smallest = float("inf")
        
        for coin_index in range(0,coin_count):
            
            if coins[coin_index] <= index :
                
                tmp_options = \
                options[ index - coins[coin_index] ]
                
                smallest = \
                min(
                        smallest, 
                        tmp_options
                        )
                
        options[ index ] = 1 + smallest
        
    return options[ change ]
        
                
print(coin_change([1,5,10],109))
# 10 * 10 = 100 5 * 3 = 15 1 * 4 = 4 = 119
    