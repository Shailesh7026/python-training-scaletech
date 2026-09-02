# # classic coroutine
# def fun():
#     while True:
#         x = yield
#         print("Received :" , x)

# coroutine = fun()
# next(coroutine)
# coroutine.send(1)
# coroutine.send(2)
# coroutine.send(3)

# native coroutine 

import asyncio

async def fun(x):
    i = 0
    while i < 10:
        print("Received :", i)
        await asyncio.sleep(1)
        i += 1
        

asyncio.run(fun(1))
