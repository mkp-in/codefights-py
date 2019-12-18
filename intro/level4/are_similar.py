def areSimilar(a, b):
    k = [(x,y) for x, y in zip(a,b)]
    count = 0
    mismatch = ()
    for i in k:
        x = i[0]
        y = i[1]
        if x != y:
            if len(mismatch) == 0:
                mismatch = (x, y)
            elif mismatch[0] != y or mismatch[1] != x:
                return False
            else:
                count += 1

    if count <= 1:
        return True
    return False





if __name__ == '__main__':
    print(areSimilar([1, 2, 3], [2, 1, 3]))
