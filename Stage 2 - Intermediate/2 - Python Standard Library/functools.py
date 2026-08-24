from functools import lru_cache
from datetime import datetime

@lru_cache
def factorial(n):
    if n <= 1:
        return 1
    return factorial(n-1) * n

# first call

start_time = datetime.now()
res = factorial(200)
end_time = datetime.now()

duration = (end_time - start_time) * 1000 

print(f"Factorial :{res} , Time Taken: f{duration.total_seconds():.4f} ms")


#second call
start_time = datetime.now()
res = factorial(200)
end_time = datetime.now()

duration = (end_time - start_time) * 1000 

print(f"Factorial :{res} , Time Taken: f{duration.total_seconds():.4f} ms")

print(factorial.cache_info())
