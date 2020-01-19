def palindromeRearranging(inputString):
    a = {c:inputString.count(c) for c in inputString}
    even = [v for v in a.values() if v % 2 == 0 ]
    print(a)
    print(even)
    if len(a) - len(even) > 1:
        return False
    return True


if __name__ == '__main__':
    print(palindromeRearranging("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"))
    print(palindromeRearranging("abbcabb"))
    print(palindromeRearranging("zyyzzzzz"))
