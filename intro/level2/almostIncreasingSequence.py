def almostIncreasingSequence(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    print(last)
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True


def almostIncreasingSequence2(sequence):
    count = 0
    for i in range(0, len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            count += 1
        if count >= 2:
            return False

    for i in range(0, len(sequence) - 2):
        if sequence[i] >= sequence[i + 2]:
            count += 1
        if count > 2:
            return False

    return True

if __name__ == "__main__":
    print(almostIncreasingSequence([1, 2, 3, 2, 1]))

