"""
Name: Heecheon Park
Description: EgMandelbrot.java in Python version
"""

import numpy as np
import time

def main():
    
    N = 100;
    CUTOFF = 100;

    char_set = [[None for i in range(N)] for j in range(N)]

    print(char_set)
    listStore_startTime = time.time()
    for i in range(N):
        for j in range(N):
            cr = (4.0 * i - 2 * N) / N
            ci = (4.0 * j - 2 * N) / N
            zr = cr
            zi = ci

            char_set[i][j] = ' '


            k = 0
            while (zr * zr + zi * zi) < 4.0:
                if k == CUTOFF:
                    char_set[i][j] = '#'
                    break;
                k += 1

                #print(char_set[i][j], end=" ")
                #if j == (N-1):
                #    print()

                newr = cr + zr * zr - zi * zi
                newi = ci + 2 * zr * zi

                zr = newr
                zi = newi

    listStore_endTime = time.time()

    print(N) 

    listAccess_startTime = time.time()
    for i in range(N):
        for j in range(N):
            print(char_set[i][j], end=" ")
            if j == (N-1):
                print()
    listAccess_endTime = time.time()

    print("list store time: %s seconds" % (listStore_endTime - listStore_startTime)) 
    print("list access time: %s seconds" % (listAccess_endTime - listAccess_startTime)) 

if __name__ == "__main__":
    main()
