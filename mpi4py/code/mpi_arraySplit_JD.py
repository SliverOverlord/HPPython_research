#Author: Joshua DeNio
#Date: 7/31/2019
#Description: This program tests splitting an array using mpi4py

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    #populate the array
    sendData = numpy.arange(16,dtype = numpy.int64)
    comm.send(sendData, dest = 1, tag = 13)
    #sendData = comm.scatter(sendData, root = 0)
    print("Data from processor ", rank, ": ", sendData)
else:
    recData = numpy.empty(16, dtype = numpy.int64)
    comm.recv(recData, source = 0, tag = 13)

    #recData = comm.gather(recData, root = 0)
    print("Data from processor ", rank, ": ", recData)
   
   
