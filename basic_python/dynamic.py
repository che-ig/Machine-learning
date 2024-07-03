def numberWaysGoToPoint(path: int):
    """
    Число способов попасть в точку i
    """
    path = 5
    d = [1] + [0 for _ in range(path)]
    jumps = [1, 2, 5, 10]
    for i in range(1, path + 1):
        for j in jumps:
            if i >= j:
                d[i] += d[i - j]
    return d


def maxSubSequence(obj_1, obj_2):
    """
    Поиск максимальной общей подпоследовательности
    """
    res = [[0 for _ in range(len(obj_2))] for _ in range(len(obj_1))]
    for i, value_1 in enumerate(obj_1):
        for j, value_2 in enumerate(obj_2):
            if value_1 == value_2:
                res[i][j] = 1 + res[i - 1][j - 1]
            else:
                res[i][j] = max(res[i - 1][j], res[i][j - 1])
    return res[-1][-1]


def maxCommonSubString(obj_1, obj_2):
    """
    Поиск самой длинной общей подстроки
    """
    res = [[0 for _ in range(len(obj_2))] for _ in range(len(obj_1))]

    for i, value_1 in enumerate(obj_1):
        for j, value_2 in enumerate(obj_2):
            if value_1 == value_2:
                res[i][j] = res[i - 1][j - 1] + 1
    return res


if __name__ == "__main__":
    print(numberWaysGoToPoint(5))
    print(maxSubSequence("foseh", "ffiseth"))
    print(maxCommonSubString("hvista", "hish"))
