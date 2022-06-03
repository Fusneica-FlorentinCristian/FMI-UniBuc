from A_Star import *
import sys
import os
import copy


def coord_to_node(coord_x, coord_y, M):
    return M * coord_x + coord_y


def node_to_coord(node, M):
    return int(node / M), node % M


def adiacency_matrix(N, M):
    a_mat = np.zeros((N * M, N * M))
    #     print(N,M)
    for i in range(N):
        for j in range(M):
            node_number = coord_to_node(i, j, M)
            #             print(i, j, node_number)
            if j == 0:
                a_mat[node_number][node_number + 1] = 1
            elif j == M - 1:
                a_mat[node_number][node_number - 1] = 1
            else:
                a_mat[node_number][node_number + 1] = a_mat[node_number][node_number - 1] = 1

            if i == N - 1:
                #                 print(node_number, node_number - M)
                a_mat[node_number][node_number - M] = 1
            elif int(node_number / M) == 0:
                a_mat[node_number][node_number + M] = 1
            else:
                a_mat[node_number][node_number + M] = a_mat[node_number][node_number - M] = 1
    return a_mat


def adiacency_matrix_weights(N, M, costs):
    a_mat = np.zeros((N * M, N * M))
    #     print(N,M)
    for i in range(N):
        for j in range(M):
            node_number = coord_to_node(i, j, M)
            #             print(i, j, node_number)
            if j == 0:
                a_mat[node_number][node_number + 1] = costs[node_number + 1] + 1
            elif j == M - 1:
                a_mat[node_number][node_number - 1] = costs[node_number - 1] + 1
            else:
                a_mat[node_number][node_number + 1] = costs[node_number + 1] + 1
                a_mat[node_number][node_number - 1] = costs[node_number - 1] + 1

            if i == N - 1:
                #                 print(node_number, node_number - M)
                a_mat[node_number][node_number - M] = costs[node_number - M] + 1
            elif i == 0:
                a_mat[node_number][node_number + M] = costs[node_number + M] + 1
            else:
                a_mat[node_number][node_number + M] = costs[node_number + M] + 1
                a_mat[node_number][node_number - M] = costs[node_number - M] + 1
    return a_mat


def build_vect_h(matrix, scopes=None, N=None, M=None):
    vect_h = []
    if N is None or M is None:
        N = len(matrix)
        M = len(matrix[0])
    for i in range(N):
        for j in range(M):
            cost = 0
            probably_closest_node = scopes[0]
            i_node = probably_closest_node[0]
            j_node = probably_closest_node[1]
            j_cost = abs(j_node - j)
            i_cost = abs(i_node - i)
            # print((i, i_node), (j, j_node))
            for line in range(min(i, i_node), max(i, i_node) + 1):
                for column in range(min(j, j_node), max(j, j_node) + 1):
                    # print(matrix[line][column])
                    if matrix[line][column] > 0:
                        cost += matrix[line][column]
            cost += i_cost + j_cost
            vect_h.append(cost)
    return vect_h


def print_vect_h(vect_h, N, M):
    print(np.array(vect_h).reshape(N, M))


class NodParcurgere:
    graf = None  # static

    def __init__(self, id, info, parinte, cost, h):
        self.id = id  # este indicele din vectorul de noduri
        self.info = info
        self.parinte = parinte  # parintele din arborele de parcurgere
        self.g = cost  # costul de la radacina la nodul curent
        self.h = h
        self.f = self.g + self.h

    def obtineDrum(self):
        l = [self.info]
        nod = self
        while nod.parinte is not None:
            l.insert(0, nod.parinte.info)
            nod = nod.parinte
        return l

    def afisDrum(self):  # returneaza si lungimea drumului
        drum = self.obtineDrum()
        print(("->").join([str(node) for node in drum]))
        print("Cost: ", self.g)
        return len(drum)

    def get_destroyed_walls(self):
        destroyed_walls = []
        for elem in self.obtineDrum():
            if self.graf.costuri[elem] > 0:
                destroyed_walls.append(elem)
        return destroyed_walls

    def contineInDrum(self, infoNodNou):
        nodDrum = self
        while nodDrum is not None:
            if (infoNodNou == nodDrum.info):
                return True
            nodDrum = nodDrum.parinte

        return False

    def __repr__(self):
        sir = ""
        #         print(self.info)
        sir += str(self.info) + "("
        sir += "id = {}, ".format(self.id)
        sir += "drum="
        drum = self.obtineDrum()
        sir += ("->").join([str(node) for node in drum])
        sir += " g:{}".format(self.g)
        sir += " h:{}".format(self.h)

        sir += " f:{})".format(self.f)
        return sir


