import sys
import os
import copy
import numpy as np
from time import time

directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1], [0, 0]]
corner_directions = [[-1, -1], [1, 1], [-1, 1], [1, -1]]


def print_matrix_weights(m):
    for i in m:
        print(' '.join(str(i)))


def build_visual_array(m):
    return np.array(["o" if elem == 0 else "#" if elem >= 0 else "i" for line in m for elem in line]).reshape(len(m),
                                                                                                              len(m[0]))


def build_visual(m):
    return ["".join(line) for line in build_visual_array(m)]


def print_matrix(m):
    for line in build_visual(m):
        print(line)


def add_costs(a, N, M):
    for i in range(N):
        for j in range(M):
            if a[i][j] != 0:
                count = 0
                for variation in range(len(directions)):
                    row = i + directions[variation][0]
                    col = j + directions[variation][1]
                    if not (row < 0 or row == N or col < 0 or col == M or a[row][col] == 0):
                        count += 1
                a[i][j] = count


def read_file(file_name="date.in"):
    with open(file_name, encoding="utf-8") as f:
        lines = f.readlines()
    coord_robinet = (int(lines[0].split()[0]), int(lines[0].split()[1]))
    #     print(lines[1].split())
    coord_canal = list(zip(*(iter([int(elem) for elem in lines[1].split()]),) * 2))

    #     coord_canal = (int(lines[1].split()[0]), int(lines[1].split()[1]))

    N = len(lines) - 2
    M = len(lines[2].split()[0])
    #     print(N, M)
    # print(coord_robinet, coord_canal)
    a = []
    for i in range(2, len(lines)):
        someList = []
        for info in lines[i].split()[0]:
            if info == 'o':
                someList.append(0)
            else:
                someList.append(-1)
        if len(someList) != M:
            return None, N, M, coord_robinet, coord_canal
        a.append(someList)
    return a, N, M, coord_robinet, coord_canal


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


def build_vect_h_banal(N, M):
    return [0] * (N * M)


def build_vect_h_admis1(costs, flattened=True):
    if flattened:
        return [item if item == 0 else 1 for list_item in costs for item in list_item]
    else:
        return [[item if item == 0 else 1 for item in list_item] for list_item in costs]


def check_for_zeros(i, j, costs_copy, N, M, costs):
    for direction in corner_directions:
        if 0 <= i + direction[0] < N and 0 <= j + direction[1] < M:
            if costs[i + direction[0]][j + direction[1]] == 0 and \
                    costs[i][j + direction[1]] != 0 and costs[i + direction[0]][j] != 0 \
                    and costs[i][j + direction[1]] != costs[i + direction[0]][j]:
                if costs[i][j + direction[1]] > costs[i + direction[0]][j]:
                    costs_copy[i + direction[0]][j] = 0
                else:
                    costs_copy[i][j + direction[1]] = 0
    return costs_copy


def build_vect_h_admis2(matrix):
    h = build_vect_h_admis1(matrix, flattened=False)
    M = len(matrix[0])
    N = len(matrix)
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                h = check_for_zeros(i, j, h, N, M, matrix)
    return np.array(h).flatten()


def build_vect_h_neadmis1(matrix, scopes=None, N=None, M=None):
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
    def genereazaSuccesori(self, nodCurent, counter=1):
        listaSuccesori = []
        for i in range(self.nrNoduri):
            if self.matriceAdiacenta[nodCurent.id][i] == 1 and not nodCurent.contineInDrum(self.noduri[i]):
                nodNou = NodParcurgere(i, self.noduri[i], nodCurent, nodCurent.g + self.costuri[nodCurent.id],
                                       self.calculeaza_h(self.noduri[i]))
                counter += 1
                listaSuccesori.append(nodNou)
        return listaSuccesori, counter

    def calculeaza_h(self, infoNod):
        return self.lista_h[self.indiceNod(infoNod)]

    def __repr__(self):
        sir = ""
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return sir


