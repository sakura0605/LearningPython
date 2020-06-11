# Thread 1: print a
# Thread 2: print b
# Write to txt file as format: abababab
# using threading and thread.lock()
import threading

file = open("result.txt", "w")
lock = threading.Lock()

class Thread(threading.Thread):
    def __init__(self, target):
        threading.Thread.__init__(self, target=target)
        self.start()

def printA():
    lock.acquire()
    file.write("a")
    lock.release()

def printB():
    lock.acquire()
    file.write("b")
    lock.release()

for i in range(1, 20):
    t1 = Thread(printA)
    t2 = Thread(printB)

file.close()

