from mpi4py import MPI
import time

start = time.time
def BubbleSort(val):
        for passnum in range (len(val)-1,0,-1):
                for i in range(passnum):
                        if val[i]>val[i+1]:
                                temp = val[i]
                                val[i] = val[i+1]
                                val[i+1] = temp

DaftarAngka = [23,87,2,10,2004,24,43,12]
BubbleSort(DaftarAngka)
print(DaftarAngka)
end = time.time()
print("waktu dikerjakan", end-start)