class Graph:  # graful problemei
    def __init__(self, noduri, matriceAdiacenta, costuri, start, scopuri, lista_h):
        self.noduri = noduri
        self.matriceAdiacenta = matriceAdiacenta
        self.costuri = costuri
        self.nrNoduri = len(matriceAdiacenta)
        self.start = start
        self.scopuri = scopuri
        self.lista_h = lista_h

    def indiceNod(self, n):
        return self.noduri.index(n)

    def testeaza_scop(self, nodCurent):
        #         print(nodCurent.info in self.scopuri)
        return nodCurent.info in self.scopuri

    # va genera succesorii sub forma de noduri in arborele de parcurgere
    def genereazaSuccesori(self, nodCurent):
        listaSuccesori = []
        for i in range(self.nrNoduri):
            if self.matriceAdiacenta[nodCurent.id][i] == 1 and not nodCurent.contineInDrum(self.noduri[i]):
                nodNou = NodParcurgere(i, self.noduri[i], nodCurent, nodCurent.g + self.costuri[nodCurent.id],
                                       self.calculeaza_h(self.noduri[i]))
                listaSuccesori.append(nodNou)
        return listaSuccesori

    def calculeaza_h(self, infoNod):
        return self.lista_h[self.indiceNod(infoNod)]

    def __repr__(self):
        sir = ""
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return sir


def a_star(gr, costs, nrSolutiiCautate=100, showQueue=False, NSOL=1):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.indiceNod(gr.start), gr.start, None, 0, gr.calculeaza_h(gr.start))]
    best_road = [c[0]]
    while len(c) > 0:
        if showQueue:
            print("Coada actuala: " + str(c))
        #             input()
        nodCurent = c.pop(0)
        if gr.testeaza_scop(nodCurent):
            #             print("Solutie: ")
            #             nodCurent.afisDrum()
            if (len([*filter(lambda x: x > nodCurent.g, [nod.g for nod in best_road])]) > 0 or best_road[0].g == 0) \
                    and not nodCurent.get_destroyed_walls() in [road.get_destroyed_walls() for road in best_road]:
                best_road.append(nodCurent)
                # print([node.g for node in best_road])
                best_road.sort(key=lambda x: x.g)
                if len(best_road) == NSOL + 1:
                    if best_road[0].g == 0:
                        best_road = best_road[1:NSOL + 1]
                    else:
                        best_road = best_road[:NSOL]
            #             print("\n----------------\n")
            #             input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                # print(f"Cea mai buna solutie din {copie_nrSolutiiCautate} de solutii: ")
                # best_road.afisDrum()
                # if best_road[0].g == 0:
                #     return best_road[1:NSOL + 1]
                # else:
                #     return best_road[:NSOL]
                best_road = list(
                    filter(lambda x: x.get_destroyed_walls() in [road.get_destroyed_walls() for road in best_road], best_road))
                return list(filter(lambda x: x.g != 0, best_road))

        lSuccesori = gr.genereazaSuccesori(nodCurent)
        for s in lSuccesori:
            i = 0
            gasit_loc = False
            for i in range(len(c)):
                # diferenta fata de UCS e ca ordonez dupa f
                if c[i].f > s.f:
                    gasit_loc = True
                    break
                elif c[i].f == s.f:
                    if s.g <= c[i].g:
                        s, c[i] = c[i], s
                    gasit_loc = True
                    break
            if gasit_loc:
                c.insert(i, s)
            else:
                c.append(s)

    # print(f"Cea mai buna solutie dupa ~{copie_nrSolutiiCautate - nrSolutiiCautate} solutii: ")
    # best_road.afisDrum()
    # print(str(len(best_road)) + " " + str(len(best_road[:NSOL])))
    best_road = list(filter(lambda x: x.g != 0, best_road))
    best_road.sort(key=lambda x: x.g)
    return best_road[:NSOL]


