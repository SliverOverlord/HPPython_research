import numpy as np
import time
import sys

from array import array
#from timeit import timeit
from timeit import Timer

def main():
    
    np_mat_double = np.zeros((10,10), dtype=np.float64)
    np_mat_double2 = np.zeros((10, 10), dtype=np.float64)

    np_mat_double = np.loadtxt("10x10_matrix.txt", usecols=range(0, 10), dtype=np.float64)
    np_mat_double2 = np.loadtxt("10x10_matrix.txt", usecols=range(0, 10), dtype=np.float64)

    np_output_double = np.zeros((10, 10), dtype=np.float64)

    # Print large numpy arrays without truncation.
    #np.set_printoptions(threshold=sys.maxsize)
    #print("np_mat: \n", np_mat)

    print("Calculation begins here.....")
    #mat_mult(np_mat_double, np_mat_double2, np_output_double)

    start_time = time.time()
    np.matmul(np_mat_double, np_mat_double2, np_output_double)
    end_time = time.time()
    print("np.matmul (double) took {} seconds.".format(end_time - start_time))
    print(np_output_double)


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



if __name__ == "__main__":
    main()
