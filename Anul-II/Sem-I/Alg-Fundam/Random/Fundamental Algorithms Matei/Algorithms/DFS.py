import ReadGraphFromFile


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


def DFS_recursive(start, someList, visited, result):
    visited.append(start)

    for i in someList[start]:
        if i[0] not in visited:
            DFS_recursive(i[0], someList, visited, result)

    result.append(start)


m, n, listAlg = ReadGraphFromFile.readUnweightedFile()
lista = ReadGraphFromFile.listaAdiacenta(n, listAlg, "neorientat")

dfs = DFS(0, lista)
print([elem + 1 for elem in dfs])
