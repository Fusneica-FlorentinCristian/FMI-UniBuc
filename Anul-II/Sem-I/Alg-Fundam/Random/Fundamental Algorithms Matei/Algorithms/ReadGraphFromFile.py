import sys


def readWeightedFile():
    f = open("zgrafpond.in", "r")
    listAlg = []

    line = f.readline()
    nodes = int(line.split()[0])
    muchii = int(line.split()[1])

    line = f.readline()
    while line:
        listAlg.append((int(line.split()[0]) - 1, int(line.split()[1]) - 1, int(line.split()[2])))
        line = f.readline()

    f.close()
    return muchii, nodes, listAlg


def readUnweightedFile():
    f = open("zgraf.in", "r")
    listAlg = []

    line = f.readline()
    noduri = int(line.split()[0])
    muchii = int(line.split()[1])

    for i in range(muchii):
        line = f.readline()
        listAlg.append((int(line.split()[0]), int(line.split()[1])))

    f.close()
    return muchii, noduri, listAlg


def adjacencyDirectedMatrixWeighted():
    f = open("zgrafpond.in", "r")

    l = f.readline()
    n = int(l.split()[0])
    m = int(l.split()[1])
    list = [[sys.maxsize] * n for i in range(n)]
    for i in range(n):
        list[i][i] = 0

    l = f.readline()
    while l:
        list[int(l.split()[0]) - 1][int(l.split()[1]) - 1] = int(l.split()[2])
        l = f.readline()
    return list


def adjacencyMatrixUndirectedWeighted():
    f = open("zgrafpond.in", "r")

    l = f.readline()
    n = int(l.split()[0])
    m = int(l.split()[1])
    list = [[sys.maxsize] * n for i in range(n)]
    for i in range(n):
        list[i][i] = 0

    l = f.readline()
    while l:
        list[int(l.split()[0]) - 1][int(l.split()[1]) - 1] = list[int(l.split()[1]) - 1][int(l.split()[0]) - 1] = \
            int(l.split()[2])
        l = f.readline()
    return list


def adjacencyMatrixUndirectedUnweighted():
    f = open("zgrafpond.in", "r")

    l = f.readline()
    n = int(l.split()[0])
    m = int(l.split()[1])
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        matrix[i][i] = 0

    l = f.readline()
    while l:
        matrix[int(l.split()[0]) - 1][int(l.split()[1]) - 1] = \
            matrix[int(l.split()[1]) - 1][int(l.split()[0]) - 1] = 1
        l = f.readline()
    return n, m, matrix


def listaAdiacenta(n, someList, o):
    matrix = [[] for i in range(n)]

    if o == "neorientat":
        for i in someList:
            matrix[i[0] - 1].append(i[1] - 1)
            matrix[i[1] - 1].append(i[0] - 1)
    elif o == "orientat":
        for i in someList:
            matrix[i[0] - 1].append(i[1] - 1)

    return matrix
