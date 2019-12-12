def sortByHeight(a):
    n = [i for i in a if i >= 0]
    n = sorted(n)
    j=0
    for i in range(len(a)):
        if a[i] >= 0:
            a[i] = n[j]
            j += 1

    return a


if __name__ == '__main__':
    print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))

