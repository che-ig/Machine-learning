l = list((1,))
l2 = list(map(lambda x: x+10, range(5) ))
print(l, l2)

a = [4,2,5,1,3, 0, 33]
def insert_sort(a):
    n =len(a)
    for k in range(1, n):
        for t in range(k, 0, -1):
            if a[t] > a[t-1]:
                a[t], a[t-1] = a[t-1], a[t]

insert_sort(a)
print(a)

a = [4,2,5,1,3, 0, 33]
def insert_sort_s(a):
    n =len(a)
    for i in range(1, n):
        for t in range(i, 0, -1):
            if a[t] > a[t-1]:
                a[t], a[t-1] = a[t-1], a[t]
            else:
                break    
        
insert_sort_s(a)
print(a)

a = [4,2,7, 5,1,3, 0, 33]
def choise_sort(a):
    n = len(a)
    for k in range(n):
        temp = k
        for t in range(k, n-1):
            if a[temp] > a[t+1]:
                a[temp], a[t+1] = a[t+1], a[temp]

choise_sort(a)
print(a)


a = [4,2,5,1,3, 0, 33, 7]
def choise_sort_s(a):
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]

choise_sort_s(a)
print(a)                

def pi_fun(a):
    n = len(a)
    pi = [0] * n
    for i in range(1, n):
        if a[i] == a[pi[i - 1]]:
            pi[i] = pi[i - 1] + 1
        else:
            j = pi[i - 1] - 1
            while j > 0:
                if a[j] == a[i]:
                    pi[i] = pi[j] + 1
                    break
                else:
                    j -= 1
                    pi[i] = 0
   
    return pi

print("{0:-^30}".format(' pi function '))

example_1 = "abcdabscabcdabia"
example_2 = "лиилфлит"
example_3 = "aabaaab"
print(pi_fun(example_1))
print(pi_fun(example_2))
print(pi_fun(example_3))

array = [-88, 5, 7, -1, 3, 0, 11, 2, 5]
def quickSort(array):
    n = len(array)
    l = []
    m = []
    r = []
    if n >= 1:
        for item in array:
            if item > array[0]:
                r.append(item)
            elif item < array[0]:
                l.append(item)
            else:
                m.append(item)
        l = quickSort(l)
        r = quickSort(r)
    else:
        return []
    return l + m + r

print(quickSort(array))