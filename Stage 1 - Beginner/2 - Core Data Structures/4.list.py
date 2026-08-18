list = ["Shailesh", 20, 3.14, True, [1, 2, 3], 4+5j, None]

# list is mutable - can change the value of list
list[0] = "Shailesh Kumar"
print(list) # ['Shailesh Kumar', 20, 3.14, True, [1, 2, 3], (4+5j), None]

# built - in methods 
print(len(list)) # 7
list.append("77")
print(list)
print(list.pop())
print(list)
list.insert(0,"Prajapati")
print(list)
list.extend([1,2,3])
print(list)
list.remove(2)
print(list)
# print(list.sort()) # error 
print(list.sort(key=str))
print(list)
print(list.reverse())
print(list)

# list is mutable  

l1 = [1,2,3]
l2 = l1

l1.insert(0,0)
print("l1 = ",l1) # l1 =  [0, 1, 2, 3]
print("l2 = ",l2) # l2 =  [0, 1, 2, 3]
print(l1 is l2) # True - both l1 and l2 point to the same object in memory


# list comprehension
l1 = [1,2,3,4,5]
l2 = [x**2 for x in l1]
l3 = [x for x in l1 if x % 2 == 0]

print(l2) # [1, 4, 9, 16, 25]
print(l3) # [2, 4]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Accessing row 1, column 2 (value 6)
print(matrix[1][2]) 


# test 1
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums[1:6:2])


# test 2
result = [x * 2 if x % 2 == 0 else x for x in range(5)]
print(result)

# test 4
grid = [[]] * 3
grid[0].append(5)
print(grid)




