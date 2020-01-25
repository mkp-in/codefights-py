def excelSheetColumnNumber(a):
    t = 0
    a = a[::-1]
    for i in range(len(a)):
        t += (26 ** i) * (ord(a[i]) - ord('A') + 1)

    return t


if __name__ == '__main__':
    print(excelSheetColumnNumber("AB"))
    print(excelSheetColumnNumber("ZZ"))
