import _thread 

def fun(threadName , count):
    print("Current Thread :",threadName,"\n")
    while count >= 0:
        print(f"{threadName} : {count} \n")
        count -= 1;


thread1 = _thread.start_new_thread(fun,("Thread 1",2))
thread2 = _thread.start_new_thread(fun,("Thread 2",3))

# thread1.join() is not available with _thread.start_new_thread()
# thread2.join()

print("Main Thread")
