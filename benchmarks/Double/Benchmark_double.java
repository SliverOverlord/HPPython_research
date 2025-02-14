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

public class Benchmark_double {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        
        int row = 1000;
        int col = 1000;
        double[][] mat_double = new double[row][col];
        double[][] mat_double2 = new double[row][col];
        double[][] mat_double_output = new double[row][col];

        //FileInputStream fis = new FileInputStream("100x100_matrix.txt");
        //BufferedInputStream bis = new BufferedInputStream(fis);

        //double buf[];
        //int i = 0;
        //int content;
        //int row_iter = 0;
        //int col_iter = 0;
        //while ((content = bis.read()) != -1)
        //{
            //System.out.print((char) content);
            //mat_double[row_iter][col_iter] = (double) content;
            //if (col_iter % 100 == 0)
            //{
            //    row_iter++;
            //    col_iter = 0;
            //}
            //col_iter++;
        //}
        //System.out.println(Arrays.deepToString(mat_double));

        //for (int r = 0; r < row; r++)
        //    
        //    for (int c = 0; c < col; c++)
        //    {
        //        mat_double[r][c] = buf[iterator];
        //        iterator++;
        //    }       

        //fis.close();

        Scanner sc = new Scanner(new BufferedReader(new FileReader("1000x1000_matrix.txt")));
        while(sc.hasNextLine()) {
         for (int i=0; i<mat_double.length; i++) {
            String[] line = sc.nextLine().trim().split(" ");
            for (int j=0; j<line.length; j++) {
               mat_double[i][j] = Double.parseDouble(line[j]);
               mat_double2[i][j] = Double.parseDouble(line[j]);
               mat_double_output[i][j] = 0;
            }
         }
        }

        mat_mult_double(mat_double, mat_double2, mat_double_output);
        System.out.println("mat_double_output (truncated)");
        System.out.println(mat_double_output[0][0]);
        System.out.println(mat_double_output[0][1]);
        System.out.println(mat_double_output[0][2]);
        System.out.println(mat_double_output[0][3]);
        System.out.println(mat_double_output[0][4]);
        System.out.println(mat_double_output[999][995]);
        System.out.println(mat_double_output[999][996]);
        System.out.println(mat_double_output[999][997]);
        System.out.println(mat_double_output[999][998]);
        System.out.println(mat_double_output[999][999]);

        //for (int i = 0; i < 100; i++)
        //{
        //    mat_mult_double(mat_double, mat_double2, mat_double_output);
        //}
    }

    public static void mat_mult_double(double[][] mat1, double[][] mat2, double[][] output_mat_double)
    {
        //row = mat1.length;
        //col = mat1[0].length;
        //DecimalFormat df = new DecimalFormat("#0.00000000");
        int row = 1000;
        int col = 1000;
        long startTime = System.nanoTime();
        for (int r = 0; r < row; r++)
            for (int c = 0; c < col; c++)
                for (int r_iter = 0; r_iter < row; r_iter++)
                    output_mat_double[r][c] += mat1[r][r_iter] * mat2[r_iter][c];
        long endTime = System.nanoTime();
        System.out.println("Matrix multiplication of two");
        System.out.println("Double matrix of type matrix[1000][1000]");
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
