import time
from not_needed_anymore.Joc import Joc
from not_needed_anymore.Stare import Stare

ADANCIME_MAX = 6

""" Algoritmul MinMax """


def min_max(stare):
    # daca sunt la o frunza in arborele minimax sau la o stare finala
    if stare.depth == 0 or stare.game.final_game():
        stare.estimare = stare.game.estimate_score(stare.depth)
        return stare

    # calculez toate mutarile posibile din starea curenta
    stare.possible_moves = stare.all_possible_moves(,

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutariCuEstimare = [min_max(x) for x in
                        stare.possible_moves]  # expandez(constr subarb) fiecare nod x din mutari posibile

    if stare.active_player == Joc.JMAX:
        # daca jucatorul e MAX_PLAYER aleg starea-fiica cu estimarea maxima
        stare.chosen_state = max(mutariCuEstimare, key=lambda x: x.estimare)  # def f(x): return x.estimare -----> key=f
    else:
        # daca jucatorul e MIN_PLAYER aleg starea-fiica cu estimarea minima
        stare.chosen_state = min(mutariCuEstimare, key=lambda x: x.estimare)

    stare.estimare = stare.chosen_state.estimare
    return stare


def alpha_beta(alpha, beta, stare):
    if stare.depth == 0 or stare.game.final_game():
        stare.estimare = stare.game.estimate_score(stare.depth)
        return stare

    if alpha > beta:
        return stare  # este intr-un interval invalid deci nu o mai procesez

    stare.possible_moves = stare.all_possible_moves(,

    if stare.active_player == Joc.JMAX:
        estimare_curenta = float('-inf')  # in aceasta variabila calculam maximul

        for mutare in stare.possible_moves:
            # calculeaza estimarea pentru starea noua, realizand subarborele
            stare_noua = alpha_beta(alpha, beta, mutare)  # aici construim subarborele pentru stare_noua

            if estimare_curenta < stare_noua.estimare:
                stare.chosen_state = stare_noua
                estimare_curenta = stare_noua.estimare
            if alpha < stare_noua.estimare:
                alpha = stare_noua.estimare
                if alpha >= beta:  # interval invalid
                    break

    elif stare.active_player == Joc.JMIN:
        estimare_curenta = float('inf')
        # completati cu rationament similar pe cazul stare.active_player==Game.MAX_PLAYER
        for mutare in stare.possible_moves:
            # calculeaza estimarea
            stare_noua = alpha_beta(alpha, beta, mutare)  # aici construim subarborele pentru stare_noua

            if estimare_curenta > stare_noua.estimare:
                stare.chosen_state = stare_noua
                estimare_curenta = stare_noua.estimare
            if beta > stare_noua.estimare:
                beta = stare_noua.estimare
                if alpha >= beta:
                    break

    stare.estimare = stare.chosen_state.estimare

    return stare


def afis_daca_final(stare_curenta):
    final = stare_curenta.game.final_game()  # metoda final() returneaza "remiza" sau castigatorul ("x" sau "0") sau
    # False daca nu e stare finala
    if final:
        if final == "remiza":
            print("Remiza!")
        else:
            print("A castigat " + final)

        return True

    return False


def main():
    # initializare algoritm
    raspuns_valid = False

    # TO DO 1
    while not raspuns_valid:
        tip_algoritm = input("Algoritmul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")
    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu x sau cu 0? ").lower()
        if Joc.JMIN in ['x', '0']:
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie x sau 0.")
    Joc.JMAX = '0' if Joc.JMIN == 'x' else 'x'
    # expresie= val_true if conditie else val_false  (conditie? val_true: val_false)

    # initializare tabla
    tabla_curenta = Joc()  # apelam constructorul
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'x', ADANCIME_MAX)

    while True:
        if stare_curenta.j_curent == Joc.JMIN:
            # muta jucatorul utilizator

            # TO DO 4
            print("Acum muta utilizatorul cu simbolul", stare_curenta.j_curent)
            raspuns_valid = False
            while not raspuns_valid:
                try:
                    linie = int(input("linie="))
                    coloana = int(input("coloana="))

                    if linie in range(Joc.NR_COLOANE) and coloana in range(Joc.NR_COLOANE):
                        if stare_curenta.tabla_joc.matr[linie * Joc.NR_COLOANE + coloana] == Joc.GOL:
                            raspuns_valid = True
                        else:
                            print("Exista deja un simbol in pozitia ceruta.")
                    else:
                        print(f"Linie sau coloana invalida (trebuie sa fie unul dintre numerele {','.join([str(elem) for elem in range(Joc.NR_COLOANE)])}).")

                except ValueError:
                    print("Linia si coloana trebuie sa fie numere intregi")

            # dupa iesirea din while sigur am valide atat linia cat si coloana
            # deci pot plasa simbolul pe "tabla de joc"
            stare_curenta.tabla_joc.matr[linie * Joc.NR_COLOANE + coloana] = Joc.JMIN

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))
            # TO DO 8a
            # testez daca jocul a ajuns intr-o stare finala
            # si afisez un mesaj corespunzator in caz ca da
            if afis_daca_final(stare_curenta):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = Joc.jucator_opus(stare_curenta.j_curent)

        # --------------------------------
        else:  # jucatorul e MAX_PLAYER (calculatorul)
            # Mutare calculator

            print("Acum muta calculatorul cu simbolul", stare_curenta.j_curent)
            # preiau timpul in milisecunde de dinainte de mutare
            t_inainte = int(round(time.time() * 1000))

            # stare actualizata e starea mea curenta in care am setat chosen_state (mutarea urmatoare)
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.game  # aici se face de fapt mutarea !!!
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))

            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")
            # TO DO 8b
            if afis_daca_final(stare_curenta):
                break

            # S-a realizat o mutare.  jucatorul cu cel opus
            stare_curenta.j_curent = Joc.jucator_opus(stare_curenta.j_curent)


if __name__ == "__main__":
    main()
# TO DO 9
