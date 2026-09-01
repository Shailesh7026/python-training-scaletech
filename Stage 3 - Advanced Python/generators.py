def count_to(max):
    i = 1
    while i <= max:
        yield i
        i += 1
   
counter = count_to(10)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

for i in count_to(10):
    print(i)
