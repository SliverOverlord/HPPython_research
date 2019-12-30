#include <stdio.h>

/*
This file is experimental to implement matrix multiplication (1d)
to be called from Python.

Build:
    $gcc -shared -o c_pylib.so -fPIC c_pylib.c
*/


void matmul(double* matA, int rowA, int colA, 
            double* matB, int rowB, int colB, 
            double* matC, int rowC, int colC) 
{
    for (int i = 0; i < rowA; i++) {
        for (int j = 0; j < colB; j++) {
            double sum = 0.0;
            for (int k = 0; k < rowB; k++)
                sum = sum + matA[i * colA + k] * matB[k * colB + j];
            matC[i * colC + j] = sum;
        }
    }
}
