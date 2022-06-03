import sys


def FW(w, n, noduri_start, t1, t2):
    distance = w
    tati = [[-1] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            distance[i][j] = w[i][j]
            if w[i][j] == 0 or w[i][j] == -sys.maxsize - 1:
                tati[i][j] = -1
            else:
                tati[i][j] = i

    list = []

    for k in range(n):
        for i in range(n):
            if i + 1 in noduri_start:
                for j in range(n):
                    if distance[i][j] < distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
                        tati[i][j] = tati[k][j]
                break
    list.append(noduri_start[0])
    valori_maxim_nod_start = [None] * n
    for i in range(n):
        valori_maxim_nod_start[i] = distance[noduri_start[0] - 1][i]
    valori_maxim_nod_start = valori_maxim_nod_start.reverse()

    return distance, list


f = open("graf2.in", "r")
list = []

l = f.readline()
n = int(l.split()[0])

weights = [None]*n

l = f.readline()
for i in range(n):
    weights[i] = int(l.split()[i])
l = f.readline()
muchii = int(l.split()[0])
numar_noduri_start = int(l.split()[1])
matrice_adiacenta = [[-sys.maxsize - 1]*n for i in range(n)]
for i in range(n):
    matrice_adiacenta[i][i] = 0

for i in range(muchii):
    l = f.readline()
    matrice_adiacenta[int(l.split()[0]) - 1][int(l.split()[1]) - 1] = weights[int(l.split()[0]) - 1]

l = f.readline()
noduri_start = [None] * numar_noduri_start
for i in range(numar_noduri_start):
    noduri_start[i] = int(l.split()[i])

l = f.readline()
t1 = int(l.split()[0])
t2 = int(l.split()[1])
matrice_drumuri_maxime, lista = FW(matrice_adiacenta, n, noduri_start, t1, t2)
print(*matrice_drumuri_maxime, sep="\n")
print(*lista, sep=" ")
f.close()