def BFS(a, start, M, N):
    nodes = []
    # Visited vector to so that a
    # vertex is not visited more than
    # once Initializing the vector to
    # false as no vertex is visited at
    # the beginning
    vertixes = M * N
    visited = [False] * vertixes
    q = [start]

    # Set source as visited
    visited[start] = True

    while q:
        vis = q[0]

        # Print current node
        # print(vis, end = ' ')
        nodes.append(vis)
        q.pop(0)

        # For every adjacent vertex to
        # the current vertex
        for i in range(vertixes):
            if (a[vis][i] == 1 or a[vis][i] == -1) and (not visited[i]):
                # Push the adjacent node
                # in the queue
                q.append(i)

                # set
                visited[i] = True
    return nodes


def flood(flooded_coords, a_mat, file=None):
    for (x, y) in flooded_coords:
        a_mat[x][y] = -1
    if file is None:
        print_matrix(a_mat)
    else:
        file.write("\n")
        for line in build_visual(a_mat):
            file.write(line + "\n")


def next_state(start, M, N, last_a_state, costs, output_file=None):
    last_state_mat_weighted = adiacency_matrix_weights(N, M, costs)
    flooded_nodes = BFS(last_state_mat_weighted, start, M, N)
    last_a_state_copy = copy.deepcopy(last_a_state)
    #     print(flooded_nodes)
    flooded_coords = [node_to_coord(node, M) for node in flooded_nodes]
    flood(flooded_coords, last_a_state_copy, output_file)
    return last_a_state_copy


def solve_solution(input_file_path, output_file_paths, NSOL=1):
    a, N, M, coord_robinet, coord_canal = read_file(input_file_path)
    if a is None:
        return
    add_costs(a, N, M)
    costs = np.array(a).flatten()

    a_mat = adiacency_matrix(N, M)
    a_mat_weighted = adiacency_matrix_weights(N, M, costs)

    vect_h = build_vect_h(a, coord_canal, N, M)
    noduri = list(range(0, N * M))
    start = coord_to_node(coord_robinet[0], coord_robinet[1], M)
    scopuri = [coord_to_node(scope[0], scope[1], M) for scope in coord_canal]

    gr = Graph(noduri, a_mat, costs, start, scopuri, vect_h)
    NodParcurgere.graf = gr
    best_road = a_star(gr, costs, showQueue=False, NSOL=NSOL)

    for i in range(len(best_road)):
        state = copy.deepcopy(a)
        destroyed_walls = best_road[i].get_destroyed_walls()
        # print(best_road[i].obtineDrum())

        flooded_nodes = BFS(a_mat_weighted, start, M, N)
        flooded_coords = [node_to_coord(node, M) for node in flooded_nodes]

        with open(output_file_paths[i], "w", encoding="utf-8") as f:
            f.write("1)")
            flood(flooded_coords, state, f)
            new_vect_h = build_vect_h(a, coord_canal, N, M)
            # print(costs)
            new_costs = copy.deepcopy(costs)
            for destroyed in range(len(destroyed_walls)):
                # print(i, destroyed)
                cost = destroyed_walls[destroyed]
                f.write("\nEliminăm obstacolul de la {}.".format(node_to_coord(cost, M)))
                f.write(f"\n{destroyed + 2})")
                new_costs = [new_costs[i] if i != cost else 0 for i in range(len(new_costs))]
                #     print(new_costs)
                state = next_state(start, M, N, state, new_costs, f)


if __name__ == "__main__":
    input_folder_path = sys.argv[1]
    output_folder_path = sys.argv[2]
    NSOL = int(sys.argv[3])
    timeout = int(sys.argv[4])
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)
    if not os.path.exists(input_folder_path):
        os.mkdir(input_folder_path)
    input_files = []
    for file in os.listdir(input_folder_path):
        input_files.append(os.path.join(input_folder_path, file))
    for input_file_path, input_file_name in zip(input_files, os.listdir(input_folder_path)):
        output_file_paths = [os.path.join(output_folder_path, input_file_name + f"_{i}.out") for i in range(NSOL)]
        # print(len(output_file_paths))
        solve_solution(input_file_path, output_file_paths, NSOL=NSOL)
