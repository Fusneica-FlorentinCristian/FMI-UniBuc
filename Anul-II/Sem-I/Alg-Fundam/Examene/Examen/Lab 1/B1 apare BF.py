import queue


def BFS(start, list):
    v = []
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        nod = q.get()
        if nod not in v:
            v.append(nod)
            for i in list[nod - 1]:
                q.put(i)

    return v


def BFS2(start, list, control):
    v = []
    tati = [-1] * len(list)
    q = queue.Queue()
    q.put(start)
    rez = []
    while not q.empty():
        nod = q.get()

        if nod in control:
            while nod != -1:
                rez.append(nod)
                nod = tati[nod - 1]
            return rez
        if nod not in v:
            v.append(nod)
            for i in list[nod - 1]:
                if i not in v:
                    q.put(i)
                    tati[i - 1] = nod


# def lista_adiacenta(n, m, list, o):
#     matx = [[] for i in range(n)]
#
#     if o == "neorientat":
#         for i in list:
#             matx[i[0] - 1].append(i[1])
#             matx[i[1] - 1].append(i[0])
#     elif o == "orientat":
#         for i in list:
#             matx[i[0] - 1].append(i[1])
#
#     return matx

def lista_adiacenta(n, m, list, o):
    matx = [[] for i in range(n)]

    if o == "neorientat":
        for i in list:
            matx[i[0] - 1].append(i[1])
            matx[i[1] - 1].append(i[0])
    elif o == "orientat":
        for i in list:
            matx[i[0] - 1].append(i[1])

    return matx

f = open("graf.in", "r")
list = []
control = []
o = "neorientat"

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

for i in range(m):
    l = f.readline()
    list.append((int(l.split()[0]), int(l.split()[1])))

l = f.readline()
for i in l.split():
    control.append(int(i))

# a = int(input("Punct de plecare: "))-1
starting_node = 1

list_ad = lista_adiacenta(n, m, list, o)

# bf care pleaca de la nodul "a" din lista de adiacenta "lista"
#bf = BFS(a, list_ad)

result = BFS2(starting_node, list_ad, control)

f.close()

f = open("graf.out", "w")

for i in range(len(result) - 1, -1, -1):
    f.write(str(result[i]) + " ")

# print(bf)
# print (list)
# print(control)
# print(a)
for i in range(len(result) - 1, -1, -1):
    print(result[i])
f.close()