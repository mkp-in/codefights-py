def allLongestStrings(inputArray):
    max_length = 0
    l = len(inputArray)
    for i in range(l):
        l_string = len(inputArray[i])
        if l_string > max_length:
            max_length = l_string


    new_array = []
    for i in range(l):
        l_string = len(inputArray[i])
        if l_string == max_length:
            new_array.append(inputArray[i])


    return new_array


if __name__ == "__main__":
    print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))
    print(allLongestStrings(["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]))
