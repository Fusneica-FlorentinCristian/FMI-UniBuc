import ReadGraphFromFile


def sortRule(x):
    return int(x[2])


def init(x, tati, h):
    tati[x] = -1
    h[x] = 0


def find(x, tati):
    while tati[x] != -1:
        x = tati[x]
    return x


def union(x, y, tati, h):
    rx = find(x, tati)
    ry = find(y, tati)
    if h[rx] > h[ry]:
        tati[ry] = rx
    else:
        tati[rx] = ry
        if h[rx] == h[ry]:
            h[rx] += 1


def algKruskal(n, someList):
    tati = [-1] * n
    h = [-1] * n
    result = []
    someList.sort(key=sortRule)

    for i in range(n):
        init(i, tati, h)
    nr = 0
    for x in someList:
        if find(x[0], tati) != find(x[1], tati):
            result.append(x)
            union(x[0], x[1], tati, h)
            nr += 1

            if nr == n - 1:
                break
    return result


m, n, listWeighted = ReadGraphFromFile.readWeightedFile()
result = algKruskal(n, listWeighted)
print(result)
