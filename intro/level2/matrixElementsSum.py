def matrixElementsSum(m):
    count = 0
    for i in range(0, len(m[0])):
        for j in range(0, len(m)):
            if m[j][i] == 0:
                break
            else:
                count = count + m[j][i]
    return count

def matrixElementsSum2(matrix):
    roomRents=0
    unzip = list(zip(*matrix))
    print(unzip)
    for i in unzip:
        for j in i:
            if(j==0):
                break
            else:
                roomRents+=j
    return roomRents

if __name__ == "__main__":
    matrix = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]
    print(matrixElementsSum2(matrix))
