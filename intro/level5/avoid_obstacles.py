def avoidObstacles(inputArray):
    i = set(inputArray)
    m = max(i)
    for j in range(1, m+2):
        k = {t for t in range(0, m+1, j)}
        p = i & k
        if len(p) == 0:
            return j

    return -1


if __name__ == '__main__':
    print(avoidObstacles([5, 3, 6, 7, 9]))
    print(avoidObstacles([1000, 999]))
    print(avoidObstacles([1, 2]))