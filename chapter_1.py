import numpy as np

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output

#weights = [0.1, 0.2, 0] 
            #toes %win #fans
ih_wgt = np.array([ [0.1, 0.2, -0.1], #hid[0]
           [-0.1,0.1, 0.9], #hid[1]
           [0.1, 0.4, 0.1] ]) #hid[2]

           #hid[0] hid[1] hid[2]
hp_wgt = np.array([ [0.3, 1.1, -0.3], #hurt?
           [0.1, 0.2, 0.0], #win?
           [0.0, 1.3, 0.1] ]) #sad?

weights = [ih_wgt, hp_wgt]

def vect_mat_mul(vect,matrix):
    assert(len(vect) == len(matrix))
    output = [0,0,0]
    for i in range(len(vect)):
        output[i] = w_sum(vect,matrix[i])
    return output

def neural_network(input, weights):
    hid = input.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred

toes =  np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65,0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

# Input corresponds to every entry
# for the first game of the season.

input = np.array([toes[0],wlrec[0],nfans[0]])
pred = neural_network(input,weights)

print(pred)

'''
def average(input):
    summ = sum(input)
    return summ / len(input)
print(average(toes))
'''

# print(neural_network(np.array([toes[0], wlrec[0], nfans[0]]), np.array([0.1, 0.2, -0.1])))
'''
w1 = [toes[0], wlrec[0], nfans[0]]
w2 = [0.1, 0.2, -0.1]
def summ(e1, e2):
    return e1 * e2
res = sum(list(map(summ, w1, w2)))
print(res)
'''

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
    ])
d = np.zeros((2, 4)) # Матрица 2*4 заполненная нулями
e = np.random.rand(2, 5) # Матрица 2*5 заполненная случайными числами от 0 до 1

f = np.zeros((1, 4))
g = np.zeros((4, 3))
cc = f.dot(g)

print(a)
print(b)
print(c)
print(d)
print(e)

print(a * c)
print('cc= ', cc)