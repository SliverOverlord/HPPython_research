/*
Name: Heecheon Park
Description: EgMandelbrot.java in C version
*/


#include <stdio.h>
#include <time.h>

int main()
{
    int N = 38;
    //int N = 100;
    int CUTOFF = 100;

    char set[N][N];


    clock_t arrayStore_startTime = clock();
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
    clock_t arrayStore_endTime = clock();

    printf("%d\n",N);
    clock_t arrayAccess_startTime = clock();
    for (int i = 0; i < N; i++)
     for (int j = 0; j < N; j++) {
       printf("%c ", set[i][j]);
       if (j == N-1)
       printf("\n");
     }
    clock_t arrayAccess_endTime = clock();

    printf("Array store time: %lf\n", (double)(arrayStore_endTime - arrayStore_startTime) / CLOCKS_PER_SEC);
    printf("Array access time: %lf\n", (double)(arrayAccess_endTime - arrayAccess_startTime) / CLOCKS_PER_SEC);

    return 0;
}
