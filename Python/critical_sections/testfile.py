import threading, time, random

# Refer to README.md for the problem instructions

class AddThread( threading.Thread ):
    def __init__(self, threadName, lock):
        threading.Thread.__init__(self, name=threadName)
        self.lock = lock
    
    def run(self):
        global number 
        self.lock.acquire()
        try:
            number += 1
            rando = random.uniform(1, 3)
            time.sleep(rando)
            number += 1    
        finally:
            self.lock.release()
        
    pass


class MultiplyThread( threading.Thread ):
    def __init__(self, threadName, lock):
        threading.Thread.__init__(self, name=threadName)
        self.lock = lock
    
    def run(self):
        global number 
        self.lock.acquire()
        try:
            number *= 2
            rando = random.uniform(1, 3)
            time.sleep(rando)
            number *= 2    
        finally:
            self.lock.release()
        
    pass


if __name__ == "__main__":
    number = 1

    lock = threading.RLock()

    thread1 = AddThread("thread1", lock)
    thread2 = MultiplyThread("thread2", lock)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Number is: {}".format(number))
