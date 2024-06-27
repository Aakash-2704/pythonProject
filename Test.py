import pandas as pd

import numpy as np

a = [1,2,3,4,5]

print(a)

a1 = 1

b = a1 == 1

print(b)


numpy_arr = np.array(a)

print(numpy_arr)

print(numpy_arr.dtype)




list_list = [[3,4],[5,6]]

print(list_list)

numpy_list = np.array(list_list)

print(numpy_list)

print(len(numpy_list.shape))

print(np.arange(5))

b = np.random.rand(5,5)

#print(b)

print(b[:4])

