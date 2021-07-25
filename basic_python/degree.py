def degree(value, deg):
    remainder = deg % 2

    if deg == 0:
        return 1

    if remainder:
        return value * degree(value, deg - 1)
    else:
        return degree(value ** 2, deg // 2)


if __name__ == '__main__':
    r = degree(2, 5)
    print(r)
