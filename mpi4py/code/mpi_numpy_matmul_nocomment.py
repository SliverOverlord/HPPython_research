from mpi4py import MPI
import numpy as np
import sys
import time

MASTER = 0

def main():
        
    COMM = MPI.COMM_WORLD
    RANK = COMM.Get_rank()
    SIZE = COMM.Get_size()


    #np.set_printoptions(threshold=sys.maxsize)
            
    np_mat = np.zeros((1000,1000), dtype=np.float64)
    np_mat2 = np.zeros((1000,1000), dtype=np.float64)
    local_np_mat = np.zeros((1000/SIZE,1000), dtype=np.float64)
    local_output_mat = np.zeros((1000/SIZE,1000), dtype=np.float64) 
    np_mat_gathered = np.zeros((1000,1000), dtype=np.float64)

    np_mat = np.loadtxt("1000x1000_matrix.txt", usecols=range(0, 1000), dtype=np.float64)
    np_mat2 = np.loadtxt("1000x1000_matrix.txt", usecols=range(0, 1000), dtype=np.float64)

    COMM.Scatter(np_mat, local_np_mat, root=MASTER)
    COMM.Bcast(np_mat2, MASTER)
    COMM.Barrier()

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
