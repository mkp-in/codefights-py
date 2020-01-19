def calculate(a, r, c):
    t = 0
    maxr = len(a)
    maxc = len(a[0])
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if i >= 0 and i < maxr and j >= 0 and j < maxc:
                if not (i == r and j == c) and a[i][j]:
                    t += 1
    return t


def minesweeper(matrix):
    ret = []
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(0, rows):
        a = []
        for c in range(0, cols):
            a.append(calculate(matrix, r, c))

        ret.append(a)

    return ret

if __name__ == '__main__':
    print(minesweeper([[True,False,False], [False,True,False], [False,False,False]]))