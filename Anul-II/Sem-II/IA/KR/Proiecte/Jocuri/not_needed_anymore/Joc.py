import copy


class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_COLOANE = 3
    JMIN = None  # alegere jucator
    JMAX = None  # calculator
    GOL = '#'

    def __init__(self, tabla=None):  # Game()
        self.matr = tabla or [Joc.GOL] * self.NR_COLOANE ** 2
        # print(self.matr)

    @classmethod
    def jucator_opus(cls, jucator):
        # val_true if conditie else val_false
        return cls.JMAX if jucator == cls.JMIN else cls.JMIN

    def elem_identice(self, lista):
        if len(set(lista)) == 1:
            return lista[0] if lista[0] != self.GOL else False
        return False

    # TO DO 5
    def final(self):  # [0,1,2,3,4,5,6,7,8]
        """
        012
        345
        678
        """
        rez = (self.elem_identice(self.matr[0:3])
               or self.elem_identice(self.matr[3:6])
               or self.elem_identice(self.matr[6:9])
               or self.elem_identice(self.matr[0:9:3])
               or self.elem_identice(self.matr[1:9:3])
               or self.elem_identice(self.matr[2:9:3])
               or self.elem_identice(self.matr[0:9:4])
               or self.elem_identice(self.matr[2:8:2]))
        if rez:
            return rez
        elif Joc.GOL not in self.matr:
            return 'remiza'
        else:
            return False

    # TO DO 3,6
    def mutari(self, jucator):  # jucator = simbolul jucatorului care muta
        l_mutari = []
        for i in range(len(self.matr)):
            if self.matr[i] == Joc.GOL:
                copie_matr = copy.deepcopy(self.matr)
                copie_matr[i] = jucator
                l_mutari.append(Joc(copie_matr))
        return l_mutari

    # linie deschisa inseamna linie pe care jucatorul mai poate forma o configuratie castigatoare
    # practic e o linie fara simboluri ale jucatorului opus
    def linie_deschisa(self, lista, jucator):
        jo = self.jucator_opus(jucator)
        # verific daca pe linia data nu am simbolul jucatorului opus
        if jo not in lista:
            # return lista.count(jucator)
            return 1
        return 0

    def linii_deschise(self, jucator):
        return self.linie_deschisa(self.matr[0:3], jucator) + self.linie_deschisa(self.matr[3:6],
                                                                                  jucator) + self.linie_deschisa(
            self.matr[6:9], jucator) + self.linie_deschisa(self.matr[0:9:3], jucator) + self.linie_deschisa(
            self.matr[1:9:3], jucator) + self.linie_deschisa(self.matr[2:9:3], jucator) + self.linie_deschisa(
            self.matr[0:9:4], jucator) + self.linie_deschisa(self.matr[2:7:2], jucator)

    # TO DO 7
    def estimeaza_scor(self, adancime):
        t_final = self.final()
        # if (depth==0):
        if t_final == self.__class__.JMAX:  # self.__class__ referinta catre clasa instantei
            return 99 + adancime
        elif t_final == self.__class__.JMIN:
            return -99 - adancime
        elif t_final == 'remiza':
            return 0
        else:
            return self.linii_deschise(self.__class__.JMAX) - self.linii_deschise(self.__class__.JMIN)

    def sirAfisare(self):
        sir = "  |"
        sir += " ".join([str(i) for i in range(self.NR_COLOANE)]) + "\n"
        sir += "-" * (self.NR_COLOANE + 1) * 2 + "\n"
        for i in range(self.NR_COLOANE):  # itereaza prin linii
            sir += str(i) + " |" + " ".join(
                [str(x) for x in self.matr[self.NR_COLOANE * i: self.NR_COLOANE * (i + 1)]]) + "\n"
        # [0,1,2,3,4,5,6,7,8]
        return sir

    def __str__(self):
        return self.sirAfisare()

    def __repr__(self):
        return self.sirAfisare()
