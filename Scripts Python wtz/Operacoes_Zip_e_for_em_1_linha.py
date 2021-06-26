import numpy as np

x = np.array([3, 6, 7, 2]) # array do numpy
#ou
# x = [3, 6, 7, 2]  #lista do python
print(x)
print(x[1:])
print(x[:-1])
a = [x-y for x,y in zip(x[1:],x[:-1])]

print(a)
