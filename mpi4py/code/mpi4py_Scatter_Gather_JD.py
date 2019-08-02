#Author: Joshua DeNio
#Date: 7/31/2019
#Description: This program demenstrates using Send() and Recv() using mpi4py

from mpi4py import MPI
import numpy

#set comm,size and rank
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
row = 4
col = 4

#initialize recData as an empty numpyarray of the correct size
recData = numpy.empty(16, dtype = numpy.int64)

def main():
    #the master does its stuff first
    if rank == 0:
        #populate the array
        sendData = numpy.arange(16,dtype = numpy.int64)
        
        sendData = comm.Scatter(sendData, root = 0)
        print("\n")
        print("Data from processor ", rank, ": ", sendData)
        print("\n")
    #the clients now do their part
    else:
        #receiving on the client nodes
        
        recData = comm.Gather(recData, root = 0)

        print("\n")
        print("Data from processor ", rank, ": ", recData)
        print("\n")
#a function to print the matrix
#def printMatrix(matrix):
    #getDigit = lambda: len(str(max(mat)))
    #maxDigit = getDigit()
    #j = 0
    #for i in range(1, row * col +1):
        ##print("{0:{width}}".format(matrix[j], width = maxDigit), " ", end = "")
        
        #if ((i%col == 0) or (i == row * col)):
            #print("")
        #j += 1
    #for i in range(0, row * col):
        #print"
if __name__ == "__main__":
    main()
