def makeArrayConsecutive2(statues):
    statues.sort()
    s = 0
    for i in range(0, len(statues)-1):
        s += statues[i+1]-statues[i]-1
    return s


print(makeArrayConsecutive2([6, 2, 3, 8]))