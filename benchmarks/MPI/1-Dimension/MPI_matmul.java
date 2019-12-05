/*
Author: Heecheon Park
Description: Matrix multiplication in 1d array.
 */

import mpi.*;

class MPI_matmul {
    static public void main(String[] args) throws MPIException {

        MPI.Init(args);

        int myrank = MPI.COMM_WORLD.getRank();
        int size = MPI.COMM_WORLD.getSize() ;
        System.out.println("Hello world from rank " + myrank + " of " + size);

        MPI.Finalize();
    }
}
