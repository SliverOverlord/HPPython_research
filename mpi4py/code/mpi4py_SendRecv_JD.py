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
        comm.Send(sendData, dest = 1, tag = 13)
        
        print("\n")
        print("Data from processor ", rank, ": ", sendData)
        print("\n")
    #the clients now do their part
    else:
        #receiving on the client nodes
        comm.Recv(recData, source = 0, tag = 13)

        #recData = comm.gather(recData, root = 0)

        print("\n")
        print("Data from processor ", rank, ": ", recData)
        print("\n")
#a function to print the matrix
#def printMatrix(matrix):
    #count = 0
    #rowC = 0
    #colC = 0
    #while count < row*col:
        #for i in range(0, row * col):
            #print
        #count += 1
if __name__ == "__main__":
    main()
