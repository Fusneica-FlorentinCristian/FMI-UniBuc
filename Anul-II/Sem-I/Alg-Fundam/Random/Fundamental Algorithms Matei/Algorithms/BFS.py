import queue
from Algorithms import ReadGraphFromFile


def BFS(start, someList):
    v = []
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        nod = q.get()
        if nod not in v:
            v.append(nod)
            for i in someList[nod]:
                q.put(i)

    return v


m, n, listAlg = ReadGraphFromFile.readUnweightedFile()
lista = ReadGraphFromFile.listaAdiacenta(n, listAlg, "neorientat")

print(BFS(0, lista))
