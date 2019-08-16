/*
Name: Heecheon Park
Description: EgMandelbrot.java in C++ version
*/

#include <iostream>

using namespace std;


int main()
{
    int N = 38;
    int CUTOFF = 100;

    char set[N][N];


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
     cout << N << endl;
     for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++) {
        cout << set[i][j] << " ";
        if (j == N-1)
        cout << endl;
      }



    return 0;
}
