from multiprocessing import Process, Pipe
def f(con):
    con.send([1,'Sapna Bandiwaddar',20000])
    con.close()
if __name__=='__main__':
    parent_con, child_con = Pipe() 
    p = Process(target=f,args=(child_con, ))
    p.start()
    print(parent_con.recv())
    p.join()   