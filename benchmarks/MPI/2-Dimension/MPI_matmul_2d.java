/*
Author: Heecheon Park
Description: Matrix multiplication in 1d array.
 */

import mpi.*;

class MPI_matmul {
    static public void main(String[] args) throws MPIException {

        public static final int MASTER = 0;
        public static final int NRA = 1000;
        public static final int NCA = 1000;
        public static final int NCB = 1000;

        static double[][] mat = new double[NRA][NCA];
        static double[][] mat2 = new double[NRA][NCB];
        static double[][] output_mat = new double[NRA][NCB];

        int myrank,
            size,
            numworkers,
            rows,
            source,
            dest,
            averow,
            extra,
            offset,
            i, j, k, rc;

        MPI.Init(args);
        myrank = MPI.COMM_WORLD.getRank();
        size = MPI.COMM_WORLD.getSize() ;
        Status status;

        numworkers = size - 1;

        if (rank == MASTER)
        {
            Scanner sc = new Scanner(
                         new BufferedReader(
                         new FileReader("1000x1000_matrix.txt")));

            while (sc.hasNextLine())
            {
                for (i = 0; i < mat.length; i++)
                {
                    String[] line = sc.nextLine().trim().split(" ");
                    for (j = 0; j < line.length; j++)
                    {
                        mat[i][j] = Double.parseDouble(line[j]);
                        mat2[i][j] = Double.parseDouble(line[j]);
                        output_mat[i][j] = 0;
                    }
                }
            }

            averow = NRA / numworkers;
            extra = NRA % numworkers;
            offset = 0;

            for (dest = 1; dest <= numworkers; dest++)
            {
                rows = (dest <= extra) ? averow + 1 : averow;

                System.out.println("Sending ", rows, " rows to task ", dest, " offset = ", offset);
                
                MPI_Send(offset, 1, MPI_INT, dest, 1, MPI.COMM_WORLD);
                MPI_Send(rows, 1, MPI_INT, dest, 1, MPI.COMM_WORLD);
                MPI_Send(mat[offset][0], rows * NCA, MPI_DOUBLE, dest, 1, MPI.COMM_WORLD);
                MPI_Send(mat2, rows * NCA, MPI_DOUBLE, dest, 1, MPI.COMM_WORLD);
                offset = offset + rows;
            }

            for (i = 1; i <= numworkers; i++)
            {
                source = 1;
                MPI_Recv(offset, 1, MPI_INT, source, 2, MPI.COMM_WORLD, status);
                MPI_Recv(rows, 1, MPI_INT, source, 2, MPI.COMM_WORLD, status);
                MPI_Recv(output_mat[offset][0], rows * NCB, MPI_INT, source, 2, MPI.COMM_WORLD, status);
            }

            for (i = 0; i < NRA; i++)
            {
                System.out.println();
                for (j = 0; j < NCB; j++)
                    System.out.println(" ", output_mat[i][j]);
                System.out.println();
            }

        }

        if (world_rank > MASTER)
        {
            MPI_Send(offset, 1, MPI_INT, MASTER, 1, MPI.COMM_WORLD);
            MPI_Send(rows, 1, MPI_INT, MASTER, 1, MPI.COMM_WORLD);
            MPI_Send(mat, rows * NCA, MPI_DOUBLE, MASTER, 1, MPI.COMM_WORLD, status);
            MPI_Send(mat2, NCA * NCB, MPI_DOUBLE, MASTER, 1, MPI.COMM_WORLD, status);

            for (k = 0; k < NCB; k++)
                for (i = 0; i < rows; i++)
                {
                    output_mat[i][j] = 0.0;
                    for (j = 0; j < NCA; j++)
                        output_mat[i][k] = output_mat[i][k] + mat[i][j] * mat2[j][k];
                }

            MPI_Send(offset, 1, MPI_INT, MASTER, 2, MPI.COMM_WORLD);
            MPI_Send(rows, 1, MPI_INT, MASTER, 2, MPI.COMM_WORLD);
            MPI_Send(output_mat, 1, MPI_INT, MASTER, 2, MPI.COMM_WORLD);
        }

        if (world_rank == MASTER)
            printMat(output_mat, 1000, 1000);

        MPI.Finalize();
    }

    public void printMat(double mat[1000][1000], int row, int col)
    {
        for (int i= 0; i < row; i++)
        {
            for (int j = 0; j < row; j++)
                System.out.print(" ", mat[i][j]);
            System.out.println();
        }
    }
}
