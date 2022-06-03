import pygame
import sys
from helperClass import HelperClass


class Graph:
    # coordonatele nodurilor ()
    nodes = list(zip(
        [float(elem / 2) for elem in [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]],
        [float(elem / 2) for elem in [0, 3, 6, 1, 3, 5, 2, 3, 4, 0, 1, 2, 4, 5, 6, 2, 3, 4, 1, 3, 5, 0, 3, 6]]))
    edges = list(zip(
        [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 3, 6, 6, 7, 8, 9, 9, 10, 10, 11, 12, 12, 13, 13, 14, 15, 15,
         16, 16, 17, 18, 18, 19, 19, 20, 21, 22],
        [1, 3, 9, 4, 2, 5, 14, 4, 6, 10, 7, 5, 8, 13, 6, 11, 7, 8, 12, 10, 21, 18, 11, 15, 13, 17, 14, 20, 23, 16, 18,
         17, 19, 20, 21, 19, 20, 22, 23, 22, 23]))
    morris = list(zip(
        [0, 0,  0, 1, 2,  2, 3,  3,  5, 6,  6,  8,  9, 12, 15, 15, 16, 17, 18, 21],
        [1, 3,  9, 4, 5, 14, 4, 10, 13, 7, 11, 12, 10, 13, 16, 18, 19, 20, 19, 22],
        [2, 6, 21, 7, 8, 23, 5, 18, 20, 8, 15, 17, 11, 14, 17, 21, 22, 23, 20, 23]))
    scaling = 100
    translation = 20
    pct_radius = 10
    piece_radius = 20


class GameDisplay:
    piese_diameter = 2 * Graph.piece_radius
    white_piece = pygame.image.load('piesa-alba.png')
    black_piece = pygame.image.load('piesa-neagra.png')
    selected_piece = pygame.image.load('piesa-rosie.png')

    def __init__(self, initialised=False):
        if not initialised:
            pygame.init()
        self.culoareEcran = (255, 255, 255)
        self.culoareLinii = (0, 0, 0)

        self.ecran = pygame.display.set_mode(size=(700, 400))

        self.white_piece = pygame.transform.scale(self.__class__.white_piece,
                                                  (self.__class__.piese_diameter, self.__class__.piese_diameter))
        self.black_piece = pygame.transform.scale(self.__class__.black_piece,
                                                  (self.__class__.piese_diameter, self.__class__.piese_diameter))
        self.selected_piece = pygame.transform.scale(self.__class__.selected_piece,
                                                     (self.__class__.piese_diameter, self.__class__.piese_diameter))
        self.coordonateNoduri = [[Graph.translation + Graph.scaling * x for x in nod] for nod in Graph.nodes]
        self.pieseAlbe = []
        self.nodPiesaSelectata = None
        self.pieseNegre = []

    def deseneazaEcranJoc(self):
        self.ecran.fill(self.culoareEcran)
        for nod in self.coordonateNoduri:
            pygame.draw.circle(surface=self.ecran, color=self.culoareLinii, center=nod, radius=Graph.pct_radius,
                               width=0)  # width=0 face un cerc plin

        for muchie in Graph.edges:
            p0 = self.coordonateNoduri[muchie[0]]
            p1 = self.coordonateNoduri[muchie[1]]
            pygame.draw.line(surface=self.ecran, color=self.culoareLinii, start_pos=p0, end_pos=p1, width=5)
        for nod in self.pieseAlbe:
            self.ecran.blit(self.white_piece, (nod[0] - Graph.piece_radius, nod[1] - Graph.piece_radius))
        for nod in self.pieseNegre:
            self.ecran.blit(self.black_piece, (nod[0] - Graph.piece_radius, nod[1] - Graph.piece_radius))
        if self.nodPiesaSelectata:
            self.ecran.blit(self.selected_piece,
                            (self.nodPiesaSelectata[0] - Graph.piece_radius, self.nodPiesaSelectata[1] - Graph.piece_radius))
        pygame.display.update()

    def activate_display(self):
        self.deseneazaEcranJoc()
        rand = 0

        print("Muta " + ("negru" if rand else "alb"))
        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for nod in self.coordonateNoduri:
                        if HelperClass.euclidian_distance(pos, nod) <= Graph.pct_radius * 2:
                            if rand == 1:
                                pieseCurente = self.pieseNegre
                            else:
                                pieseCurente = self.pieseAlbe

                            if nod not in self.pieseAlbe + self.pieseNegre:
                                if self.nodPiesaSelectata:
                                    n0 = self.coordonateNoduri.index(nod)
                                    n1 = self.coordonateNoduri.index(self.nodPiesaSelectata)
                                    if (n0, n1) in Graph.edges or (n1, n0) in Graph.edges:
                                        pieseCurente.remove(self.nodPiesaSelectata)
                                        pieseCurente.append(nod)
                                        rand = 1 - rand
                                        print("Muta " + ("negru" if rand else "alb"))
                                        self.nodPiesaSelectata = False
                                else:
                                    pieseCurente.append(nod)
                                    rand = 1 - rand
                                    print("Muta " + ("negru" if rand else "alb"))
                            else:
                                if nod in pieseCurente:
                                    if self.nodPiesaSelectata == nod:
                                        self.nodPiesaSelectata = False
                                    else:
                                        self.nodPiesaSelectata = nod

                            self.deseneazaEcranJoc()
                            break
