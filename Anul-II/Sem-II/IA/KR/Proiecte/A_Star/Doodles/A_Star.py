import numpy as np

directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]


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
