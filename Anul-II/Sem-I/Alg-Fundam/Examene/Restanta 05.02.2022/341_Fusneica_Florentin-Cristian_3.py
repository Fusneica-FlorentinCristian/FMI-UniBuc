# a)

list = []
left = []
right = []
f = open("graf3.in", "r")

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

for l in f:
    if int(l.split()[0]) in left:
        if int(l.split()[1]) not in right:
            right.append(int(l.split()[1]))
    elif int(l.split()[0]) in right:
        if int(l.split()[1]) not in left:
            left.append(int(l.split()[1]))
    elif int(l.split()[1]) in right:
        if int(l.split()[0]) not in left:
            left.append(int(l.split()[0]))
    elif int(l.split()[1]) in left:
        if int(l.split()[0]) not in right:
            right.append(int(l.split()[0]))
    else:
        right.append(int(l.split()[1]))
        left.append(int(l.split()[0]))
k = 5

print("pentru k=" + str(k))
print("asocieri proiect-student")
print(right, left)
for i in range(k):
    # i = 0 <=> proiect 1, la print adaug artificial +1 ca sa arate corect
    print(i + 1, right[i])

# b) ar trebui sparta problema ca una de fluxuri, cu doua "coloane" intermediare
# fluxul care vine dinspre student (in cazul exemplului, = 2) spre coloana intermediara I
# coloana intermediara I, care poate sa trimita flux de cel mult 1 (ca poate lucra la acelasi proiect de 2 ori) inspre coloana intermediara II
# coloana intermediara II, care trimite catre proiectele fluxul pe care il primeste fiecare proiect (in cazul exemplului, accepta 2 studenti per proiect)
# cu noul graf de fluxuri, se poate aplica Edmonds Karp pe el, cu fiecare start
# astfel se putea rezolva di subpunctul a), unde fluxul era 1 de la studenti, si 1 la proiect
import queue
import sys

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
