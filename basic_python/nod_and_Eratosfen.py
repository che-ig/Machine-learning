def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


if __name__ == '__main__':
    r = nod(4, 16)
    print(r)