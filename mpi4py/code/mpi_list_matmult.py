"""
Name: Heecheon Park
Date: September 6th 2019
Minnesota State University Moorhead

Running 1000x1000 matrix multiplication with list and mpi
with 5 processors.


Execution Method:

mpiexec -np 5 python3 mpi_list_matmult.py
"""
from mpi4py import MPI
from numba import njit
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
            
    list_mat = []
    list_mat2 = []
    #local_list_mat = [[int(0) for col in range(1000)] for row in range(row_split)]
    local_list_mat = None
    local_output_mat = [[int(0) for col in range(1000)] for row in range(1000)]
    np_list_gathered = [[int(0) for col in range(1000)] for row in range(1000)]

    with open("1000x1000_matrix.txt",'r') as f:
        for line in f:
            int_string_list = line.split()

            float_list = [float(i) for i in int_string_list]
            list_mat.append(float_list)
            list_mat2.append(float_list)

        f.close()

    #print("local row:",len(local_output_mat))
    #print("local col:",len(local_output_mat[0]))

    if (RANK == MASTER): 
        print("Initial list_matrix at processor at: {}".format(RANK))
        print(list_mat)
        print("Scattering the list_matrix to all processor from {}".format(MASTER))
    #COMM.Scatter(sendbuf, recvbuf, root) is
    #COMM.Scatter([list_mat (data), 8 (count), MPI.INT (datatype)], [local_list_mat, 8, MPI.INT], root=MASTER)
    #COMM.Scatter([list_mat, 8, MPI.INT], local_list_mat, root=MASTER)
    #COMM.Scatter(list_mat, local_list_mat, root=MASTER)
    local_list_mat = COMM.scatter(list_mat, root=MASTER)
    COMM.bcast(list_mat2, MASTER)
    COMM.Barrier()

    print("The list_matrix has been scattered!")
    print("***********************************************")
    print("Local list_matrix at processor {}:".format(RANK))
    print(local_list_mat)
    print("***********************************************")
    time.sleep(1)
    print("***********************************************")

    mat_mult(local_list_mat, list_mat2, local_output_mat)

    #COMM.Gather(local_list_mat, list_mat_gathered, root=MASTER)
    #COMM.Gather(local_output_mat, list_mat_gathered, root=MASTER)
    list_mat_gathered = COMM.gather(local_output_mat, root=MASTER)
    COMM.Barrier()
    if RANK == MASTER:
        print("Gathering the local list_matrix to the Master Processor!")
        print("***********************************************")
        print("Gathered list_matrix:")
        print(list_mat_gathered)
    
@njit
def mat_mult(mat1, mat2, output_mat):
    
    row = len(mat1)
    col = len(mat1[0])
    #start_time = time.time()
    for c in range(0, col):
        for r in range(0, row):
            for r_iter in range(0, col):                
                output_mat[r][c] += mat1[r][r_iter] * mat2[r_iter][c] 
    
    #end_time = time.time()
    #print(type(output_mat[0][0]), "took","--- %s seconds ---" % (end_time - start_time))

    return output_mat

if __name__ == "__main__":
    main()
