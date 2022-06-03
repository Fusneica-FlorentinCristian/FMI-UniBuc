import copy
import sys
import time
import math
from itertools import product

def distance(n,m,matr,start):
    dist = 999999999999
    pair = []
    for k in range(n):
        for l in range(m):
            if matr[k][l][0] == 's':
                dist = min(dist,abs(start[0] - k) + abs(start[1] - l))
    for k in range(n):
        for l in range(m):
            if matr[k][l][0] == 's':
                if abs(start[0] - k) + abs(start[1] - l) == dist:
                    pair.append(k)
                    pair.append(l)
    return pair[0:2]

def nr_soareci(mat):
    nr = 0
    if (mat is None):
        return -1
    for i in mat:
        for j in i:
            if j[0] == 's' or j[0] == 'S':
                nr +=1
    return nr

class NodParcurgere:
    def __init__(self, info, parinte, cost=0, h=0):
        self.info = info
        self.parinte = parinte  # parintele din arborele de parcurgere
        self.g = cost  # consider cost=1 pentru o mutare
        self.h = h
        self.f = self.g + self.h

    def obtineDrum(self):
        l = [self];
        nod = self
        while nod.parinte is not None:
            l.insert(0, nod.parinte)
            nod = nod.parinte
        return l

    def afisDrum(self, afisCost=False, afisLung=False):  # returneaza si lungimea drumului
        l = self.obtineDrum()
        for nod in l:
            print(str(nod))
        if afisCost:
            print("Cost: ", self.g)
        if afisCost:
            print("Lungime: ", len(l))
        return len(l)

    def contineInDrum(self, infoNodNou):
        nodDrum = self
        while nodDrum is not None:
            if (infoNodNou == nodDrum.info):
                return True
            nodDrum = nodDrum.parinte

        return False


    def __repr__(self):
        sir = ""
        sir += str(self.info)
        return (sir)

    # euristica banală: daca nu e stare scop, returnez 1, altfel 0

    def __str__(self):
        sir = ""
        for linie in self.info:
            sir += " ".join([str(elem) for elem in linie]) + "\n"
        sir += "\n"
        return sir

