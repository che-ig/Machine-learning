import numpy as np
a = np.array([1, 8, 2, 4])
# создание массива содержащий нули
z = np.zeros((2, 2))
# создание массива содержащий еденицы 
o = np.ones(2, dtype=np.int64)
# создание массива рандомных значений 
e = np.empty(2)

# создание массива диапозона от нуля до требуемого значения 
r = np.arange(4)
print(np.sort(a))
print(np.concatenate((e, o)))
print(z, o, e, r)