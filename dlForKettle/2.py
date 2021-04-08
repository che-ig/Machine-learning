import numpy as np

a1 = np.identity(3)
a2 = np.eye(3)
print(a1, '\n', a2)

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(800, 0)
