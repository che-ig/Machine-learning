
path = 5
d = [1] + [0 for _ in range(path)]
jumps = [1, 2, 5, 10]
for i in range(1, path + 1):
    for j in jumps:
        if i >= j:
            d[i] += d[i - j]
print(d)