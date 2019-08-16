/*
Name: Heecheon Park
Description: EgMandelbrot.java in C version
*/


#include <stdio.h>

int main()
{
    //int N = 38;
    int N = 50;
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

          // z = c + z * z

          double newr = cr + zr * zr - zi * zi ;
          double newi = ci + 2 * zr * zi ;

          zr = newr ;
          zi = newi ;
        }
     }
     printf("%d\n",N);
     for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++) {
        printf("%c ", set[i][j]);
        if (j == N-1)
        printf("\n");
      }



    return 0;
}
