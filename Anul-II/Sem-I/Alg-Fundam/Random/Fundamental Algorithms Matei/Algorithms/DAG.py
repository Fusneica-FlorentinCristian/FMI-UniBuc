import sys
import ReadGraphFromFile
import TopologicalSorting


def DAG(start, someList):
    length = len(someList)
    distance = [sys.maxsize] * length
    tati = [-1] * length
    distance[start] = 0

    sort_top = TopologicalSorting.topologicalSorting(someList)
    for x in sort_top:
        for i in someList[x]:
            if distance[x] + i[1] < distance[i[0]]:
                distance[i[0]] = distance[x] + i[1]
                tati[i[0]] = x
    result = []
    for i in sort_top:
        result.append((i, distance[i]))
    return result


m, n, listAlg = ReadGraphFromFile.readWeightedFile()
lista = ReadGraphFromFile.listaAdiacenta(n, listAlg, "orientat")

print(DAG(0, lista))
