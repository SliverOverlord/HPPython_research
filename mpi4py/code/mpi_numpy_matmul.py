"""
Name: Heecheon Park
Date: September 6th 2019
Minnesota State University Moorhead

Running 1000x1000 matrix multiplication with numpy and mpi
with 5 processors.


Execution Method:

mpiexec -np 5 python3 np_scatter_and_gather.py
"""
from mpi4py import MPI
import numpy as np
import sys
import time

MASTER = 0

def main():
        
    COMM = MPI.COMM_WORLD
    RANK = COMM.Get_rank()
    SIZE = COMM.Get_size()

    row_split = 1000 / SIZE

    assert((1000 % row_split) == 0), "Row must be divisible by row_split!"
    row_split = int(row_split)
    #np.set_printoptions(threshold=sys.maxsize)
            
    np_mat = np.zeros((1000,1000), dtype=np.float64)
    np_mat2 = np.zeros((1000,1000), dtype=np.float64)
    local_np_mat = np.zeros((row_split,1000), dtype=np.float64) #container to receive data
    local_output_mat = np.zeros((row_split,1000), dtype=np.float64) #container to receive data
    #local_np_mat2 = np.zeros((1000,1000), dtype=np.float64) #container to receive data
    np_mat_gathered = np.zeros((1000,1000), dtype=np.float64) #container to gather data

    np_mat = np.loadtxt("1000x1000_matrix.txt", usecols=range(0, 1000), dtype=np.float64)
    np_mat2 = np.loadtxt("1000x1000_matrix.txt", usecols=range(0, 1000), dtype=np.float64)

    #np_mat = np.zeros((1000,1000), dtype=np.int64)
    #np_mat2 = np.zeros((1000,1000), dtype=np.int64)
    #local_np_mat = np.zeros((2,1000), dtype=np.int64) #container to receive data
    #np_mat_gathered = np.zeros((1000,1000), dtype=np.int64) #container to gather data

    #np_mat = np.loadtxt("1000x1000_matrix.txt", usecols=range(0, 1000), dtype=np.int64)
    #np_mat2 = np.loadtxt("1000x1000_matrix.txt", usecols=range(0, 1000), dtype=np.int64)

    if (RANK == MASTER): 
        print("Initial np_matrix at processor at: {}".format(RANK))
        print(np_mat)
        print("Scattering the np_matrix to all processor from {}".format(MASTER))
    #COMM.Scatter(sendbuf, recvbuf, root) is
    #COMM.Scatter([np_mat (data), 8 (count), MPI.INT (datatype)], [local_np_mat, 8, MPI.INT], root=MASTER)
    #COMM.Scatter([np_mat, 8, MPI.INT], local_np_mat, root=MASTER)
    COMM.Scatter(np_mat, local_np_mat, root=MASTER)
    COMM.Bcast(np_mat2, MASTER)
    COMM.Barrier()

    print("The np_matrix has been scattered!")
    print("***********************************************")
    print("Local np_matrix at processor {}:".format(RANK))
    print(local_np_mat)
    print("***********************************************")
    time.sleep(1)
    print("***********************************************")

    np.matmul(local_np_mat, np_mat2, local_output_mat)

    #COMM.Gather(local_np_mat, np_mat_gathered, root=MASTER)
    COMM.Gather(local_output_mat, np_mat_gathered, root=MASTER)
    COMM.Barrier()
    if RANK == MASTER:
        print("Gathering the local np_matrix to the Master Processor!")
        print("***********************************************")
        print("Gathered np_matrix:")
        print(np_mat_gathered)
    
def mat_mult(mat1, mat2, output_mat):
    
    row = len(mat1)
    col = len(mat1[0])
    start_time = time.time()
    for r in range(0, row):
        for c in range(0, col):
            for r_iter in range(0, row):                
                output_mat[r][c] += mat1[r][r_iter] * mat2[r_iter][c] 
    
    end_time = time.time()
    #print(type(output_mat[0][0]), "took","--- %s seconds ---" % (end_time - start_time))

    return output_mat

if __name__ == "__main__":
    main()
