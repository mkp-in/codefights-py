def firstNotRepeatingCharacter(s):
    seen = {}
    for i, c in enumerate(list(s)):
        if seen.get(c) is not None:
            seen[c] = -1
        else:
            seen[c] = i

    minimum = len(s)
    val = "_"
    for k, v in seen.items():
        if v >= 0:
            if v < minimum:
                minimum = v
                val = k

    return val



if __name__ == '__main__':
    print(firstNotRepeatingCharacter("abacabad"))
    print(firstNotRepeatingCharacter("bcccccccb"))
