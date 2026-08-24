from itertools import count,cycle

for i in count(start=1,step=2):
    if i == 11:
        break
    print(i)

for i in count(start=1):
    if i == 10:
        break
    for elem in cycle(["Python" , "Java"]):
        print(elem)
        break
