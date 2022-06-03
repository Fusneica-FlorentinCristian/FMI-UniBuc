import sys
import queue


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


def listaAdiacenta(nodes, someList):
    matrix = [[] for i in range(nodes)]
    for i in someList:
        matrix[i[0] - 1].append(i[1])
        matrix[i[1] - 1].append(i[0])
    return matrix


f = open("graf.in", "r")
listaInscrieri = []
visited = []

line = f.readline()
nProjects = int(line.split()[0])
mStudents = int(line.split()[1])
flowStudent = [[0] * (nProjects + 1) for i in range(nProjects + 1)]
flowProiect = [[0] * (nProjects + 1) for i in range(nProjects + 1)]
proiectPerStudent = 1
studentPerProiect = 1

line = f.readline()
while line:
    proiect = int(line.split()[0])
    student = int(line.split()[1])
    listaInscrieri.append((int(line.split()[0]), int(line.split()[1])))
    flowStudent[student][proiect] = 1
    line = f.readline()
f.close()
# --------------------------------------------
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

listaAdiacenta = listaAdiacenta(n, lista, "neorientat")

print(EK(1, 6, listaAdiacenta, n, rest))
# ----------------------------------------------

listaAdiacenta = listaAdiacenta(nProjects, listaInscrieri)

print(listaInscrieri)
print(listaAdiacenta)
# print(EK(1, 6, listaAdiacenta, nProjects, flowStudent))
