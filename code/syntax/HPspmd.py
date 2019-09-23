from mpi4py import MPI
import numpy as np

#import abc

class HPspmd:

    # Are these class attributes or instance attributes?
    COMM = None
    RANK = None
    SIZE = None

    def procs(self):
        COMM = MPI.COMM_WORLD
        RANK = MPI.Get_rank()
        SIZE = MPI.Get_size()

    def getRank(self): return RANK
    def getSize(self): return SIZE

    def __repr__(self):
        pass

    @staticmethod
    def on(p):
        pass
        
    @staticmethod
    def matmul(mat1, mat2, output_mat):
        return np.matmul(mat1, mat2, output_mat)
    
    @staticmethod
    def matrix(row, col, datatype):
        return np.zeros((row, col), dtype=datatype)
        
    @staticmethod
    def matrix_read(filename, datatype):
        return np.loadtxt(filename, usecols=range(0, col), dtype=datatype)
    

#class HPspmd(abc.ABC):
#    pass
#
# HPspmd Abstract Base Class
# Use '@abc.abstrctmethod' decorator to define abstract functions.# i.e.
#
#@abc.abstractmethod
#def abstract_func():
#   pass
