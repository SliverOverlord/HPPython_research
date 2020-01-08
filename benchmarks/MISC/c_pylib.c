#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

/*
Author: Heecheon Park

This file is experimental to provide MPI functions
to be called from Python including a few utility functions like matrix multiplication.

Build:
    $gcc -shared -o c_pylib.so -fPIC c_pylib.c
    
    or if you need MPI functionalities, 
    
    $mpicc.mpich -shared -o c_pylib.so -fPIC c_pylib.c
*/

int mpi_send(void* data, int count, int destination, int tag)
{
    MPI_Init(NULL,NULL);
    return MPI_Send(&data, count, MPI_CHAR, destination, tag, MPI_COMM_WORLD);
}

int mpi_recv(void* data, int count, int source, int tag)
{
    MPI_Finalize();
    return MPI_Recv(&data, count, MPI_CHAR, source, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
}

void matmul(double* matA, int rowA, int colA, 
            double* matB, int rowB, int colB, 
            double* matC, int rowC, int colC) 
{
    for (int i = 0; i < rowA; i++) {
        for (int j = 0; j < colB; j++) {
            double sum = 0.0;
            for (int k = 0; k < rowB; k++)
                sum = sum + matA[i * colA + k] * matB[k * colB + j];
            matC[i * colC + j] = sum;
        }
    }
}

int hello_mpi() {
    MPI_Init(NULL, NULL);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    char processor_name[MPI_MAX_PROCESSOR_NAME];
    int name_len;

    MPI_Get_processor_name(processor_name, &name_len);

    printf("Hello world from processor %s, rank %d out of %d processors\n",
           processor_name, world_rank, world_size);

    MPI_Finalize();
}


//int MPI_Send(void* data,
//             int count,
//             MPI_Datatype datatype,
//             int destination,
//             int tag,
//             MPI_Comm communicator)
//
//int MPI_Recv(void* data,
//             int count,
//             MPI_Datatype datatype,
//             int source,
//             int tag,
//             MPI_Comm communicator,
//             MPI_Status* status)

