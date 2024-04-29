from os import getpid
from multiprocessing import Process, Pipe
def childProcess(myPipeWrite):
    myPipe.Write.send([1001,"Some name here", 3456.9876])
    print(f"writing into the pipe done-->{getpid()}")
    myPipeWrite.close()
if __name__=="__main__":
    print(f"Main parent process here{getpid()}")
    pRead,pWrite=Pipe()
    pObj=Process(target=childProcess,args=(pWrite, ))
    pObj.start()
    print(f"Received.. {pRead.recv()}")
    pObj.join()    