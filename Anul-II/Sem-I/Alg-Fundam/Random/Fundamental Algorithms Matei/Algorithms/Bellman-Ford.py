import sys
import ReadGraphFromFile


def BF(start, someList, nodes):
    distance = [sys.maxsize] * nodes
    tati = [-1] * nodes
    distance[start] = 0

    for i in range(nodes - 1):
        for x in someList:
            if distance[x[0]] + x[2] < distance[x[1]]:
                distance[x[1]] = distance[x[0]] + x[2]
                tati[x[1]] = x[0]

    for x in someList:
        if distance[x[0]] + x[2] < distance[x[1]]:
            return ["nu merge bo$$"]

    result = []
    for i in range(nodes):
        result.append((i, distance[i]))
    return result


m, n, listAlg = ReadGraphFromFile.readWeightedFile()

print(BF(0, listAlg, n))
