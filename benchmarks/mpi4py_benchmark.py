#Author: Heecheon Park
#Date: 8/11/2019
"""
#Description: This program benchmarks numpy matrix
   multiplication vs standard python on mpi4py
Read numbers from 100x100_matrix.txt
Store each line into lists and numpy arrays.
Then, benchmarks matrix multiplication.
For example, list A and list B are 2-dimensional lists and
performs list A * list B.
Likewise, numpy A and numpy B are 2-dimensional numpy arrays and
performs numpy A * numpy B.
I created a matrix multiplication function that takes 2 array-like containers and output array.
The function calculate and append the result to output array.

Note: Run python3 100x100_mat_generator.py first before running this program.
"""

from mpi4py import MPI
import timeit
import numpy
import sys

from array import array
from timeit import Timer

#set comm,size and rank
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def main():
    if rank == 0:
        list_mat = []
        list_mat2 = []
        np_mat = numpy.zeros((100,100), dtype=numpy.int64)
        np_mat2 = numpy.zeros((100,100), dtype=numpy.int64)
    
        # Initializing 100x100 list_matrix of zeros
        list_output = [[0 for col in range(100)] for rows in range(100)]
        np_output = numpy.zeros((100,100), dtype=numpy.int64)

        with open("100x100_matrix.txt", "r") as f:
            for line in f:
                # Split each line as a list of string
                int_string_list = line.split()

                # Convert the string element to int
                int_list = [int(i) for i in int_string_list]

                # Append the int_list to list_mat and list_mat2
                list_mat.append(int_list)
                list_mat2.append(int_list)

                #array_mat.append(array.fromlist(int_list))
                #array_mat2.append(array.fromlist(int_list))

            f.close()
        
        np_mat = numpy.loadtxt("100x100_matrix.txt", usecols=range(0, 100), dtype=numpy.int64)
        np_mat2 = numpy.loadtxt("100x100_matrix.txt", usecols=range(0, 100), dtype=numpy.int64)

        #print("list_mat: ", list_mat)
        #the above line has been commented out for readability-----------------------

        # Print large numpy arrays without truncation.
        numpy.set_printoptions(threshold=sys.maxsize)
        #print("np_mat: \n", np_mat)
        #the above line has been commented out for readability-----------------------
    
        list_timer = Timer(lambda: mat_mult(list_mat, list_mat2, list_output))
        ndarray_timer = Timer(lambda: mat_mult(np_mat, np_mat2, np_output))
        built_in_mult_timer = Timer(lambda: numpy.matmul(np_mat, np_mat2, np_output))

        print("*"*80)
    
        print("How many times would you like to perform the matrix multiplication?")
        print("I recommend a small number less than 50: ")
        iteration_count = int(input())
        print("*"*80)
        print('Custom Mat_Multiplication {} times (list):'.format(iteration_count), list_timer.timeit(number=iteration_count))
        print('Custom Mat_Multiplication {} times (ndarray):'.format(iteration_count), ndarray_timer.timeit(number=iteration_count))
        print('Numpy Built-in Mat_Multiplication {} times (array):'.format(iteration_count), built_in_mult_timer.timeit(number=iteration_count))


def mat_mult(mat1, mat2, output_mat):
    
    row = len(mat1)
    col = len(mat1[0])

    for r in range(0, row):
        for c in range(0, col):
            for r_iter in range(0, row):                
                output_mat[r][c] += mat1[r][r_iter] * mat2[r_iter][c] 

    return output_mat


if __name__ == "__main__":
    main()
