import queue
import ReadGraphFromFile


def prim(someList, start):
    result = []
    pqueue = queue.PriorityQueue()
    v = [start]
    for i in someList[start]:
        pqueue.put((i[1], (start, i[0])))

    while not pqueue.empty():
        bestCost = pqueue.get()
        cost = bestCost[0]
        next = bestCost[1][1]
        if next not in v:
            v.append(next)
            result.append((bestCost[1][0], bestCost[1][1], cost))

            for i in someList[next]:
                pqueue.put((i[1], (next, i[0])))
    return result


m, n, lista = ReadGraphFromFile.readWeightedFile()
lista = ReadGraphFromFile.listaAdiacenta(n, lista, "neorientat")

print(prim(lista, 0))
