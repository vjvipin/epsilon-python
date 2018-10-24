import numpy as np
# pip3 install numpy
a = np.zeros((3,3,3))
print (dir(np))
print(a)
b = np.ones((2,2,4,5), dtype=int)
print(b)
np.random.rand(10)
data = np.random.randint(5,10,(10,10))
print(data)

#Access of NumPy
print(data[4:8])

print(data[4:8,4:6])
# Combine Data

data1 = np.random.randint(5,15,size=(5,3))
data2 = np.random.randint(5,15,size=(5,3))
print(np.hstack([data1,data2]))
print(np.vstack([data1, data2]))
print(np.concatenate([data1, data2], axis=1)) # axis = 0
a1,a2 = np.hsplit(data,[5])
b1,b2,b3 = np.vsplit(data,[5,7])
# print all of above to see the result
# Check out following attribute 
data.shape
data.ndim
data.size
data.reshape(2,50)
np.sum(data)
np.sum(data, axis=1)
np.sin(data)
data.mean(axis=1)
data.std(axis=1)






