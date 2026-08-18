def fun(*args):
    print(args)
    
def kfun(**kwargs):
    for k,val in kwargs.items():
        print(f"{k}:{val}")
        
def fun2(*args,**kwargs):
    print(args)
    print(kwargs)

fun(1,2,"str")
kfun(a=1,b=3,name="Shailesh")
fun2(1,2,56,name="shailesh",id="23X1")
# fun2(name="shailesh",id="23X1",1,2,56,) # Syntax Error



# lambda functions 

res = lambda a,b,c : a+b+c
print(res(1,2,3))


check = lambda x : "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(check(12))
print(check(-12))
print(check(0))


