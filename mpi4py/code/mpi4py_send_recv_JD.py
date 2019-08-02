#Author: Joshua DeNio
#Date: 7/31/2019
#Description: This program demenstrates using send() and recv() using mpi4py

from mpi4py import MPI

#set comm,size and rank
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def main():
    #the master does its stuff first
    if rank == 0:
        #make an object
        data = "Test Data"
        
        #send the object
        comm.send(data, dest = 1, tag = 11)
        
        #print the object that was sent
        print("\n")
        print("Data from processor "+ str(rank) + ": ", data)
        print("\n")
        
    #the clients now do their part
    elif rank == 1:
        
        #Receive the object
        data = comm.recv(source = 0, tag = 11)

        #print the object received
        print("\n")
        print("Data from processor "+ str(rank) + ": ", data)
        print("\n")
        
if __name__ == "__main__":
    main()
