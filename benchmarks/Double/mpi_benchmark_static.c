// Author: Heecheon Park
// Description: 1000x1000 matrix multiplication benchmark program in C with MPI.
// Date: 8/30/19

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>
#include <assert.h>

void mat_mult(double mat1[1000][1000], double mat2[1000][1000], double output_mat[1000][1000]);
void printMat(double mat[1000][1000], int, int);

#define MASTER 0

int main(){
    static double list_mat[1000][1000];
    static double list_mat2[1000][1000];
    static double output_mat[1000][1000];
    
    int rowCount = 0;
    int colCount = 0;

    FILE *fp, *fp2;
    fp = fopen("1000x1000_matrix.txt", "r");
    fp2 = fopen("1000x1000_matrix.txt", "r");
    
    if ((fp == NULL) || (fp2 == NULL))
    {
        fprintf(stderr, "File not found!\n");
        exit(-1);
    }

    for (int i = 0; i < 1000; i++)    
        for (int j =0; j < 1000; j++)
            fscanf(fp, "%lf", &list_mat[i][j]);
        
           
    for (int i = 0; i < 1000; i++)    
        for (int j =0; j < 1000; j++)
            fscanf(fp2, "%lf", &list_mat2[i][j]);
        
    fclose(fp);   
    fclose(fp2);
    printf("Checking the initial matrix.\n");
    printf("====================================\n");
    printMat(list_mat, 1000, 1000);
    mat_mult(list_mat, list_mat2, output_mat);
    
    printf("output_mat (truncated) \n");
    printf("%lf\n", output_mat[0][0]);
    printf("%lf\n", output_mat[999][999]);

    return 0;
}

void mat_mult(double mat1[1000][1000], double mat2[1000][1000], double output_mat[1000][1000]){
    
    int row = 1000;
    int col = 1000;
    
    clock_t startTime = clock();
    
    for (int r = 0; r < row; r++){
        for (int c = 0; c < col; c++){
            for (int r_iter = 0; r_iter < row; r_iter++){                
                output_mat[r][c] += mat1[r][r_iter] * mat2[r_iter][c];
            }
        }
    }
    
    clock_t endTime = clock();
    double timeElapsed = (double) (endTime - startTime) / CLOCKS_PER_SEC;
    
    printf("Matrix multiplication of two\n");
    printf("Double matrix of type matrix[1000][1000]\n");
    
    printf("\nThe processing time is: ");
    printf("%lf in seconds\n", timeElapsed);
}

void printMat(double mat[1000][1000], int row, int col)
{
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
            printf("%.2f ", mat[i][j]);
        printf("\n");
    }
}
