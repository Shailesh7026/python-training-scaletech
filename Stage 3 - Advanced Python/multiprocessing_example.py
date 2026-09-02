from multiprocessing import Process
import os
import time

def fun(ch):
    print(f"Process Id {os.getpid()} Started - {ch}")
    time.sleep(2)
    print(f"Process Id {os.getpid()} Finished - {ch}")
    
if __name__ == "__main__":
    p1 = Process(target=fun,args=("A",))
    p2 = Process(target=fun,args=("B",))
    
    p1.start()
    p2.start()
    
    print(f"Main Process Id {os.getpid()}")
    
