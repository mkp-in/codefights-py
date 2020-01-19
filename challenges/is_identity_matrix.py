def isIdentityMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(i, j, matrix[i][j])
            if i == j and matrix[i][j] != 1:
                return False
            elif i != j and matrix[i][j] != 0:
                return False
    return True

if __name__ == '__main__':
    m = list()
    m.append([1, 0, 0])
    m.append([0, 1, 0])
    m.append([0, 0, 1])
    print(isIdentityMatrix(m))
