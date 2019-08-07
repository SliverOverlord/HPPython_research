import numpy as np
import time
import sys

from array import array

def main():
    
    list_mat = [[1,2,3],[4,5,6],[7,8,9]]
    list_mat2 = [[1,2,3],[4,5,6],[7,8,9]]
    np_mat = np.arange(1,10).reshape(3,3)
    np_mat2 = np.arange(1,10).reshape(3,3)
    list_output = [[0,0,0],[0,0,0],[0,0,0]]
    np_output = np.zeros((3,3), dtype='i')

    expectedOutput = [[30, 36, 42], [66, 81, 96] ,[102, 126, 150]]

    print("list_mat: ", list_mat)
    print("np_mat: \n", np_mat)

    print("Output (list):\n", mat_mult(list_mat, list_mat2, list_output))
    print("Output (ndarray):\n", mat_mult(np_mat, np_mat2, np_output))


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
