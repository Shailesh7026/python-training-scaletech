import threading
import time

connection_pool =  threading.Semaphore(2)

def connect_db():
    with connection_pool:
        print(f"Connected {threading.current_thread().name}")
        time.sleep(2)
        print(f"Disconnected{threading.current_thread().name}")
        

for i in range(5):
    thread = threading.Thread(target=connect_db,name=f"Thread {i+1}")
    thread.start()
    
