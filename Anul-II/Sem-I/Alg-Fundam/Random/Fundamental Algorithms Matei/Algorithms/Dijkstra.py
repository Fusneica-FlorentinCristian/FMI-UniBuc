import sys
import queue
import ReadGraphFromFile


def dijkstra(someList, start):
    n = len(someList)
    distance = [sys.maxsize] * n
    distance[start] = 0
    v = []
    pqueue = queue.PriorityQueue()
    pqueue.put((0, start))

    while not pqueue.empty():
        node = pqueue.get()[1]
        if node not in v:
            v.append(node)
            for x in someList[node]:
                next = x[0]
                cost = x[1]
                if distance[next] > distance[node] + cost:
                    distance[next] = distance[node] + cost
                    pqueue.put((distance[next], next))
    result = []
    for i in range(n):
        result.append((i, distance[i]))
    return result


m, n, listAlg = ReadGraphFromFile.readWeightedFile()
lista = ReadGraphFromFile.listaAdiacenta(n, listAlg, "neorientat")

print(dijkstra(lista, 0))
