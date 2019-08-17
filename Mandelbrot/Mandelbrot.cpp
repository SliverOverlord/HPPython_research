/*
Name: Heecheon Park
Description: EgMandelbrot.java in C++ version
*/

#include <iostream>
#include <chrono>

using namespace std;


int main()
{
    int N = 38;
    int CUTOFF = 100;

    char set[N][N];


    auto arrayStore_startTime = chrono::high_resolution_clock::now();
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++) {
        double cr = (4.0 * i - 2 * N) / N ;
        double ci = (4.0 * j - 2 * N) / N ;
        double zr = cr, zi = ci ;

        set [i][j] = ' ' ;


        int k = 0 ;
        while (zr * zr + zi * zi < 4.0) {
          if(k++ == CUTOFF) {
            set [i][j] = '#' ;
            break ;
          } 

        //cout << set[i][j] << " ";
        //if (j == N-1)
        //cout << endl;
           

        double newr = cr + zr * zr - zi * zi ;
        double newi = ci + 2 * zr * zi ;

        zr = newr ;
        zi = newi ;
        }
     }
    auto arrayStore_endTime = chrono::high_resolution_clock::now();
    chrono::duration<double> arrayStore_Time = arrayStore_endTime - arrayStore_startTime;
    cout << N << endl;
    auto arrayAccess_startTime = chrono::high_resolution_clock::now();
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++) {
        cout << set[i][j] << " ";
        if (j == N-1)
        cout << endl;
      }
    auto arrayAccess_endTime = chrono::high_resolution_clock::now();
    chrono::duration<double> arrayAccess_Time = arrayAccess_endTime - arrayAccess_startTime;


    cout << "Array store time: " << arrayStore_Time.count() << " seconds." << endl;
    cout << "Array access time: " << arrayAccess_Time.count() << " seconds." << endl;

    return 0;
}
