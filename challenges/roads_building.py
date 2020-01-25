def roadsBuilding(cities, roads):
    def helper(m, source, destination):
        if m.get(source) is None:
            m[source] = set()
        m[source].add(destination)

    all_cities = {i for i in range(cities)}
    d = {}
    for i in roads:
        a,b = i[0], i[1]
        helper(d, a, b)
        helper(d, b, a)

    missing = []
    for i in range(cities):
        s = d.get(i)
        mycity = set()
        mycity.add(i)
        if s is not None:
            missing_cities = sorted(list(((all_cities - s) - mycity)))
            for j in missing_cities:
                if i < j and (i, j) not in missing:
                    missing.append((i, j))
                elif (j, i) not in missing:
                    missing.append((j, i))

    return missing

if __name__ == '__main__':
    print(roadsBuilding(4, [[0,1], [1,2], [2,0]]))
