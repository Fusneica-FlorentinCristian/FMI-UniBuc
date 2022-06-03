import itertools
import math
import sys

import pygame


class HelperClass:
    @staticmethod
    def euclidian_distance(p0, p1):
        (x0, y0) = p0
        (x1, y1) = p1
        return math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)

    @staticmethod
    def check_final(current_state):
        final = current_state.game.final_game(current_state)
        if final:
            if final == "remiza":
                print("Remiza!")
            else:
                print(f"{final} wins!")
            return True
        return False

    @staticmethod
    def check_exit(ev):
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    @staticmethod
    def same_elements(your_list):
        if len(set(your_list)) == 1:
            return your_list[0] if your_list[0] is not None or your_list[0] != "#" else False
        return False

    @staticmethod
    def print_current_player(active_player, debug=True):
        if debug:
            print("Muta " + ("negru" if active_player == "black" else "alb"))

    @staticmethod
    def build_all_new_morrises(all_morrisses, nodes):
        new_morrises = []
        combinations_of_3 = list(itertools.combinations(nodes, 3))
        combinations_of_3 = [tuple(sorted(list(elem))) for elem in combinations_of_3]
        # print(combinations_of_3)
        for combination in combinations_of_3:
            if combination in all_morrisses:
                new_morrises.append(combination)
        return new_morrises


