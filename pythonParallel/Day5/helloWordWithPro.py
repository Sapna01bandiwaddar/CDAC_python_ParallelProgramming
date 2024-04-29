from mpi4py import MPI

comm = MPI.COMM_WORLD # default communicator
rank = comm.Get_rank()

if rank == 0:
    print(f"Hello world...From first processor")
elif rank == 1:
    print(f"Hello world...From second processor")
else:
    print(f"Hello world...From others")