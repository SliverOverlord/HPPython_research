// Author: Heecheon Park
// Description: 1000x1000 matrix multiplication benchmark program in C.
// Date: 8/14/19

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARR_SIZE 1000000
void mat_mult_1d(double* mat1, int mat1_row, int mat1_col, 
                 double* mat2, int mat2_row, int mat2_col,
                 double* output_mat, int output_mat_row, int output_mat_col);

int main(){
    double* list_mat = (double*) malloc(ARR_SIZE * sizeof(double));
    double* list_mat2 = (double*) malloc(ARR_SIZE * sizeof(double));
    double* output_mat = (double*) malloc(ARR_SIZE * sizeof(double));
    
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

    for (int i = 0; i < ARR_SIZE; i++)    
        fscanf(fp, "%lf", &list_mat[i]);
        
           
    for (int i = 0; i < ARR_SIZE; i++)    
        fscanf(fp2, "%lf", &list_mat2[i]);
        
    fclose(fp);   
    fclose(fp2);
    
    mat_mult_1d(list_mat, 1000, 1000, list_mat2, 1000, 1000, output_mat, 1000, 1000);
    
    printf("output_mat (truncated) \n");
    printf("%lf\n", output_mat[0]);
    printf("%lf\n", output_mat[1]);
    printf("%lf\n", output_mat[2]);
    printf("%lf\n", output_mat[3]);
    printf("%lf\n", output_mat[4]);
    printf("%lf\n", output_mat[ARR_SIZE-5]);
    printf("%lf\n", output_mat[ARR_SIZE-4]);
    printf("%lf\n", output_mat[ARR_SIZE-3]);
    printf("%lf\n", output_mat[ARR_SIZE-2]);
    printf("%lf\n", output_mat[ARR_SIZE-1]);

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

void mat_mult_1d(double* mat1, int mat1_row, int mat1_col, 
                 double* mat2, int mat2_row, int mat2_col,
                 double* output_mat, int output_mat_row, int output_mat_col)
{

    clock_t startTime = clock();
    for (int i = 0; i < mat1_row; i++) {
        for (int j = 0; j < mat2_col; j++) {
            double sum = 0.0;
            for (int k = 0; k < mat2_row; k++)
                sum = sum + mat1[i * mat1_col + k] * mat2[k * mat2_col + j];
            output_mat[i * output_mat_col + j] = sum;
        }
    }
    clock_t endTime = clock();
    double timeElapsed = (double) (endTime - startTime) / CLOCKS_PER_SEC;
    printf("Matrix multiplication of two\n");
    printf("Double matrix of type matrix[1000][1000]\n");
    
    printf("\nThe processing time is: ");
    printf("%lf in seconds\n", timeElapsed);
}
