import procs

MASTER = 0

def main():
    
    p = procs.procs() # MPI.COMM_WORLD will be called within the definition of class procs.
    RANK = p.getRank()
    SIZE = p.getSize()

