import pygame
import sys
import math


def distEuclid(p0, p1):
    (x0, y0) = p0
    (x1, y1) = p1
    return math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)


class Graph:
    # coordonatele nodurilor ()
    noduri = list(zip(
        [float(elem / 2) for elem in [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]],
        [float(elem / 2) for elem in [0, 3, 6, 1, 3, 5, 2, 3, 4, 0, 1, 2, 4, 5, 6, 2, 3, 4, 1, 3, 5, 0, 3, 6]]))
    muchii = list(zip(
        [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 3, 6, 6, 7, 8, 9, 9, 10, 10, 11, 12, 12, 13, 13, 14, 15, 15,
         16, 16, 17, 18, 18, 19, 19, 20, 21, 22],
        [1, 3, 9, 4, 2, 5, 14, 4, 6, 10, 7, 5, 8, 13, 6, 11, 7, 8, 12, 10, 21, 18, 11, 15, 13, 17, 14, 20, 23, 16, 18,
         17, 19, 20, 21, 19, 20, 22, 23, 22, 23]))
    scalare = 100
    translatie = 20
    razaPct = 10
    razaPiesa = 20


class EcranJoc:
    def __init__(self, graph: Graph, initialised=False):
        if not initialised:
            pygame.init()
        self.culoareEcran = (255, 255, 255)
        self.culoareLinii = (0, 0, 0)

        self.ecran = pygame.display.set_mode(size=(700, 400))

        self.piesaAlba = pygame.image.load('../../my_implementation/piesa-alba.png')
        self.diametruPiesa = 2 * Graph.razaPiesa
        self.piesaAlba = pygame.transform.scale(self.piesaAlba, (self.diametruPiesa, self.diametruPiesa))
        self.piesaNeagra = pygame.image.load('../../my_implementation/piesa-neagra.png')
        self.piesaNeagra = pygame.transform.scale(self.piesaNeagra, (self.diametruPiesa, self.diametruPiesa))
        self.piesaSelectata = pygame.image.load('../../my_implementation/piesa-rosie.png')
        self.piesaSelectata = pygame.transform.scale(self.piesaSelectata, (self.diametruPiesa, self.diametruPiesa))
        self.coordonateNoduri = [[Graph.translatie + Graph.scalare * x for x in nod] for nod in Graph.noduri]
        self.pieseAlbe = []
        self.nodPiesaSelectata = None
        self.pieseNegre = []

    def deseneazaEcranJoc(self):
        self.ecran.fill(self.culoareEcran)
        for nod in self.coordonateNoduri:
            pygame.draw.circle(surface=self.ecran, color=self.culoareLinii, center=nod, radius=Graph.razaPct,
                               width=0)  # width=0 face un cerc plin

        for muchie in Graph.muchii:
            p0 = self.coordonateNoduri[muchie[0]]
            p1 = self.coordonateNoduri[muchie[1]]
            pygame.draw.line(surface=self.ecran, color=self.culoareLinii, start_pos=p0, end_pos=p1, width=5)
        for nod in self.pieseAlbe:
            self.ecran.blit(self.piesaAlba, (nod[0] - Graph.razaPiesa, nod[1] - Graph.razaPiesa))
        for nod in self.pieseNegre:
            self.ecran.blit(self.piesaNeagra, (nod[0] - Graph.razaPiesa, nod[1] - Graph.razaPiesa))
        if self.nodPiesaSelectata:
            self.ecran.blit(self.piesaSelectata,
                            (self.nodPiesaSelectata[0] - Graph.razaPiesa, self.nodPiesaSelectata[1] - Graph.razaPiesa))
        pygame.display.update()


def activate_display():
    display = EcranJoc(Graph())

    display.deseneazaEcranJoc()
    rand = 0

    print("Muta " + ("negru" if rand else "alb"))
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for nod in display.coordonateNoduri:
                    if distEuclid(pos, nod) <= Graph.razaPct * 2:
                        if rand == 1:
                            piesa = display.piesaNeagra
                            pieseCurente = display.pieseNegre
                        else:
                            piesa = display.piesaAlba
                            pieseCurente = display.pieseAlbe

                        if nod not in display.pieseAlbe + display.pieseNegre:
                            if display.nodPiesaSelectata:
                                n0 = display.coordonateNoduri.index(nod)
                                n1 = display.coordonateNoduri.index(display.nodPiesaSelectata)
                                if (n0, n1) in Graph.muchii or (n1, n0) in Graph.muchii:
                                    pieseCurente.remove(display.nodPiesaSelectata)
                                    pieseCurente.append(nod)
                                    rand = 1 - rand
                                    print("Muta " + ("negru" if rand else "alb"))
                                    display.nodPiesaSelectata = False
                            else:
                                pieseCurente.append(nod)
                                rand = 1 - rand
                                print("Muta " + ("negru" if rand else "alb"))
                        else:
                            if nod in pieseCurente:
                                if display.nodPiesaSelectata == nod:
                                    display.nodPiesaSelectata = False
                                else:
                                    display.nodPiesaSelectata = nod

                        display.deseneazaEcranJoc()
                        break


activate_display()
