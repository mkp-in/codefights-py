def commonCharacterCount(s1, s2):
    a1 = [0] * 26
    a2 = [0] * 26

    l = len(s1)
    diff = ord('a')
    for i in range(l):
        c = ord(s1[i]) - diff
        a1[c] += 1

    l = len(s2)
    for i in range(l):
        c = ord(s2[i]) - diff
        a2[c] += 1

    total = 0
    for i in range(26):
        total += min(a1[i], a2[i])

    return total

if __name__ == "__main__":
    print(commonCharacterCount("aabcc", "adcaa"))