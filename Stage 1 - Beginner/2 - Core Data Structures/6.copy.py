# shallow copy vs deep copy 
l1 = [[1,2,3],1,2,3]
l2 = l1[:] 

import copy 
shallow = l1.copy()
deep = copy.deepcopy(l1)

# edit l1
l1[1] = 2
l1[0][0] = 2

print(l1)
print(l2)
print(shallow)
print(deep)