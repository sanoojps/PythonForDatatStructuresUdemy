# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:06:37 2018

@author: sanooj
"""



def longestEvenWord():
    
    sentense: str = "Your can do it they waya youa like"
    
    wordArray = sentense.split(" ")
    
    longestWord = wordArray[0]
    
    for word in wordArray:
        
        if len(word) % 2 == 0:
            print(word)
            if len(word) > len(longestWord):
                longestWord = word
    
    return longestWord

#print(longestEvenWord())


def longestEvenWordAlt():
    
    #sentense: str = "You can doi iit the way you like"
    sentense: str = "You can like"
    
    longestWord = ""
    
    substring = ""
    
    for char in sentense:
        if char == " ":
           if len(substring) % 2 == 0:
               if len(substring) > len(longestWord):
                   longestWord = substring
               substring = ""
           else:
               substring = ""
        else:
            substring += char
       
        #last word
    if len(substring) % 2 == 0:
           if len(substring) > len(longestWord):
               longestWord = substring
    
    return (longestWord if (len(longestWord) > 1 and len(longestWord) % 2 == 0) else "00")

print(longestEvenWordAlt())


def sockMerchant(n, ar):
    
    arrayCountDict = {};
    
    for element in ar:
        count =  arrayCountDict.get(element)
        if count == None:
            count = 1
            arrayCountDict[element] = count
        else:
            count = count + 1
            arrayCountDict[element] = count
            
    matchingPairCount = 0
    for key,count in arrayCountDict.items():
        if key !=0 and count >= 2:
            matchingPairCount = matchingPairCount + count // 2;
            
    return matchingPairCount

#print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sockMerchant(9,[4, 5, 5,5, 6, 6, 4, 1,4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]))
