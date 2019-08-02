#Author: Joshua DeNio
#Date: 7/31/2019
#Description: This program demenstrates using send() and recv() using mpi4py

from mpi4py import MPI

#set comm,size and rank
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
row = 4
col = 4
recData = [0,0,0,0]

def main():
    #the master does its stuff first
    if rank == 0:
        #
        sendData = 2
        comm.send(sendData, dest = 1, tag = 13)
        
        print("\n")
        print("Data from processor ", rank, ": ", sendData)
        print("\n")
    #the clients now do their part
    else:
        
        comm.recv(recData, source = 0, tag = 13)

        print("\n")
        print("Data from processor ", rank, ": ", recData)
        print("\n")
        
if __name__ == "__main__":
    main()
