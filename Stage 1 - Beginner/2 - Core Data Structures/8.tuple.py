tuple = (1,)
tuple = (1) # ⚠️ it creates string

# Because they are immutable, tuples can be used as keys in a dictionary (lists cannot)

dic = {
    (1, 2): "value1",
    (3, 4): "value2"
}


tuple1 = ([1,2,3], 2, 3)
tuple1[0].append(4) # ✅ it is allowed because list is mutable

# Shallow copy and deep copy

tuple2 = (1, 2, [3, 4])

import copy
tuple3 = copy.copy(tuple2) # shallow copy
tuple4 = copy.deepcopy(tuple2) # deep copy

# editing the list inside the tuple
tuple2[2].append(5)

print(tuple2) # (1, 2, [3, 4 , 5])
print(tuple3) # (1, 2, [3, 4 , 5])
print(tuple4) # (1, 2, [3, 4])