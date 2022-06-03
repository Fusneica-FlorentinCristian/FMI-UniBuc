import sys
import ReadGraphFromFile


def FW(w, node):
    distance = w
    tati = [[-1] * node for i in range(node)]

    for i in range(node):
        for j in range(node):
            distance[i][j] = w[i][j]
            if w[i][j] == 0 or w[i][j] == sys.maxsize:
                tati[i][j] = -1
            else:
                tati[i][j] = i

    for k in range(node):
        for i in range(node):
            for j in range(node):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    tati[i][j] = tati[k][j]
    return distance


n, m, matrix = ReadGraphFromFile.adjacencyDirectedMatrixWeighted()

print(*FW(matrix, n), sep="\n")
