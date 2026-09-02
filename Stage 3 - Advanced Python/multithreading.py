import threading 

def fun(x):
    print("Current Thread :",threading.current_thread(),"\n")
    while x >= 0:
        print(f"{threading.current_thread().name} : {x} \n")
        x -= 1;
        
thread1 = threading.Thread(target=fun,args=(2,))
thread2 = threading.Thread(target=fun,args=(3,))

thread1.start()
thread2.start()

thread1.join()
# thread2.join()

print("Main Thread")
