// Author:Joshua DeNio
// Date: 8/8/19

#include <iostream>
#include <string>
#include <fstream>
#include <chrono>

using namespace std;

void mat_mult(double mat1[1000][1000], double mat2[1000][1000], double output_mat[1000][1000]);

int main(){
    static double list_mat[1000][1000];
    static double list_mat2[1000][1000];
    static double output_mat[1000][1000];
    
    int currentTime;
    
    int rowCount = 0;
    int colCount = 0;
    
    ifstream inFile("1000x1000_matrix.txt");
    if (inFile.is_open()){
        
        for (int i = 0; i < 1000; i++){
            //
            for (int j =0; j < 1000; j++){
                inFile >> list_mat[i][j];
            }
        }
    }
    inFile.close();
    
    ifstream inFile2("1000x1000_matrix.txt");
    if (inFile2.is_open()){
        
        for (int i = 0; i < 1000; i++){
            //
            for (int j =0; j < 1000; j++){
                inFile2 >> list_mat2[i][j];
            }
        }
    }
    inFile2.close();
    
    //for (int i = 0; i < 1000; i++){
    //    mat_mult(list_mat, list_mat2, output_mat);
    //}
    
    mat_mult(list_mat, list_mat2, output_mat);
    cout << "output matrix (truncated)" << endl;
    cout << output_mat[0][0] << endl;
    cout << output_mat[999][999] << endl;
    
    return 0;
}

void mat_mult(double mat1[1000][1000], double mat2[1000][1000], double output_mat[1000][1000]){
    
    int row = 1000;
    int col = 1000;
    
    auto startTime = chrono::high_resolution_clock::now();
    
    for (int r = 0; r < row; r++){
        for (int c = 0; c < col; c++){
            for (int r_iter = 0; r_iter < row; r_iter++){                
                output_mat[r][c] += mat1[r][r_iter] * mat2[r_iter][c];
            }
        }
    }
    
    auto endTime = chrono::high_resolution_clock::now();
    chrono::duration<double> timeElapsed = endTime - startTime;
    
    cout << "Matrix multiplication of two" << endl;
    cout << "Double matrix of type matrix[1000][1000]" << endl;
    cout << "\n";
    
    cout << "The processing time is: ";
    cout << timeElapsed.count() << " in seconds" << endl;
}
