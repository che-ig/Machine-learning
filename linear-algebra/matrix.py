import numpy as np

def addLine():
    print('{0:~^30}'.format('~'))

m1 = np.array([1, 2, 3])
print(m1)

m2 = np.arange(12).reshape(-1, 3)
print(m2)

addLine()
d2 = np.diag(m2)
print(d2)

addLine()
m3 = np.diag(m1)
print(m3)

addLine()
m4 = np.diag(np.ones((4)))
# create E matrix
m5 = np.eye(3)
print(m4, '\n\n', m5, '\n\n', m4[:, 1])

addLine()
m6 = np.arange(2, 6).reshape(-1, 2)
det_m6 = np.linalg.det(m6)
inv_m6 = np.linalg.inv(m6)
r6 = np.linalg.matrix_rank(m6)
print(det_m6, 'inv m6 =', inv_m6, 'rank m6 =', r6)

addLine()
m7 = np.array([[3, -1, 2], [1, 4, -1], [2, 3, 1]])
m7v = np.matrix('-4; 10; 8')
print(m7, '\n\n', m7v, '\n\n')
m7copy = np.matrix(m7)
m7copy[:, 1] = m7v
# m7[:, 1] = m7v
print(m7copy, '\n\n', m7copy[:, 1], '\n\n', m7[:, 1], '\n\n', m7, '\n\n')

a = np.array([2, 7, 3])
b = np.array([5, 9, 3])
vect_cos = lambda a, b: a.T.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(a.T, '\n', a.dot(b.T), vect_cos(a, b))