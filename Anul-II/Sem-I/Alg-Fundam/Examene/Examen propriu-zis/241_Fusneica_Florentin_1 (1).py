import sys
import queue

def ListaAdiacenta(n,m,list,o):
    listaNoua = [[]for i in range(n)]

    if o == "neorientat":
        for i in list:
            # adaug in Dijkstra weight = 1
            listaNoua[i[0]].append((i[1],1))
            listaNoua[i[1]].append((i[0],1))
    elif o == "orientat":
        for i in list:
            listaNoua[i[0]].append((i[1],1))

    return listaNoua


def Dijkstra(list, start):
    n = len(list)
    distance = [sys.maxsize]*n
    distance[start] = 0
    v = []
    pqueue = queue.PriorityQueue()
    pqueue.put((0, start))

    while not pqueue.empty():
        node = pqueue.get()[1]
        if node not in v:
            v.append(node)
            for x in list[node]:
                next = x[0]
                cost = x[1]
                if distance[next] > distance[node] + cost:
                    distance[next] = distance[node] + cost
                    pqueue.put((distance[next],next))
    result = []
    for i in range(n):
        result.append((i + 1,distance[i]))
    return result



f = open("graf.in","r")
list = []

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

l = f.readline()
while l:
    list.append((int(l.split()[0])-1, int(l.split()[1])-1))
    l = f.readline()
f.close()
listaAd = ListaAdiacenta(n,m,list,"neorientat")

listaDijkstra = Dijkstra(listaAd,0)
print(listaDijkstra)

T = []
for i in listaDijkstra:
    if(i[1] < sys.maxsize):
        if(i[1] == 1):
            T.append((1, int(i[0])))

print(T)