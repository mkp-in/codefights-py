def firstDuplicate(a):
    seen = {}
    for d, i in enumerate(a):
        if seen.get(i):
            return i
        else:
            seen[i] = d + 1

    return -1


if __name__ == '__main__':
    print(firstDuplicate([2, 1, 3, 5, 3, 2]))

