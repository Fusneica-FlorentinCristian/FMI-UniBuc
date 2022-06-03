def readInput():
    with open('graf2.in', 'rt') as f:
        n, m = f.readline().split()
        d = dict()
        for _ in range(int(m)):
            a = f.readline().split()
            a = (int(a[0]) - 1, int(a[1]) - 1, int(a[2]),)
            if a[0] not in d:
                d[a[0]] = {a[1]: a[2]}
            else:
                d[a[0]][a[1]] = a[2]
        a = []
        for v in f.readline().split():
            a.append(int(v) - 1)
        b = f.readline().split()
        return d, a[1:], [int(b[0]) - 1, int(b[1]) - 1], int(n)


def isCyclic(node, visited, completed, graph):
    visited[node] = completed[node] = True
    if node not in graph:
        completed[node] = False
        return False
    for v in graph[node]:
        if not visited[v]:
            if isCyclic(v, visited, completed, graph):
                return True
        elif completed[v]:
            return True
    completed[node] = False
    return False


def isCyclicMain(graph, n):
    visited = [False for _ in range(n)]
    completed = [False for _ in range(n)]

    for node in range(n):
        if not visited[node]:
            if isCyclic(node, visited, completed, graph):
                return "Are circuite !"

    return "Nu are circuite !"


def findMaxCost(node, n, graph):
    distance = [-1e7 for _ in range(n)]
    distance[node] = 0
    visited = [False for _ in range(n)]
    for node in range(n):
        m = -1e7
        for v in range(n):
            if distance[v] > m and not visited[v]:
                m = distance[v]
                index = v
        visited[index] = True
        for v in range(n):
            if index in graph and v in graph[index] and not visited[v] and distance[v] < distance[index] + \
                    graph[index][v]:
                distance[v] = distance[index] + graph[index][v]
    return distance


def findBestPath(graph, n, S, T):
    m = -1e7
    for s in S:
        d = findMaxCost(s, n, graph)
        for t in T:
            if d[t] > m:
                m = d[t]
    return m


graph, S, T, n = readInput()
# print(graph, S, T)
print(isCyclicMain(graph, n))

# print(findMaxCost(int(S[0]), n, graph))

print(findBestPath(graph, n, S, T))
