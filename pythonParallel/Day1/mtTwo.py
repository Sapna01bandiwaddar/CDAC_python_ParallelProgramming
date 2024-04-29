from threading import Thread
def doSomeJob():
    for _ in range(10):
        print('X',end=" ")
if __name__=="__main__":
    tObj= Thread(target=doSomeJob)
    tObj.start()
    for _ in range(10):
        print('0',end=" ")        