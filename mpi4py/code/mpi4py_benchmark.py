#Author: Joshua DeNio
#Date: 8/6/2019
#Description: This program benchmarks numpy matrix
#   multiplication vs standard python

from mpi4py import MPI
import random
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
    
    matrixList1 = [[] for x in range(0,100)]
    matrixList2 = [[] for x in range(0,100)]
    
    row = 100
    col = 100
    
    #the master does its work first
    if rank == 0:
        try:
            #try to open the files
            openFile("data1.txt")
            openFile("data2.txt")
        
        except:
        
            #call makeData to make data1.txt and data2.txt
        
            makeData("data1.txt")
            makeData("data2.txt")
        
        

        #format array to matrix 100x100
        matrix1 = matrix1.reshape(100,100)
        matrix2 = matrix2.reshape(100,100)
        
def openFile(fileName):
    #open textfiles
    f1 = open(data1.txt, 'r')
        
    #import data from data2.txt
    #save to matrix2

    rowCount = 0
    colCount = 0
            
    #import data from data1.txt
    for line in f1.readlines():
        #split on ,
        for i in line.split(","):
            #insert value into the matrix
            matrixList1[rowCount][colCount] = i
            colCount += 1
            rowCount +=1
    f1.close()

def makeData(fileName):
    #code to populate a txtfile with random numbers
    f = open(fileName, "w")
    
    #counter
    count = 0
    numCounter = 0
    lines = 0
    
    while count < 100*100:
        if numCounter == 99:
            numCounter = 0
            
            f.write(str(random.randrange(10))+",")
            f.write("\n")
            lines += 1
            count += 1
        else:
            f.write(str(random.randrange(10))+",")
            numCounter += 1
            count += 1
            
    f.close()
    print(fileName + " created");
    
def multiplyMatrixNumpy(matrix1, matrix2):
    result = numpy.empty(10000, dtype = numpy.int64).reshape(100,100)
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
def multiplyMatrixList(matrix1, matrix2):
    #set result matrix to empty
    result = [[] for x in range(0,100)]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

                

if __name__ == "__main__":
    main()
