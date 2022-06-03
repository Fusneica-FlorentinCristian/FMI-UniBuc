import sys
import queue
import ReadGraphFromFile

visited = []


def BFS_EdmondsKarp(start, someList, finish, tati, rest):
    q = queue.Queue()
    q.put(start)
    global visited
    visited = [start]

    while not q.empty():
        nod = q.get()
        for j in someList[nod]:
            index = j[0]
            if rest[nod][index] and index not in visited:
                visited.append(index)
                tati[index] = nod
                if index != finish:
                    q.put(index)
    return finish in visited


def EK(start, finish, someList, n, rest):
    tati = [0] * (n + 1)
    global visited
    flow = 0
    while BFS_EdmondsKarp(start, someList, finish, tati, rest):
        for i in someList[n]:
            index = i[0]
            if index in visited and rest[index][n]:
                x = sys.maxsize
                tati[n] = index
                j = n
                while j != start:
                    x = min(x, rest[tati[j]][j])
                    j = tati[j]
                j = n
                while j != start:
                    rest[tati[j]][j] -= x
                    rest[j][tati[j]] += x
                    j = tati[j]
                flow += x
    return flow


f = open("zgrafpondEdmonds-Karp.in", "r")
lista = []

n = int(f.readline())
line = f.readline()
start = int(line.split()[0])
finish = int(line.split()[1])
m = int(f.readline())

rest = [[0] * (n + 1) for i in range(n + 1)]

line = f.readline()
while line:
    lista.append((int(line.split()[0]), int(line.split()[1]), int(line.split()[2])))
    rest[int(line.split()[0])][int(line.split()[1])] = int(line.split()[2])
    line = f.readline()

listaAdiacenta = ReadGraphFromFile.listaAdiacenta(n, lista, "neorientat")

print(EK(1, 6, listaAdiacenta, n, rest))
f.close()
