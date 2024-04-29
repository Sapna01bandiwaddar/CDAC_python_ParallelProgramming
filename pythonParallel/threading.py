import threading as td
def square(num):
    print(f"Square: {num*num}")
def cube(num):
    print(f"cube: {num*num*num}")

if __name__=='__main__':
    t1 = td.Thread(target=square,args=(10, ))
    t2 = td.Thread(target=cube,args=(10, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()     