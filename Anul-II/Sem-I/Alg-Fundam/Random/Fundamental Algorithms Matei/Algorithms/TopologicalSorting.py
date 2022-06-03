import ReadGraphFromFile
import DFS


def topologicalSorting(someList):
    v = []
    result = []

    for i in range(len(someList)):
        if i not in v:
            DFS.DFS_recursive(i, someList, v, result)

    return result[::-1]


m, n, listAlg = ReadGraphFromFile.readWeightedFile()
lista = ReadGraphFromFile.listaAdiacenta(n, listAlg, "orientat")
print(lista)

print(topologicalSorting(lista))
