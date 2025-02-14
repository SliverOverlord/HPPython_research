/*
Name: Heecheon Park

This standalone java program read matrix from 1000x1000_matrix.txt

and performs a matrix multiplication.

Then, it measures how fast it calculates to compare with C++ and Python implementation on a single processor.

*/
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.File;
import java.io.FileReader;
import java.util.Scanner;
import java.lang.System;
import java.util.Date;
import java.text.DecimalFormat;
//import java.io.FileInputStream;
//import java.io.BufferedInputStream;
//import java.util.Arrays;
//import java.util.concurrent.TimeUnit;

public class Benchmark_float {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        
        int row = 1000;
        int col = 1000;
        float[][] mat_float = new float[row][col];
        float[][] mat_float2 = new float[row][col];
        float[][] mat_float_output = new float[row][col];


        Scanner sc = new Scanner(new BufferedReader(new FileReader("1000x1000_matrix.txt")));
        while(sc.hasNextLine()) {
         for (int i=0; i<mat_float.length; i++) {
            String[] line = sc.nextLine().trim().split(" ");
            for (int j=0; j<line.length; j++) {
               mat_float[i][j] = Float.parseFloat(line[j]);
               mat_float2[i][j] = Float.parseFloat(line[j]);
               mat_float_output[i][j] = 0;
            }
         }
        }

        mat_mult_float(mat_float, mat_float2, mat_float_output);
        System.out.println("mat_float_output (truncated)");
        System.out.println(mat_float_output[0][0]);
        System.out.println(mat_float_output[0][1]);
        System.out.println(mat_float_output[0][2]);
        System.out.println(mat_float_output[0][3]);
        System.out.println(mat_float_output[0][4]);
        System.out.println(mat_float_output[999][995]);
        System.out.println(mat_float_output[999][996]);
        System.out.println(mat_float_output[999][997]);
        System.out.println(mat_float_output[999][998]);
        System.out.println(mat_float_output[999][999]);

        //for (int i = 0; i < 100; i++)
        //{
        //    mat_mult_double(mat_double, mat_double2, mat_double_output);
        //}
    }

    public static void mat_mult_float(float[][] mat1, float[][] mat2, float[][] output_mat_float)
    {
        int row = 1000;
        int col = 1000;
        long startTime = System.nanoTime();
        for (int r = 0; r < row; r++)
            for (int c = 0; c < col; c++)
                for (int r_iter = 0; r_iter < row; r_iter++)
                    output_mat_float[r][c] += mat1[r][r_iter] * mat2[r_iter][c];
        long endTime = System.nanoTime();
        System.out.println("Matrix multiplication of two");
        System.out.println("Float matrix of type matrix[1000][1000]");
        System.out.println("The processing time is: " + (endTime - startTime)/1000000000.0 + " seconds");
       
    }

    public static void print_mat (double[][] mat, int row, int col ) 
    {
        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
                System.out.println(mat[i][j]);
            System.out.println();
        }    
                
    }

 }
