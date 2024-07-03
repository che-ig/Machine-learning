def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


def erotosfen(a):
    primes = []
    arr = [True] * a
    arr[0], arr[1] = False, False
    for i in range(2, a):
        if arr[i]:
            for j in range(i * 2, a, i):
                arr[j] = False

    return [v for v, _ in filter(lambda x: x[1], enumerate(arr))]


if __name__ == "__main__":
    r = nod(116, 117)
    print(r)

    prime_numbers = erotosfen(144)
    print(prime_numbers)
