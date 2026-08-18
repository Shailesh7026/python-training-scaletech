# set = {} # ⚠️ This is not a set, it is a dictionary
# set = set() # ✅ This is a set

set = {1, 2, 3, 4, 5 , 5}
print(set) # {1, 2, 3, 4, 5} - duplicate values are removed


# Set methods 
set.add(6)
print(set) # {1, 2, 3, 4, 5,6}

set.remove(7) # ⚠️ KeyError: 7

set.discard(5) # ✅ it will not throw error if the element is not present in the set
print(set) # {1, 2, 3, 4, 5}

set.pop() # removes a random element from the set since set is unordered


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# union
print(a | b) # {1, 2, 3, 4, 5, 6, 7, 8}
# intersection
print(a & b) # {4, 5}
# difference
print(a - b) # {1, 2, 3}
# symmetric difference - removes the common elements from both sets
print(a ^ b) # {1, 2, 3, 6, 7, 8}