import multiprocessing as mp
def f(q):
    q.put([1,'Sapna Bandiwaddar',20000])

if __name__=='__main__':
    ctx=mp.get_context("spawn")
    q = ctx.Queue()
    p = ctx.Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()    