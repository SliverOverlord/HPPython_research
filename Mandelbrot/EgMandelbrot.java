/*
 * Example code from "Parallel Programming in HPJava".
 * Chapter: More on Mapping Arrays
 * Section: Other Distribution Formats
 * Figure: Mandelbrot set computation.
 */


public class EgMandelbrot {

  public static void main(String [] args) {

    int N = 38 ;
    int CUTOFF = 100 ;

    char [][] set = new char [N][N] ;

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
     System.out.println(N);
     for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++) {
        System.out.print(set[i][j] + " ");
        if (j == N-1)
          System.out.println();   
      }
  }
}
