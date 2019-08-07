#Author: Joshua DeNio
#Date: 8/6/2019
#Description: This program benchmarks numpy matrix
#   multiplication vs standard python

from mpi4py import MPI
import numpy

#set comm,size and rank
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def main():
    
    #initialize recData as an empty numpyarray of the correct size and sendData to null

    sendData = None
    matrix1 = numpy.empty(10000, dtype = numpy.int64)
    matrix2 = numpy.empty(10000, dtype = numpy.int64)
    
    matrixList1 = [[] for x in range xrange(0,100)]
    matrixList2 = [[] for x in range xrange(0,100)]
    
    row = 100
    col = 100
    
    #the master does its work first
    if rank == 0:
        try:
            #open textfiles
            
            #import data from data1.txt
            #save to matrix1
        
            #import data from data2.txt
            #save to matrix2
        
        except:
        
            #call makeData to make data1.txt and data2.txt
        
            makeData("data1.txt")
            makeData("data2.txt")
        
        

        #format array to matrix 100x100
        matrix1 = recData.reshape(100,100)
        matrix2 = recData.reshape(100,100)

def makeData(fileName):
    #code to populate a txtfile with random numbers
    f = open(fileName, "w")
    
    #counter
    count = 0
    numCounter = 0
    lines = 0
    
    while count < 100*100:
        if numCounter = 99:
            numCounter = 0
            f.write("\n")
        
        
    
    print(fileName, " created\n");
    
def multiplyMatrixNumpy(matrix1, matrix2):
    result = numpy.empty(10000, dtype = numpy.int64).reshape(100,100)
    
    for i in range(len(matrix1):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
def multiplyMatrixList(matrix1, matrix2):
    #set result matrix to empty
    result = [[] for x in range xrange(0,100)]
    
    for i in range(len(matrix1):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

                

if __name__ == "__main__":
    main()
