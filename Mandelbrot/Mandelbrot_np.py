"""
Name: Heecheon Park
Description: EgMandelbrot.java in Python version
"""

import numpy as np
import sys
import time

def main():
    
    N = 100;
    #N = 38
    CUTOFF = 100

    #char_set = np.chararray((N, N), unicode=True, order='C')
    char_set = np.chararray((N, N), unicode=True)
    #char_set = np.array(dtype=string)
    #char_set = np.zeros((38,38))

    char_set[:] = None
    np.set_printoptions(threshold=sys.maxsize)
    print(char_set)

    ndarrayStore_startTime = time.time()
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

    ndarrayStore_endTime = time.time()

    print(N) 

    ndarrayAccess_startTime = time.time()
    for i in range(N):
        for j in range(N):
            print(char_set[i][j], end=" ")
            if j == (N-1):
                print()
    ndarrayAccess_endTime = time.time()

    print("Ndarray store time: %s seconds" % (ndarrayStore_endTime - ndarrayStore_startTime)) 
    print("list access time: %s seconds" % (ndarrayAccess_endTime - ndarrayAccess_startTime)) 

if __name__ == "__main__":
    main()
