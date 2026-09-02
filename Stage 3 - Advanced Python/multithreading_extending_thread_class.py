import threading 

class myThread(threading.Thread):
    def __init__(self,name,count):
        threading.Thread.__init__(self)
        self.name = name
        self.count = count
        
    def run(self):
        print("Current Thread :",self,"\n")
        while self.count >= 0:
            print(f"{self.name} : {self.count} \n")
            self.count -= 1;
        
thread1 = myThread("Thread 1",2)
thread2 = myThread("Thread 2",3)

thread1.start()
thread2.start()

thread1.join()
# thread2.join()

print("Main Thread")
