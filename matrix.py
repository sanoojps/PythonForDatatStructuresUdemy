# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 00:40:54 2018

@author: sanooj
"""

def print_a_matrix(
        rows:int, 
        columns:int,
        matrix:list
        ):
    
    # loop for rows
    for r_index in range(0,rows):
        
        # loop for column indexes
        for c_index in range(0, columns):
            
            # print
            print(
                    "matrix[%s][%s] = %s \n" \
                    %(r_index, \
                      c_index, \
                      matrix[r_index][c_index]
                      )
                )
            

def make_a_matrix(
        rows:int, 
        columns:int
        ):
    
    
    # matrix is an array within an array
    
    #primary array
    #serves as ROW
    matrix = []
    
    # loop for rows
    for r_index in range(0,rows):
        
        # inner array
        # serves as column
        columns_array = []
        
        # loop for column indexes
        for c_index in range(0, columns):
            
            columns_array.append(c_index)
            
        matrix.append(columns_array)
            
    print(matrix)
    
    print_a_matrix(rows,columns,matrix)
    
    return matrix
    
make_a_matrix(3,3)

"""
[ 
 1,2,3
 4,5,6
 7,8,9
 ]
"""

def make_incremented_matrix(
        rows:int, 
        columns:int
        ) -> list:
    
    
    # matrix is an array within an array
    
    #primary array
    #serves as ROW
    matrix = []
    
    current_increment = 0
    
    # loop for rows
    for r_index in range(0,rows):
        
        # inner array
        # serves as column
        columns_array = []
        
        # loop for column indexes
        for c_index in range(0, columns):
            
            current_increment = \
            current_increment + 1
            
            # add to column
            columns_array.append(current_increment)
        
        # add to row
        matrix.append(columns_array)
            
    print(matrix)
    
    print_a_matrix(rows,columns,matrix)
    
    return matrix
    
make_incremented_matrix(3,3)

"""
[ 
 1,2,3
 4,5,6
 7,8,9
 ]

in pythoon

[ [1,2,3], [4,5,6], [7,8,9] ]

transpose 

[ [1,4,7] , [2,5,8], [3,6,9] ]


[ 
 1,2
 3,4,
 5,6
 ] 3 x 2

in pythoon

[ [1,2], [3,4,], [5,6] ]

transpose  2 x 3

[ [1,3,5] , [2,4,6] ]


[ 
 1,2,3
 4,5,6
 ] 2 x 3

in pythoon

[ [1,2,3], [4,5,6] ]

transpose  3 x 2

[ [1,2,5] , [2,4,6] ]

"""
def get_transposed_matrix(
        rows:int, 
        columns:int,
        matrix
        ) -> list:
    
    
    # matrix is an array within an array
       
    print("orig_matrix")
    print(matrix)
    
    transposed_matrix = \
    make_a_matrix(columns,rows)
    
    print("transposed_matrix")
    print(transposed_matrix)

    # loop for row indexes
    for r_index in range(0,columns):
        
        # loop for column indexes
        for c_index in range(0,rows):
            
#            print(
#                    "transposed_matrix[%s][%s] = %s \n" \
#                    %(
#                            r_index,
#                            c_index,
#                            transposed_matrix[r_index][c_index]
#                            )
#                    )
#                    
#            print(
#                    "matrix[%s][%s] = %s \n" \
#                    %(
#                            c_index,
#                            r_index,
#                            matrix[c_index][r_index]
#                            )
#                    ) 
            
            transposed_matrix[r_index][c_index] = \
            matrix[c_index][r_index]
            
         
    #print(transposed_matrix)
    
    print_a_matrix(columns,rows,transposed_matrix)

#matrix = make_incremented_matrix(3,3)     
#get_transposed_matrix(3,3,matrix)

matrix = make_incremented_matrix(2,3)
get_transposed_matrix(2,3,matrix)

#matrix = make_incremented_matrix(3,2)
#get_transposed_matrix(3,2,matrix)