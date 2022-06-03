def readUnweightedFile():
    f = open("graf.in", "r")
    listAlg = []

    line = f.readline()
    noduri = int(line.split()[0])
    muchii = int(line.split()[1])

    for i in range(muchii):
        line = f.readline()
        listAlg.append((int(line.split()[0]), int(line.split()[1])))

    v = int(f.readline())
    f.close()
    return noduri, muchii, listAlg, v



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


def DFS(start, someList):
    v = []
    stack = []
    v.append(start)
    stack.append(start)

    while len(stack) != 0:
        s = stack.pop()
        if s not in v:
            v.append(s)
        for i in someList[s]:
            if i not in v and i not in stack:
                stack.append(i)

    return v


