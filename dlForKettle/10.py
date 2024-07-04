import os
import string

s = "aaa, bbb # 888"


def multySumm(multyList):
    total = 0
    for i in multyList:
        for p in i:
            total += p

    return total


def cum_sum(arr):
    cum_arr = []
    summ = 0
    for i in arr:
        summ += i
        cum_arr.append(summ)
    return cum_arr


example_lest_1 = [[1, 2], [3], [4, 5, 6]]
t = [1, 2, 3, 4]

print(multySumm(example_lest_1))
print(cum_sum(t))


def histogram(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


if __name__ == "__main__":
    print(histogram("бронтазавр"))
    l = s.split()
    d = dict()
    for word in l:
        word = word.strip(string.punctuation + string.whitespace)
        if word:
            d[word] = d.get(word, 0) + 1

    print(d)

    walk(".")
