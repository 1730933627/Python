import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadID,name,conuter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name = name
        self.conuter = conuter
    def run(self):
        print("{0}-开始线程:".format(self.name))
        print_time(self.name,self.conuter,5)
        print("{0}:结束线程".format(self.name))

def print_time(threadName,delay,conuter):
    while conuter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s,%s" %(threadName,time.ctime(time.time())))
        conuter -= 1


thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
#thread3 = myThread(3, "Thread-3", 3)

thread1.start()
thread2.start()
#thread3.start()

thread1.join()
thread2.join()
#thread3.join()
print("退出主程序")

