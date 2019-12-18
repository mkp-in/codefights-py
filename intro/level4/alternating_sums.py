def alternatingSums(a):
    s = [0, 0]
    for i, val in enumerate(a):
        s[i%2] += val
    return s


if __name__ == '__main__':
    print(alternatingSums([50, 60, 60, 45, 70]))
