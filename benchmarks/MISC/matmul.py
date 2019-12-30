"""
Author: Heecheon Park

Description: Python program to call matmul function from C program. (Experimental)

Disclaimer:

I am still in learning process as to what would be the best way to
improve the performance of matrix multiplication in Python using lists (rather numpy's ndarray)

Although numpy library provides the most efficient implementation of math and science related operations
in Python, numpy array tends to be much slower when interacting with user-define functions.

It is noteworthy if calling a function from C into Python elicits improvement in performance.
"""

import ctypes as C

_c_pylib = C.CDLL("c_pylib.so")
_c_pylib.matmul.argtypes = (C.POINTER(C.c_double), C.c_int, C.c_int, \
                    C.POINTER(C.c_double), C.c_int, C.c_int, \
                    C.POINTER(C.c_double), C.c_int, C.c_int)

def main():
    
    mat1 = [float(i) for i in range(1, 10)]
    mat2 = [float(i) for i in range(1, 10)]
    output_mat = [0 for i in range(1,10)]

    result =  matmul(mat1, 3, 3, \
              mat2, 3, 3, \
              output_mat, 3, 3)

    # Cannot "print(result)" because result is not a list
    # but a ctypes double*.
    print(type(result))

    #for elem in result:
    #    print(elem)

    for i in range(len(result)):
        if ((i + 1) % 3) == 0:
            print(result[i])
        else:
            print(result[i], end=" ")

def matmul(matA, rowA, colA,\
           matB, rowB, colB,\
           output_mat, rowC, colC):

    global _c_pylib
    mat_size = len(output_mat)

    mat1 = (C.c_double * len(matA))(*matA)
    mat2 = (C.c_double * len(matB))(*matB)
    mat3 = (C.c_double * len(output_mat))(*output_mat)

    _c_pylib.matmul(mat1, rowA, colA, \
                    mat2, rowB, colB, \
                    mat3, rowC, colC)

    return mat3

if __name__ == "__main__":
    main()
