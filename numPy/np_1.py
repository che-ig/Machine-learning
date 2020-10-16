import numpy as np
simple_array = np.array([1, 8, 2, 4])
array_example = np.array([[5,5], [6,6], [7,7]])
# создание массива содержащий нули
z = np.zeros((2, 2))
# создание массива содержащий еденицы 
o = np.ones((2, 4), dtype=np.int64)
# создание массива рандомных значений 
e = np.empty(2)

# создание массива диапозона от нуля до требуемого значения 
r = np.arange(4)
print(np.sort(simple_array))
print(np.concatenate((e, simple_array)))
print(z, o, e)
# shape and size of array
print(array_example.ndim)
print(array_example.size)
print(array_example.shape)
# create a new form
print(array_example.reshape(2, 3))