class Graph:
    def __init__(self, nume_fisier):
        f = open(nume_fisier, 'r')
        self.k = None
        self.M = None
        self.mat = None
        self.nr_soarcei_evadati = None
        self.pisici = None
        self.soareci = None
        checkFile = f.readlines()
        if len(checkFile) > 0:
            self.k = int(checkFile[0])
            # acum voi incepe contruirea matricei
            # voi face pentru soareci si pisici cate o lista de tupluri in care le voi retine coordonatele
            camera = []
            for i in range(1, len(checkFile)):
                if i == len(checkFile) - 1:
                    camera.append(checkFile[i])
                else:
                    camera.append(checkFile[i][:-1])

            if len(camera) > 0:
                self.soareci = [None] * 100
                self.pisici = [None] * 100
                self.M = []
                i1 = 0
                i2 = 0
                for c in camera:
                    l = []
                    for el in c.split():
                        if el[0] == 's':
                            'fac conversia din string in int'
                            nr = 0
                            for i in el[1:]:
                                nr = nr * 10 + int(i)
                            self.soareci[nr] = (i1, i2)

                        elif el[0] == 'p':
                            nr = 0
                            for i in el[1:]:
                                nr = nr * 10 + int(i)
                            self.pisici[nr] = (i1, i2)
                        l.append(el)
                        i2 += 1
                    i2 = 0
                    i1 += 1
                    if l != []:
                        self.M.append(l)
                self.mat = self.M

    def genereazaSuccesori(self, nodCurent, tip_euristica="euristica banala"):
        # deplasarea soarecilor
        listaSuccesori = []
        listaPartiala = []
        len_s = 0
        l_directii = []
        for i in self.soareci:
            if i != None:
                len_s += 1
                ch = '.E@'
                directii = []
                # verific care directii de deplasare sunt disponibile pentru soarecele curent
                if i[1] - 1 >= 0:
                    if ch.find(self.M[i[0]][i[1] - 1]) != -1:
                        l_directii.append([i[0], i[1] - 1, len_s])
                if i[1] + 1 < len(self.M[0]):
                    if ch.find(self.M[i[0]][i[1] + 1]) != -1:
                        l_directii.append([i[0], i[1] + 1, len_s])
                if i[0] - 1 >= 0:
                    if ch.find(self.M[i[0] - 1][i[1]]) != -1:
                        l_directii.append([i[0] - 1, i[1], len_s])
                if i[0] + 1 < len(self.M):
                    if ch.find(self.M[i[0] + 1][i[1]]) != -1:
                        l_directii.append([i[0] + 1, i[1], len_s])


        p_c_in = list(product(l_directii, repeat=len_s))
        p_c_fin = []
        k = 0
        for el in p_c_in:
            if len(el) > 1:
                k += 1

                # ordonez dupa el[0][2]
                def check_el(x):
                    for i in range(len(x) - 1):
                        for j in range(i + 1, len(x)):
                            if x[i][2] == x[j][2]:
                                return False
                    return True

                if check_el(el):
                    p_c_fin.append(el)
        p_c_fin2 = []
        # eliminam  cazul in care soarecii nu sunt ordonati
        for el in p_c_fin:
            def check_el2(x):
                for i in range(len(x) - 1):
                    for j in range(i + 1, len(x)):
                        if x[i][2] > x[j][2]:
                            return False
                return True
            if check_el2(el):
                p_c_fin2.append(el)


        for stare in p_c_fin2:
            self.nr_soarcei_evadati = 0
            cM = copy.deepcopy(self.M)
            for i in range(len(cM)):
                for j in range(len(cM[i])):
                    if cM[i][j][0] == 's' or cM[i][j][0] == 'S' :
                        cM[i][j] = cM[i][j].lower()
                        nr = 0
                        for k in cM[i][j][1:]:
                            nr = nr * 10 + int(k)
                        # interschimbare
                        if cM[stare[nr][0]][stare[nr][1]] == '.':
                            aux = cM[stare[nr][0]][stare[nr][1]]
                            cM[stare[nr][0]][stare[nr][1]] = cM[i][j]
                            cM[i][j] = aux
                        elif cM[stare[nr][0]][stare[nr][1]] == 'E':
                            self.nr_soarcei_evadati += 1
                            # mesaj ca a iesit soarecele
                            cM[i][j] = '.'
                        elif cM[stare[nr][0]][stare[nr][1]] == '@':
                            # mesaj ca s-a ascuns soarecele

                            cM[stare[nr][0]][stare[nr][1]] = cM[i][j].upper()
                            cM[i][j] = '.'
            listaPartiala.append(cM)
        # pisicile se deplaseaza doar dupa ce au fost generati succesori in functie de mutarile soarecilor
        for mat in listaPartiala:
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if mat[i][j][0] == 'p':
                        nr = 0
                        for k in mat[i][j][1:]:
                            nr = nr * 10 + int(k)
                        # coordonatele celui mai apropiat soarece de pisica curenta
                        pair = distance(len(self.mat), len(self.mat[0]), self.mat, self.pisici[nr])
                        if (i < pair[0] and j < pair[1]):
                            mutare = 0
                            if (i + 1 < len(self.mat) and j + 1 < len(self.mat[0])):
                                if (mat[i + 1][j + 1] == '.' or mat[i + 1][j + 1][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i + 1][j + 1]
                                    mat[i + 1][j + 1] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1
                            if (j + 1 < len(mat[0])):
                                if (mat[i][j + 1] == '.' or mat[i][j + 1][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i][j + 1]
                                    mat[i][j + 1] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1
                            if (i + 1 < len(mat)):
                                if (mat[i + 1][j] == '.' or mat[i + 1][j][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i + 1][j]
                                    mat[i + 1][j] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1
                        if (i > pair[0] and j > pair[1]):
                            mutare = 0
                            if (i - 1 >= 0 and j - 1 >= 0):
                                if (mat[i - 1][j - 1] == '.' or mat[i - 1][j - 1][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i - 1][j - 1]
                                    mat[i - 1][j - 1] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1
                            if (j - 1 >= 0):
                                if (mat[i][j - 1] == '.' or mat[i][j - 1][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i][j - 1]
                                    mat[i][j - 1] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1
                            if (i - 1 >= 0):
                                if (mat[i - 1][j] == '.' or mat[i - 1][j][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i - 1][j]
                                    mat[i - 1][j] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1
                        if (i > pair[0] and j < pair[1]):
                            mutare = 0
                            if (i - 1 >= 0 and j + 1 < len(mat[0])):
                                if (mat[i - 1][j + 1] == '.' or mat[i - 1][j + 1][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i - 1][j + 1]
                                    mat[i - 1][j + 1] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1
                            if (j + 1 < len(mat[0])):
                                if (mat[i][j + 1] == '.' or mat[i][j + 1][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i][j + 1]
                                    mat[i][j + 1] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1
                            if (i - 1 >= 0):
                                if (mat[i - 1][j] == '.' or mat[i - 1][j][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i - 1][j]
                                    mat[i - 1][j] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1
                        if (i < pair[0] and j > pair[1]):
                            mutare = 0
                            if (i + 1 < len(mat) and j - 1 >= 0):
                                if (mat[i + 1][j - 1] == '.' or mat[i + 1][j - 1][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i + 1][j - 1]
                                    mat[i + 1][j - 1] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1
                            if (j - 1 >= 0):
                                if (mat[i][j - 1] == '.' or mat[i][j - 1][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i][j - 1]
                                    mat[i][j - 1] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1
                            if (i + 1 < len(mat)):
                                if (mat[i + 1][j] == '.' or mat[i + 1][j][0] == 's') and mutare == 0:
                                    aux = mat[i][j]
                                    mat[i][j] = mat[i + 1][j]
                                    mat[i + 1][j] = aux
                                    # mesaj ca soarecele a fost mancat
                                    if mat[i][j][0] == 's':
                                        mat[i][j] = mat[i][j][0] + 'd'
                                    mutare = 1



        for matr in listaPartiala:
            for i in range(len(matr)):
                for j in range(len(matr[0])):
                    if matr[i][j][0] == 's':
                        if matr[i][j][1] == 'd':
                            matr[i][j] = '.'
            self.mat = matr
            camera_copy = copy.deepcopy(self.mat)
            if not nodCurent.contineInDrum(camera_copy):
                listaSuccesori.append(NodParcurgere(camera_copy,nodCurent,nodCurent.g+1, self.calculeaza_h(camera_copy,tip_euristica)))

        return listaSuccesori

    def nuAreSolutii(self, matr):
        nrE = 0
        if(matr is None):
            return -1
        for i in range(len(matr)):
            for j in range(len(matr[0])):
                if matr[i][j] == 'E':
                    nrE+=1
        if nrE != 0:
            return 1
        return 0

    def testeaza_scop(self, infoNod, tip_euristica ="euristica banala"):
        if(nr_soareci(self.M) - nr_soareci(infoNod) >= self.k):
            return 1
        return 0

    def calculeaza_h(self,infoNod, tip_euristica="euristica banala"):
        if tip_euristica == "euristica banala":
            if self.testeaza_scop(infoNod,tip_euristica) == 1:
                return 1
        return 0

def uniform_cost(gr, timeout, nrSolutiiCautate=1):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    t_o = time.time()
    copy_mat = copy.deepcopy(gr.M)
    c = [NodParcurgere(copy_mat, None, 0, gr.calculeaza_h(copy_mat))]

    if gr.nuAreSolutii(gr.M) == 0:
        print("Nu are solutii!")
        return
    while len(c) > 0:
        current_time = time.time()
        if current_time - t_o > timeout:
            print("Timeout!")
            return

        nodCurent = c.pop(0)

        if gr.testeaza_scop(nodCurent):
            print("Solutie: ", end="")
            nodCurent.afisDrum()
            print("\n----------------\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent)
        for s in lSuccesori:
            i = 0
            gasit_loc = False
            for i in range(len(c)):
                # ordonez dupa cost(notat cu g aici și în desenele de pe site)
                if c[i].g > s.g:
                    gasit_loc = True
                    break;
            if gasit_loc:
                c.insert(i, s)
            else:
                c.append(s)

def a_star(gr, nrSolutiiCautate, timeout, tip_euristica):
    if(gr.M is None):
        print("Input file is not good")
        return
    t_o = time.time()
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    if gr.nuAreSolutii(gr.M) == 0:
        print("Nu are solutii!")
        return
    copy_mat = copy.deepcopy(gr.M)
    c = [NodParcurgere(copy_mat, None, 0, gr.calculeaza_h(copy_mat))]

    while len(c) > 0:
        current_time = time.time()
        if current_time - t_o > timeout:
            print("Timeout!")
            return
        nodCurent = c.pop(0)


        if gr.testeaza_scop(nodCurent.info):
            print("Solutie: ")
            nodCurent.afisDrum(afisCost=True, afisLung=True)
            print("\n----------------\n")
            input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent, tip_euristica=tip_euristica)
        print('Succesori: ',lSuccesori)
        for s in lSuccesori:
            i = 0
            gasit_loc = False
            for i in range(len(c)):
                # diferenta fata de UCS e ca ordonez dupa f
                if c[i].f >= s.f:
                    gasit_loc = True
                    break;
            if gasit_loc:
                c.insert(i, s)
            else:
                c.append(s)

# nume_f_input = input("Numele fisierului din care doriti sa cititi date: ")
nume_f_input = "text.in"
# nume_f_output = input("Numele fisierului de output: ")
nume_f_output = "text.out"
# numar_solutii = input("Numarul de solutii: ")
# numar_solutii = int(numar_solutii)
numar_solutii = 2
# timeout = input("Timp timeout: ")
# timeout = int(timeout)
timeout = 4
#nume_fisier_intrare = sys.argv[1]
#nume_fisier_iesire = sys.argv[2]
#nrSol = int(sys.argv[3])
#timeout = int(sys.argv[4])
gr=Graph(nume_f_input)
a_star(gr,numar_solutii,timeout,"euristica banala")
