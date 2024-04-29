import multiprocessing as mp
import os
def info(title):
    print(title)
    print("module name: ",__name__)
    print("parent process: ",os.getpid())
    print("process id",os.getpid())
def f(name):
    print("Hello: ",name)

if __name__=='__main__':
    info("main line")
    p1=mp.Process(target=f, args=('Sapna ',))
    p1.start()
    p1.join()
