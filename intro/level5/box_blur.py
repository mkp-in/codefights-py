def get_avg(a, r, c):
    t = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            t += a[i][j]

    return t//9


def boxBlur(image):
    ret = []
    for r in range(1, len(image)-1):
        a = []
        for c in range(1, len(image[0])-1):
            a.append(get_avg(image, r, c))
        ret.append(a)

    return ret




if __name__ == '__main__':
    print(boxBlur([[1,1,1], [1,7,1], [1,1,1]]))
    print(boxBlur([[36,0,18,9], [27,54,9,0], [81,63,72,45]]))