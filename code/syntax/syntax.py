import HPspmd       #HPspmd must import numpy as np.
                    #HPspmd must have its own print function.
                    #HPspmd print function should check if the Rank is Master and print matrices.
#import procs   ... Do we need procs or HPspmd?

MASTER = 0

def main():
    
    p = HPspmd.procs() # MPI.COMM_WORLD will be called within the definition of class procs.
    RANK = p.getRank()
    SIZE = p.getSize()

    on(p):
        # Declare the empty matrices.
        mat = HPspmd.matrix(1000,1000,DOUBLE)
        mat2 = HPspmd.matrix(1000,1000,DOUBLE)

        # Next two lines need to be auto-generated.
        #local_mat = HPspmd.matrix(1000/SIZE,1000,DOUBLE)
        #local_output_mat = HPspmd.matrix(1000/SIZE,1000,DOUBLE)
        
        # np_mat3 will hold the result of HPspmd.matmul
        mat3 = HPspmd.matrix(1000,1000,DOUBLE)

        # Initialize or read matrices.
        mat = HPspmd.matrix_read("fileName")
        mat2 = HPspmd.matrix_read("fileName")

        # Calling MPI functions Scatter, Bcast, and Barrier.
        # Here is the location for MPI functions.

        mat3 = HPspmd.matmul(mat, mat2)

        # Calling MPI functions Gather and Barrier.

    



