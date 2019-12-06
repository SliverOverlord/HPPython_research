"""
Author: Heecheon Park

Note: Run python3 1000x1000_mat_generator.py first before running this program.

Description: Read numbers from 1000x1000_matrix.txt

Store each line into lists and numpy arrays.

Then, benchmarks matrix multiplication.

For example, list A and list B are 2-dimensional lists and

performs list A * list B.

Likewise, numpy A and numpy B are 2-dimensional numpy arrays and

performs numpy A * numpy B.

I created a matrix multiplication function that takes 2 array-like containers and output array.

The function calculate and append the result to output array.
"""
import numpy as np
import time
import sys

from array import array
#from timeit import timeit
from timeit import Timer
from numba import njit

def main():
    
    list_mat = []
    list_mat2 = []

    # Initializing 1000x1000 list_matrix of zeros
    list_output = [[float(0) for col in range(1000)] for rows in range(1000)]

    with open("1000x1000_matrix.txt", "r") as f:
        for line in f:
            # Split each line as a list of string
            int_string_list = line.split()

            # Convert the string element to int or float
            #int_list = [int(i) for i in int_string_list]
            float_list = [float(i) for i in int_string_list]

            list_mat.append(float_list)
            list_mat2.append(float_list)


        f.close()


    """
        Timer function cannot take function parameter with arguments which is uncallable.
        However, using lambda can make the function parameter with arguments callable.
    """
    print("Calculation begins here.....")
    mat_mult(list_mat, list_mat2, list_output)

    #mat_mult2(list_mat, list_mat2, list_output)
    #print(list_output[999][999])

    #start_time = time.time()
    #numba_mat_mult(list_mat, list_mat2, list_output)
    #end_time = time.time()
    #print(type(output_mat[0][0]), "took","--- %s seconds ---" % (end_time - start_time))

    #print(np_output_double)

def mat_mult(mat1, mat2, output_mat):
    
    row = len(mat1)
    col = len(mat1[0])
    start_time = time.time()
    for r in range(0, row):
        for c in range(0, col):
            for r_iter in range(0, row):                
                output_mat[r][c] += mat1[r][r_iter] * mat2[r_iter][c] 
    
    end_time = time.time()
    print(type(output_mat[0][0]), "took","--- %s seconds ---" % (end_time - start_time))

    return output_mat

def mat_mult2(mat1, mat2, output_mat):
    zip_mat2 = zip(*mat2)

    start_time = time.time()
    output_mat = [[sum(elem_a * elem_b for elem_a, elem_b in zip(row_a, col_b)) for col_b in zip_mat2] for row_a in mat1]
    end_time = time.time()
    print(type(output_mat[0][0]), "took","--- %s seconds ---" % (end_time - start_time))

@njit
def numba_mat_mult(mat1, mat2, output_mat):
    
    row = len(mat1)
    col = len(mat1[0])
    for r in range(0, row):
        for c in range(0, col):
            for r_iter in range(0, row):                
                output_mat[r][c] += mat1[r][r_iter] * mat2[r_iter][c] 
    
    return output_mat

if __name__ == "__main__":
    main()
