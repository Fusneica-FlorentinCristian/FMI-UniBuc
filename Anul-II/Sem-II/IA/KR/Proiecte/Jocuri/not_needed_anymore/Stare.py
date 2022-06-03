from not_needed_anymore.Joc import Joc

class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    O instanta din clasa stare este un nod din arborele minimax
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Game sa fie definiti MIN_PLAYER si MAX_PLAYER (cei doi jucatori posibili)
    De asemenea cere ca in clasa Game sa fie definita si o metoda numita mutari() care ofera lista cu configuratiile posibile in urma mutarii unui jucator
    """

    # TO DO 2
    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, estimare=None):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        # adancimea in arborele de stari
        self.adancime = adancime

        # estimarea favorabilitatii starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.estimare = estimare

        # lista de mutari posibile (tot de tip State) din starea curenta
        self.mutari_posibile = []

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        # e de tip State (cel mai bun succesor)
        self.stare_aleasa = None

    def mutari(self):
        l_mutari = self.tabla_joc.all_possible_moves(self.j_curent, )  # lista de informatii din nodurile succesoare
        joc_opus = Joc.jucator_opus(self.j_curent)

        # mai jos calculam lista de nodes-fii (succesori)
        l_stari_mutari = [Stare(mutare, joc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Jucator curent:" + self.j_curent + ")\n"
        return sir