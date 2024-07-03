l = list((1,))
l2 = list(map(lambda x: x + 10, range(5)))
print(l, l2)

a = [4, 2, 5, 1, 3, 0, 33]


def insert_sort(a):
    n = len(a)
    for k in range(1, n):
        for t in range(k, 0, -1):
            if a[t] > a[t - 1]:
                a[t], a[t - 1] = a[t - 1], a[t]


insert_sort(a)
print(a)

a = [4, 2, 5, 1, 3, 0, 33]


def insert_sort_s(a):
    n = len(a)
    for i in range(1, n):
        for t in range(i, 0, -1):
            if a[t] > a[t - 1]:
                a[t], a[t - 1] = a[t - 1], a[t]
            else:
                break


insert_sort_s(a)
print(a)

a = [4, 2, 7, 5, 1, 3, 0, 33]


def choise_sort(a):
    n = len(a)
    for k in range(n):
        temp = k
        for t in range(k, n - 1):
            if a[temp] > a[t + 1]:
                a[temp], a[t + 1] = a[t + 1], a[temp]


choise_sort(a)
print(a)


a = [4, 2, 5, 1, 3, 0, 33, 7]


def choise_sort_s(a):
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
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


print("{0:-^30}".format(" pi function "))

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


def anagram(s: str):

    if not isinstance(s, str):
        return False

    n = len(s)
    if n == 1 or n == 0:
        return True
    l = s[0]
    r = s[-1]
    if l == r:
        return anagram(s[1:-1])
    else:
        return False


ex_1 = "abccbad"
exa_2 = 10
# print(anagram(ex_1))
# print(anagram(exa_2))


def find_equals(arr_a, arr_b):
    dict_a = {}
    res = []
    for item in arr_a:
        if not dict_a.get(item):
            dict_a[item] = 1
        else:
            dict_a[item] += 1

    for item in arr_b:
        if item in dict_a and dict_a[item] > 0:
            res.append(item)
            dict_a[item] -= 1
    return res


# print(find_equals([1,2,2,3], [2,2]))
# print(find_equals([1,2,3], [4]))
# print(find_equals([1,1,1,2,3,4], [3,4]))


def separate_elemenst(arr):
    di_from_arr = {}
    for item in arr:
        val = sorted(item)
        val = "".join(val)
        if not di_from_arr.get(val):
            di_from_arr[val] = [item]
        else:
            di_from_arr[val].append(item)

    res = [a for a in di_from_arr.values()]
    return res


elements = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(separate_elemenst(elements))


def group_by():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
    b = ["c", "a", "b", "c", "a", "b", "c", "a", "b", "c"]
    d = {}
    for i, j in zip(b, a):
        if d.get(i):
            d[i] += j
        else:
            d[i] = j
    return d


def mod_five(arr, x):
    res = []
    for i in arr:
        t = i % x
        if t == 0:
            res.append(i)
        else:
            res.append(i + (x - t))
    return res


if __name__ == "__main__":
    # print(group_by())
    print(mod_five([0, 2, 3, 12, 21, 30], 5))