def a_star(gr, nrSolutiiCautate=100, showQueue=False, NSOL=1, counter=1):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.indiceNod(gr.start), gr.start, None, 0, gr.calculeaza_h(gr.start))]
    max_nodes = len(c)
    best_road = [c[0]]
    while len(c) > 0:
        max_nodes = max(max_nodes, len(c))
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
                    filter(lambda x: x.get_destroyed_walls() in [road.get_destroyed_walls() for road in best_road],
                           best_road))
                return list(filter(lambda x: x.g != 0, best_road)), max_nodes, counter

        lSuccesori, counter = gr.genereazaSuccesori(nodCurent, counter)
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
    return best_road[:NSOL], max_nodes, counter


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
    start_time = time()
    a, N, M, coord_robinet, coord_canal = read_file(input_file_path)
    if a is None:
        return
    add_costs(a, N, M)
    costs = np.array(a).flatten()
    # print_matrix_weights(a)

    a_mat = adiacency_matrix(N, M)
    a_mat_weighted = adiacency_matrix_weights(N, M, costs)

    # vect_h = build_vect_h_neadmis1(a, coord_canal, N, M)
    # vect_h = build_vect_h_banal(N, M)
    # vect_h = build_vect_h_admis1(a)
    heuristics_list = [build_vect_h_neadmis1(a, coord_canal, N, M), build_vect_h_banal(N, M), build_vect_h_admis1(a),
                       build_vect_h_admis2(a)]
    for index, vect_h in enumerate(heuristics_list):
        # print_vect_h(vect_h, N, M)

        noduri = list(range(0, N * M))
        start = coord_to_node(coord_robinet[0], coord_robinet[1], M)
        scopuri = [coord_to_node(scope[0], scope[1], M) for scope in coord_canal]

        gr = Graph(noduri, a_mat, costs, start, scopuri, vect_h)
        NodParcurgere.graf = gr
        best_roads, max_nodes, node_counter = a_star(gr, showQueue=False, NSOL=NSOL)

        for i in range(len(best_roads)):
            flooded_nodes = BFS(a_mat_weighted, start, M, N)
            flooded_coords = [node_to_coord(node, M) for node in flooded_nodes]
            final_state = coord_robinet in flooded_coords and set(flooded_coords).intersection(set(coord_canal))

            path_w = output_file_paths[i] + f"_h{index}.out"

            with open(path_w, "w", encoding="utf-8") as f:
                print(path_w + ":")
                if final_state:
                    print(f"IT IS ALREADY FINAL STATE, so:\n"
                          f"Length of \"road\": number of flooded nodes: {len(flooded_nodes)}.\n"
                          f"The road as order numbers: the flooded nodes: {flooded_nodes}.\n"
                          f"The road as coords: {flooded_coords}.\n"
                          f"Total cost for solution: {0}.\n"
                          f"Time for solution: {time() - start_time} seconds.\n"
                          f"Most nodes at one time in memory: {max_nodes}.\n"
                          f"Total number of calculated nodes: {node_counter}"
                          f"\n--------------------------------------------------"
                          f"-----------------------------------------\n")
                    return
                state = copy.deepcopy(a)
                destroyed_walls = best_roads[i].get_destroyed_walls()
                new_costs = copy.deepcopy(costs)
                f.write("1)")
                flood(flooded_coords, state, f)
                # CHECK IF STARTING STATE IS THE FINAL STATE

                print(f"Length of \"road\": {len(best_roads[i].obtineDrum())}.\n"
                      f"The road as order numbers: {best_roads[i].obtineDrum()}.\n"
                      f"Total cost for solution: {sum([new_costs[destroyed] for destroyed in destroyed_walls])}.\n"
                      f"Time for solution: {time() - start_time} seconds.\n"
                      f"Most nodes at one time in memory: {max_nodes}.\n"
                      f"Total number of calculated nodes: {node_counter}")
                # print(costs)
                for destroyed in range(len(destroyed_walls)):
                    # print(i, destroyed)
                    cost = destroyed_walls[destroyed]
                    print("Cost for destroyed wall at {}:".format(node_to_coord(cost, M)), new_costs[cost])
                    f.write("\nEliminăm obstacolul de la {}.".format(node_to_coord(cost, M)))
                    f.write(f"\n{destroyed + 2})")
                    new_costs = [new_costs[i] if i != cost else 0 for i in range(len(new_costs))]
                    #     print(new_costs)
                    state = next_state(start, M, N, state, new_costs, f)
            print("\n-------------------------------------------------------------------------------------------\n")


if __name__ == "__main__":
    input_folder_path = sys.argv[1]
    output_folder_path = sys.argv[2]
    NSOL = int(sys.argv[3])
    timeout = int(sys.argv[4])

    if not os.path.exists(input_folder_path):
        os.mkdir(input_folder_path)
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)

    input_files_paths = []
    input_files_names = []
    for file in os.listdir(input_folder_path):
        input_files_paths.append(os.path.join(input_folder_path, file))
        input_files_names.append(file)

    # print(input_files_names)
    for input_file_path, input_file_name in zip(input_files_paths, input_files_names):
        output_files_paths = [os.path.join(output_folder_path, input_file_name + f"_{i}") for i in range(NSOL)]
        # print(len(output_file_paths))
        solve_solution(input_file_path, output_files_paths, NSOL=NSOL)
