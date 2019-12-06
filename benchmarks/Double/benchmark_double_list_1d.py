"""
Name: Heecheon Park
Date: September 6th 2019
Minnesota State University Moorhead

Running 1000x1000 matrix multiplication with list and mpi
with 5 processors.


Execution Method:

mpiexec -np 5 python3 mpi_list_matmult.py
"""
from mpi4py import MPI
from numba import njit, jit
import numpy as np
import sys
import time

MASTER = 0
ARR_SIZE = 1000000

def main():
        
    list_mat = []
    list_mat2 = []
    output_mat = [None] * ARR_SIZE

    with open("1000x1000_matrix.txt",'r') as f:
        for line in f:
            for data in line.split():
                list_mat.append(float(data))
                list_mat2.append(float(data))
    f.close()
    
    #print("list_mat", list_mat[ARR_SIZE-1])

    mat_mult_1d(list_mat, 1000, 1000, list_mat2, 1000, 1000, output_mat, 1000, 1000)
    
    #start_time = time.time()
    #numba_mat_mult_1d(list_mat, 1000, 1000, list_mat2, 1000, 1000, output_mat, 1000, 1000)
    #end_time = time.time()
    #print(type(output_mat[0]), "took","--- %s seconds ---" % (end_time - start_time))

#@njit
#def mat_mult(mat1, mat2, output_mat):
#    
#    row = len(mat1)
#    col = len(mat1[0])
#    #start_time = time.time()
#    for c in range(0, col):
#        for r in range(0, row):
#            for r_iter in range(0, col):                
#                output_mat[r][c] += mat1[r][r_iter] * mat2[r_iter][c] 
#    
#    #end_time = time.time()
#    #print(type(output_mat[0][0]), "took","--- %s seconds ---" % (end_time - start_time))
#
#    return output_mat

#@njit
def mat_mult_1d(mat1, mat1_row, mat1_col, mat2, mat2_row, mat2_col, output_mat, output_mat_row, output_mat_col):
    
    start_time = time.time()
    for i in range(mat1_row):
        for j in range(mat2_col):
            var_sum = float(0.0)
            for k in range(mat2_row):
                var_sum += mat1[i * mat1_col + k] * mat2[k * mat2_col + j]
            output_mat[i * output_mat_col + j] = var_sum
    end_time = time.time()
    print(type(output_mat[0]), "took","--- %s seconds ---" % (end_time - start_time))
    

@jit
def numba_mat_mult_1d(mat1, mat1_row, mat1_col, mat2, mat2_row, mat2_col, output_mat, output_mat_row, output_mat_col):
    
    for i in range(mat1_row):
        for j in range(mat2_col):
            var_sum = float(0.0)
            for k in range(mat2_row):
                var_sum += mat1[i * mat1_col + k] * mat2[k * mat2_col + j]
            output_mat[i * output_mat_col + j] = var_sum

if __name__ == "__main__":
    main()
