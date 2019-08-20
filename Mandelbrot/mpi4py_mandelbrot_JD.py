#Author: Joshua DeNio, Heecheon park
#Date: 8/20/2019
#Contributers: This code is based on algorithms made by Dr Hanku Lee

#Description:
#   This program is a mpi4py implimentation of a mandelbrot set as a benchmark for mpi4py

from mpi4py import MPI
import time

#set comm, size, and rank
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def main():
    #set up variables
    num = 38
    cutoff = 100
    
    #set up the masters tasks
    if rank == 0:
        print("Time from master node")
        calcMandelbrot(num, cutoff)
    #set up the clients tasks
    elif rank == 1:
        print("Time from slave node")
        calcMandelbrot(num, cutoff)

def calcMandelbrot(n, cutoff):
    
    char_set = [[None for i in range(n)] for j in range(n)]
    
    startTime = time.time()
    
    for i in range(n):
        for j in range(n):
            cr = (4.0 * i - 2 * n) / n
            ci = (4.0 * j - 2 * n) / n
            zr = cr
            zi = ci
            
            char_set[i][j] = ' '
            
            k = 0
            
            while (zr * zr + zi * zi) < 4.0:
                if k == cutoff:
                    char_set[i][j] = '#'
                    break;
                k += 1
                new_r = cr + zr * zr - zi * zi
                new_i = ci + 2 * zr * zi
                
    endTime = time.time()
    
    print()
    print("The time to store to a list is:")
    print("%s seconds" % (startTime - endTime))
    
    
    startTime = time.time()
    
    for i in range(n):
        for j in range(n):
            print(char_set[i][j], end=" ")
            if j == (n - 1):
                print()
    endTime = time.time()
    
    print()
    print("The time to access the values in the list is:")
    print("%s seconds" % (startTime - endTime))
    
    
        
if __name__ == "__main__":
    main()
