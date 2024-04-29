from threading import Thread
def doSomeJob():
    while True:
        print('X',end=" ")
if __name__=="__main__":
    tObj= Thread(target=doSomeJob)
    tObj.start()
    while True:
        print('0',end=" ")        