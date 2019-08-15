// Author:Joshua DeNio
// Date: 8/8/19

#include <iostream>
#include <string>
#include <fstream>
#include <chrono>

using namespace std;


const int rowCount = 1000;
const int colCount = 1000;

string txtFile = "1000x1000_matrix.txt";

static void mat_mult(int mat1[rowCount][colCount], int mat2[rowCount][colCount], int output_mat[rowCount][colCount]);

int main(){
    
    static int list_mat[rowCount][colCount];
    static int list_mat2[rowCount][colCount];
    static int output_mat[rowCount][colCount];
    
    
    ifstream inFile(txtFile);
    if (inFile.is_open()){
        
        for (int i = 0; i < rowCount; i++){
            //
            for (int j =0; j < colCount; j++){
                inFile >> list_mat[i][j];
            }
        }
    }
    inFile.close();
    
    ifstream inFile2(txtFile);
    if (inFile2.is_open()){
        
        for (int i = 0; i < rowCount; i++){
            //
            for (int j =0; j < colCount; j++){
                inFile2 >> list_mat[i][j];
            }
        }
    }
    inFile2.close();
    /*
    for (int i = 0; i < 100; i++){
        mat_mult(list_mat, list_mat2, output_mat);
    }
    */
    mat_mult(list_mat, list_mat2, output_mat);
    
    return 0;
}

void mat_mult(int mat1[rowCount][colCount], int mat2[rowCount][colCount], int output_mat[rowCount][colCount]){
    
    //Start timer
    auto startTime = chrono::high_resolution_clock::now();
    
    for (int r = 0; r < rowCount; r++){
        for (int c = 0; c < colCount; c++){
            for (int r_iter = 0; r_iter < rowCount; r_iter++){                
                output_mat[r][c] += mat1[r][r_iter] * mat2[r_iter][c];
            }
        }
    }
    
    //End timer
    auto endTime = chrono::high_resolution_clock::now();
    chrono::duration<double> timeElapsed = endTime - startTime;
    
    cout << "Matrix multiplication of two" << endl;
    cout << "Integer matrix of type matrix[" << rowCount << "][" << colCount << "]" << endl;
    cout << "\n";
    
    cout << "The processing time is: ";
    cout << timeElapsed.count() << " in seconds" << endl;
}
