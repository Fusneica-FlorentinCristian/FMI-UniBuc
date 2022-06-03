def listToInt(list):
    return [int(elem) for elem in list]


def changeIndexing(value):
    return value - 1


def unchangeIndexing(value):
    return value + 1


def cycleDetect(startPoint, nodeList, visited, chain, depth=1):
    # print(visited, chain, depth)
    chains = []
    for node in nodeList[startPoint]:
        if visited[node] == 0:
            chain.append(node)
            visited[node] = depth
            result = cycleDetect(node, nodeList, visited, chain, depth + 1)
            print(result)
            chains.extend(result)
            visited[node] = 0
            chain.pop()
        elif visited[node] < depth:
            chain.append(node)
            return [chain]

    return chains


with open("graf.in", "r") as inputFile:
    readInput = inputFile.read()
    readInput = readInput.split("\n")
    readInput = [line.split(" ") for line in readInput]

    n, m = listToInt(readInput[0])

    nodesList = [[] for _ in range(0, n)]
    for i in range(1, m + 1):
        a, b = listToInt(readInput[i])
        a, b = changeIndexing(a), changeIndexing(b)

        nodesList[a].append(b)
        nodesList[b].append(a)
    # print(nodesList)

    chainList = cycleDetect(0, nodesList, [0 if x != 0 else 1 for x in range(n)], [0, ], 1)
    # print(chainList)
    for chain in chainList:
        # print([unchangeIndexing(elem) for elem in chain])
        if len(chain) % 2 == 1:
            print([unchangeIndexing(elem) for elem in chain])
            chainList.remove(chain)
            break
    # print([unchangeIndexing(elem) for elem in chainList[0]])
