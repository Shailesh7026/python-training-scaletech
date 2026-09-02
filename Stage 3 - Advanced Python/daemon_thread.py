import threading
import time

def fun():
    while True:
        print("🦹‍♀️Daemon Thread is Running ...")
        time.sleep(1)

monitor_thread = threading.Thread(target=fun, daemon=True)
monitor_thread.start()

print("Main Thread Started")
time.sleep(3)
print("Main Thread Ended")

# The moment this code ends, the daemon thread is killed instantly, 
# even though it contains an infinite 'while True' loop.
