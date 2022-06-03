import copy
import itertools
import math
from time import time

import pygame
import sys


class Graph:
    # changed
    # coordonatele nodurilor ()
    nodes = list(zip(
        [float(elem / 2) for elem in [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]],
        [float(elem / 2) for elem in [0, 3, 6, 1, 3, 5, 2, 3, 4, 0, 1, 2, 4, 5, 6, 2, 3, 4, 1, 3, 5, 0, 3, 6]]))
    edges = list(zip(
        [0, 0, 0, 1, 1, 2,  2, 3, 3,  3, 4, 4, 5,  5, 3,  6, 6, 7,  8,  9,  9, 10, 10, 11, 12, 12, 13, 13, 14, 15, 15, 16, 16, 17, 18, 18, 19, 19, 20, 21, 22],
        [1, 3, 9, 4, 2, 5, 14, 4, 6, 10, 7, 5, 8, 13, 6, 11, 7, 8, 12, 10, 21, 18, 11, 15, 13, 17, 14, 20, 23, 16, 18, 17, 19, 20, 21, 19, 20, 22, 23, 22, 23]))
    morris = list(zip(
        [0, 0,  0, 1, 2,  2, 3,  3,  5, 6,  6,  8,  9, 12, 15, 15, 16, 17, 18, 21],
        [1, 3,  9, 4, 5, 14, 4, 10, 13, 7, 11, 12, 10, 13, 16, 18, 19, 20, 19, 22],
        [2, 6, 21, 7, 8, 23, 5, 18, 20, 8, 15, 17, 11, 14, 17, 21, 22, 23, 20, 23]))
    scaling = 100
    translation = 20
    pct_radius = 10
    piece_radius = 20


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
    def check_exit(event):
        if event.type == pygame.QUIT:
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


class Button:
    def __init__(self, display=None, left=0, top=0, w=0, h=0, background_color=(53, 80, 115),
                 selected_background_color=(89, 134, 194), text="", font="arial", font_size=16,
                 text_color=(255, 255, 255),
                 value=""):
        self.display = display
        self.background_color = background_color
        self.selected_background_color = selected_background_color
        self.text = text
        self.font = font
        self.w = w
        self.h = h
        self.is_selected = False
        self.font_size = font_size
        self.text_color = text_color
        # creez obiectul font
        font_obj = pygame.font.SysFont(self.font, self.font_size)
        self.rendered_text = font_obj.render(self.text, True, self.text_color)
        self.rectangle = pygame.Rect(left, top, w, h)
        # aici centram textul
        self.rectangle_text = self.rendered_text.get_rect(center=self.rectangle.center)
        self.value = value

    def selected(self, sel):
        self.is_selected = sel
        self.display_button()

    def select_with_coords(self, coord):
        if self.rectangle.collidepoint(coord):
            self.selected(True)
            return True
        return False

    def rect_update(self, top, left):
        self.rectangle.top = top
        self.rectangle.left = left
        self.rectangle_text = self.rendered_text.get_rect(center=self.rectangle.center)

    def display_button(self):
        background_color = self.selected_background_color if self.is_selected else self.background_color
        pygame.draw.rect(self.display, background_color, self.rectangle)
        self.display.blit(self.rendered_text, self.rectangle_text)


class ButtonsGroup:
    def __init__(self, buttons_list=None, selected_index=0, button_spacing=10, left=0, top=0):
        self.buttons_list = [] if not buttons_list else buttons_list
        self.selected_index = selected_index
        self.buttons_list[self.selected_index].is_selected = True
        self.top = top
        self.left = left
        current_left = self.left
        for b in self.buttons_list:
            b.rect_update(self.top, current_left)
            current_left += (button_spacing + b.w)

    def select_with_coords(self, coord):
        for ib, b in enumerate(self.buttons_list):
            if b.select_with_coords(coord):
                self.buttons_list[self.selected_index].selected(False)
                self.selected_index = ib
                return True
        return False

    def display_buttons(self):
        # atentie, nu face wrap
        for b in self.buttons_list:
            b.display_button()

    def get_value(self):
        return self.buttons_list[self.selected_index].value


# ----------------- game_display initial ---------------
def display_menu(display):
    btn_player = ButtonsGroup(buttons_list=[
        Button(display=display, w=120, h=30, text="Alb - primul", value="white"),
        Button(display=display, w=120, h=30, text="Negru - al doilea", value="black")
    ], selected_index=0, left=30, top=30)
    btn_algorithm = ButtonsGroup(buttons_list=[
        Button(display=display, w=80, h=30, text="min-max", value="minmax"),
        Button(display=display, w=80, h=30, text="alphabeta", value="alphabeta")
    ], selected_index=0, left=30, top=70)
    btn_difficulty = ButtonsGroup(buttons_list=[
        Button(display=display, w=60, h=30, text="Usor", value="2"),
        Button(display=display, w=60, h=30, text="Mediu", value="3"),
        Button(display=display, w=60, h=30, text="Greu", value="4")
    ], selected_index=1, left=30, top=110)
    btn_game_type = ButtonsGroup(buttons_list=[
        Button(display=display, w=70, h=30, text="PvP", value="pvp"),  # player vs player
        Button(display=display, w=70, h=30, text="PvsBot", value="pvb"),  # player vs bot
        Button(display=display, w=70, h=30, text="BotVsBot", value="bvb")  # bot vs bot
    ], selected_index=1, left=30, top=170)
    ok = Button(display=display, left=30, top=250, w=40, h=30, background_color=(155, 0, 55), text="ok")
    btn_game_type.display_buttons()
    btn_algorithm.display_buttons()
    btn_player.display_buttons()
    btn_difficulty.display_buttons()
    ok.display_button()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not btn_algorithm.select_with_coords(pos):
                    if not btn_player.select_with_coords(pos):
                        if not btn_game_type.select_with_coords(pos):
                            if not btn_difficulty.select_with_coords(pos):
                                if ok.select_with_coords(pos):
                                    display.fill((0, 0, 0))  # stergere game_display
                                    return btn_player.get_value(), btn_algorithm.get_value(), \
                                           btn_difficulty.get_value(), btn_game_type.get_value()
        pygame.display.update()


class State:
    def __init__(self, game, active_player, depth: int, score=None):
        self.game = game
        self.active_player = active_player
        # adancimea in arborele de stari
        self.depth = depth

        # scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.score = score

        # lista de mutari posibile din starea curenta
        self.possible_moves = []

        # cea mai bunÄ mutare din lista de mutari posibile pentru jucatorul curent
        self.chosen_state = None

    def moves(self):
        opposite_player = Game.opposite_player(self.active_player)
        game_moves_list = self.game.moves(self.active_player, self)
        games = [game for game in [self.game.copy_game(move, self.active_player) for move in game_moves_list]]
        # print("games in State.moves()")
        for game in games:
            if self.active_player == "white":
                if game.last_move[0] is not None:
                    game.white_pieces.remove(game.nodes_coords[game.last_move[0]])
                if game.last_move[1] is not None:
                    game.white_pieces.append(game.nodes_coords[game.last_move[1]])
                if game.last_move[2] is not None:
                    game.black_pieces.remove(game.nodes_coords[game.last_move[2]])
            if self.active_player == "black":
                if game.last_move[0] is not None:
                    game.black_pieces.remove(game.nodes_coords[game.last_move[0]])
                if game.last_move[1] is not None:
                    game.black_pieces.append(game.nodes_coords[game.last_move[1]])
                if game.last_move[2] is not None:
                    if self.depth == 3:
                        print("in State.moves() there is a deletable node")
                    game.white_pieces.remove(game.nodes_coords[game.last_move[2]])

            self.game.check_new_morris(self.active_player)
            self.game.check_new_morris(self.active_player, opposite=True)

        states_list = [State(game, opposite_player, self.depth - 1) for game in games]

        return states_list

    def __str__(self):
        sir = str(self.game) + "(Juc curent:" + self.active_player + ")\n"
        return sir

    def __repr__(self):
        sir = str(self.game) + "(Juc curent:" + self.active_player + ")\n"
        return sir


class Game:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    MIN_PLAYER = None
    MAX_PLAYER = None
    NO_PIECES = 12
    max_score = 0
    piece_diameter = 2 * Graph.piece_radius
    white_piece = pygame.image.load('piesa-alba.png')
    black_piece = pygame.image.load('piesa-neagra.png')
    selected_piece = pygame.image.load('piesa-rosie.png')
    debug = False

    def __init__(self, debug=False, initialised=False):
        # creez proprietatea last_move = (last_node, new_node, deleted_node)
        self.last_white_move = (None, None, None)
        self.last_black_move = (None, None, None)
        self.last_move = (None, None, None)
        if not initialised:
            self.__class__.debug = debug
            self.__class__.initialise()
        self.selected_piece_node = None
        self.white_pieces = []
        self.black_pieces = []
        self.unused_white_pieces = self.__class__.NO_PIECES
        self.unused_black_pieces = self.__class__.NO_PIECES
        self.white_morrises = []
        self.black_morrises = []

    @classmethod
    def initialise(cls):
        cls.background_color = (255, 255, 255)
        cls.edges_color = (0, 0, 0)

        cls.game_display = pygame.display.set_mode(size=(700, 400))

        cls.white_piece = pygame.transform.scale(cls.white_piece,
                                                 (cls.piece_diameter, cls.piece_diameter))
        cls.black_piece = pygame.transform.scale(cls.black_piece,
                                                 (cls.piece_diameter, cls.piece_diameter))
        cls.selected_piece = pygame.transform.scale(cls.selected_piece,
                                                    (cls.piece_diameter, cls.piece_diameter))
        cls.nodes_coords = [[Graph.translation + Graph.scaling * x for x in nod] for nod in Graph.nodes]

    def copy_game(self, changes, active_player):
        game = Game(initialised=True)
        game.last_white_move = copy.copy(self.last_white_move) if active_player == "black" else changes
        game.last_black_move = copy.copy(self.last_black_move) if active_player == "white" else changes
        game.last_move = changes
        game.selected_piece_node = None
        unused_whites = copy.copy(self.unused_white_pieces) - 1 if active_player == "white" \
            else copy.copy(self.unused_white_pieces)
        unused_blacks = copy.copy(self.unused_black_pieces) - 1 if active_player == "black" \
            else copy.copy(self.unused_black_pieces)
        game.unused_white_pieces = unused_whites
        game.unused_black_pieces = unused_blacks
        game.white_morrises = copy.copy(self.white_morrises)
        game.black_morrises = copy.copy(self.black_morrises)
        game.white_pieces = copy.copy(self.white_pieces)
        game.black_pieces = copy.copy(self.black_pieces)
        return game

    def moves(self, active_player, current_state):
        white_nodes = [self.nodes_coords.index(piece) for piece in self.white_pieces]
        black_nodes = [self.nodes_coords.index(piece) for piece in self.black_pieces]
        current_nodes = white_nodes if active_player == "white" else black_nodes
        moves = []
        for node in current_nodes:
            variants = self.variants_node(node, current_state=current_state, white_pieces=white_nodes,
                                          black_pieces=black_nodes)
            for variant in variants:
                moves.append((node, variant[0], variant[1]))
        for elem in range(24):  # all nodes' indexes
            if elem not in white_nodes + black_nodes:
                if self.check_new_morris(active_player, new_piece=elem, set_new_morrises=False):
                    deletable = self.get_removable_piece(current_state, is_player=False)
                    if len(deletable) > 0:
                        moves.extend([(None, elem, deleted_node) for deleted_node in deletable])
                    else:
                        moves.append((None, elem, None))
                else:
                    moves.append((None, elem, None))

        # print("Game.moves(): " + str(moves))
        return moves

    def display_game(self):
        self.game_display.fill(self.background_color)
        for nod in self.nodes_coords:
            pygame.draw.circle(surface=self.game_display, color=self.edges_color, center=nod, radius=Graph.pct_radius,
                               width=0)  # width=0 face un cerc plin

        for muchie in Graph.edges:
            p0 = self.nodes_coords[muchie[0]]
            p1 = self.nodes_coords[muchie[1]]
            pygame.draw.line(surface=self.game_display, color=self.edges_color, start_pos=p0, end_pos=p1, width=5)
        for nod in self.white_pieces:
            self.game_display.blit(self.white_piece, (nod[0] - Graph.piece_radius, nod[1] - Graph.piece_radius))
        for nod in self.black_pieces:
            self.game_display.blit(self.black_piece, (nod[0] - Graph.piece_radius, nod[1] - Graph.piece_radius))
        if self.selected_piece_node:
            self.game_display.blit(self.selected_piece,
                                   (self.selected_piece_node[0] - Graph.piece_radius,
                                    self.selected_piece_node[1] - Graph.piece_radius))
        pygame.display.update()

    def initialise_game(self):
        pygame.init()
        pygame.display.set_caption("Fusneica Florentin-Cristian - Twelve men's morris")
        Game.MIN_PLAYER, algorithm_type, difficulty, play_type = display_menu(self.game_display)
        self.display_game()

        # if Game.debug:
        #     print(Game.MIN_PLAYER, algorithm_type, difficulty, play_type)

        Game.MAX_PLAYER = 'white' if Game.MIN_PLAYER == 'black' else 'black'

        # print("Tabla initiala")
        # print(str(tabla_curenta))
        #
        # # creare stare initiala
        current_state = State(self, 'white', depth=int(difficulty))
        if not Game.debug:
            print("Muta " + ("negru" if current_state.active_player == "black" else "alb"))
        return algorithm_type, play_type, current_state

    def check_new_morris(self, active_player, new_piece=None, set_new_morrises=True, opposite=False):
        active_player = self.opposite_player(active_player) if opposite else active_player
        is_new_morris = False
        if active_player == "white":
            current_nodes = [self.nodes_coords.index(piece) for piece in self.white_pieces]
        else:
            current_nodes = [self.nodes_coords.index(piece) for piece in self.black_pieces]

        if new_piece is not None:
            current_nodes.append(new_piece)
        new_morrises = HelperClass.build_all_new_morrises(Graph.morris, current_nodes)
        # print("new_morrises=", new_morrises)
        for new_morris in new_morrises:
            if (new_morris not in self.white_morrises and active_player == "white") or (
                    new_morris not in self.black_morrises and active_player == "black"):  # changed

                is_new_morris = True
                break
        if active_player == "white" and set_new_morrises:
            self.white_morrises = new_morrises
        elif set_new_morrises:
            self.black_morrises = new_morrises
        return is_new_morris

    def set_last_move(self, last_node, current_state, node):
        is_new_morris = self.check_new_morris(current_state.active_player)
        deleted_node = self.get_removable_piece(current_state) if is_new_morris else None
        # print(deleted_node)
        if current_state.active_player == "white":
            current_state.game.last_white_move = (last_node, node, deleted_node)
        else:
            current_state.game.last_black_move = (last_node, node, deleted_node)
        current_state.game.last_move = (last_node, node, deleted_node)

    def player_move(self, current_state):
        for event in pygame.event.get():
            HelperClass.check_exit(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.display_game()
                for node in self.nodes_coords:
                    if HelperClass.euclidian_distance(pos, node) <= Graph.pct_radius * 2:
                        current_pieces = self.black_pieces if current_state.active_player == "black" \
                            else self.white_pieces
                        # print(current_state.game.unused_white_pieces, current_state.game.unused_black_pieces)
                        opposite_pieces = self.black_pieces if current_state.active_player == "white" \
                            else self.white_pieces

                        if node not in self.white_pieces + self.black_pieces:
                            if self.selected_piece_node:
                                n0 = self.nodes_coords.index(node)
                                n1 = self.nodes_coords.index(self.selected_piece_node)
                                if (n0, n1) in Graph.edges or (n1, n0) in Graph.edges:
                                    last_moved_node = current_state.game.last_black_move[1] \
                                        if current_state.active_player == "black" \
                                        else current_state.game.last_white_move[1]
                                    before_last_moved_node = current_state.game.last_black_move[0] \
                                        if current_state.active_player == "black" \
                                        else current_state.game.last_white_move[0]

                                    if node != before_last_moved_node or self.selected_piece_node != last_moved_node:
                                        current_pieces.append(node)
                                        current_pieces.remove(self.selected_piece_node)
                                        old_node_place = self.selected_piece_node
                                        self.selected_piece_node = False
                                        current_state.game.display_game()
                                        self.set_last_move(old_node_place, current_state, node)
                                        if current_state.game.last_move[2]:  # if a node was selected to be deleted
                                            opposite_pieces.remove(current_state.game.last_move[2])

                                        current_state.game.display_game()
                                        if HelperClass.check_final(current_state):
                                            return "final"
                                        current_state.active_player = self.opposite_player(current_state.active_player)
                                        HelperClass.print_current_player(current_state.active_player)
                                        self.selected_piece_node = False
                                        return False
                            elif current_state.active_player == "white" and current_state.game.unused_white_pieces > 0:
                                current_pieces.append(node)
                                current_state.game.display_game()
                                current_state.game.unused_white_pieces -= 1
                                self.set_last_move(self.selected_piece_node, current_state, node)
                                if current_state.game.last_move[2]:  # if a node was selected to be deleted
                                    opposite_pieces.remove(current_state.game.last_move[2])

                                current_state.game.display_game()
                                if HelperClass.check_final(current_state):
                                    return "final"
                                current_state.active_player = self.opposite_player(current_state.active_player)
                                HelperClass.print_current_player(current_state.active_player)
                                return False
                            elif current_state.active_player == "black" and current_state.game.unused_black_pieces > 0:
                                current_pieces.append(node)
                                current_state.game.display_game()
                                current_state.game.unused_black_pieces -= 1
                                self.set_last_move(self.selected_piece_node, current_state, node)
                                if current_state.game.last_move[2]:  # if a node was selected to be deleted
                                    opposite_pieces.remove(current_state.game.last_move[2])

                                current_state.game.display_game()
                                if HelperClass.check_final(current_state):
                                    return "final"
                                current_state.active_player = self.opposite_player(current_state.active_player)
                                HelperClass.print_current_player(current_state.active_player)
                                return False
                        elif node in current_pieces:
                            self.selected_piece_node = False if self.selected_piece_node == node else node

                        current_state.game.display_game()
                        # break

    def bot_move(self, current_state: State, algorithm_type="minmax"):
        print("Bot started thinking")
        start_time = time()
        if algorithm_type == "minmax":
            new_state = min_max(current_state)
        else:  # tip_algoritm=="alphabeta"
            new_state = alpha_beta(-500, 500, current_state)
        # print(f"player after minmax in bot_move: {current_state.active_player}")
        end_time = time()
        print("Calculatorul a \"gandit\" " + str(end_time - start_time) + " milisecunde.")

        current_state.game = new_state.chosen_state.game
        current_state.game.display_game()

        if HelperClass.check_final(current_state):
            return "final"

        current_state.active_player = self.opposite_player(current_state.active_player)
        HelperClass.print_current_player(current_state.active_player)
        # print("end of bot_move")
        return None

    def get_removable_piece(self, current_state, is_player=True):
        # print("NEW MORRIS")
        opposite_pieces = [self.nodes_coords.index(piece) for piece in self.black_pieces] \
            if current_state.active_player == "white" else \
            [self.nodes_coords.index(piece) for piece in self.white_pieces]
        opposite_morrisses = self.black_morrises if current_state.active_player == "white" else self.white_morrises
        opposite_nodes_in_morris = list(set([element for morris in opposite_morrisses for element in morris]))
        if sorted(opposite_nodes_in_morris) == sorted(opposite_pieces):
            return None

        if is_player:
            while True:
                for event in pygame.event.get():
                    HelperClass.check_exit(event)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        for node in self.nodes_coords:
                            if HelperClass.euclidian_distance(pos, node) <= Graph.pct_radius * 2:
                                node = current_state.game.nodes_coords.index(node)
                                if node not in opposite_nodes_in_morris and node in opposite_pieces:
                                    return current_state.game.nodes_coords[node]
        else:
            removable_pieces = []
            for node in opposite_pieces:
                if node not in opposite_nodes_in_morris:
                    removable_pieces.append(node)
            return removable_pieces

    def player_vs_player(self, current_state):
        while True:
            if self.player_move(current_state):
                break

    def player_vs_bot(self, algorithm_type, current_state):
        while True:
            if current_state.active_player == Game.MIN_PLAYER:
                if self.player_move(current_state):
                    break
            elif self.bot_move(current_state, algorithm_type):
                break

    def activate_display(self):
        algorithm_type, play_type, current_state = self.initialise_game()
        if play_type == "pvp":
            self.player_vs_player(current_state)
        elif play_type == "pvb":
            self.player_vs_bot(algorithm_type, current_state)
        else:
            self.player_vs_player(current_state)

    @classmethod
    def opposite_player(cls, player):
        return cls.MAX_PLAYER if player == cls.MIN_PLAYER else cls.MIN_PLAYER

    def final(self, current_state):
        if not current_state.game.last_move[1]:  # daca e inainte de prima mutare
            # print("not current_status.game.last_move[1]")
            return False
        if current_state.game.unused_white_pieces > 0 or current_state.game.unused_black_pieces > 0:
            # print(current_state.game.unused_white_pieces, current_state.game.unused_black_pieces)
            return False
        remaining_white_pieces = current_state.game.unused_white_pieces + len(current_state.game.white_pieces)
        remaining_black_pieces = current_state.game.unused_black_pieces + len(current_state.game.black_pieces)
        if remaining_white_pieces <= 2 and remaining_black_pieces <= 2:
            print("remiza")
            return "remiza"
        # print("before opposite_player_can_move")
        opposite_can_move = self.opposite_player_can_move(current_state)

        if current_state.active_player == "black" and (remaining_white_pieces <= 2 or not opposite_can_move):
            return "Black"
        elif current_state.active_player == "white" and (remaining_black_pieces <= 2 or not opposite_can_move):
            return "White"
        else:
            return False

    # linie deschisa inseamna linie pe care jucatorul mai poate forma o configuratie castigatoare
    # practic e o linie fara simboluri ale jucatorului opus
    def open_morris(self, morrises_list, player):
        jo = self.opposite_player(player)
        # verific daca pe linia data nu am simbolul jucatorului opus
        if jo not in morrises_list:
            # return 1
            return morrises_list.count(player)
        return 0

    def open_morrises(self, player):
        return None

    def estimate_score(self, state):
        return 0

    def console_output(self):
        return ""

    def __str__(self):
        return self.console_output()

    def __repr__(self):
        return self.console_output()

    def variants_node(self, node, current_state, white_pieces, black_pieces, opposite=False, with_deleted=False):
        variants_list = []
        last_move = None
        if opposite:
            opposite_player = self.opposite_player(current_state.active_player)
            last_move = current_state.game.last_black_move[0] if opposite_player == "black" else \
                current_state.game.last_white_move[0]
        if not opposite:
            last_move = current_state.game.last_black_move[0] if current_state.active_player == "black" else \
                current_state.game.last_white_move[0]
        # print(node)
        for edge in Graph.edges:
            other_node = None
            if node in edge:
                for variant in edge:
                    other_node = variant if variant != node else other_node
            if other_node not in white_pieces + black_pieces + [last_move] and other_node is not None:
                deletable = self.get_removable_piece(current_state, is_player=False) if with_deleted else [None]
                variants_list.extend([(other_node, delete) for delete in deletable])
        # if Game.debug:
        #     print(variants_list)
        return variants_list

    def opposite_player_can_move(self, current_state):
        if Game.debug:
            print("opposite_player_can_move")
        opposite_player = self.opposite_player(current_state.active_player)
        if (opposite_player == "white" and current_state.game.unused_white_pieces > 0) \
                or (opposite_player == "black" and current_state.game.unused_black_pieces > 0):
            return True

        white_pieces = [self.nodes_coords.index(piece) for piece in current_state.game.white_pieces]
        black_pieces = [self.nodes_coords.index(piece) for piece in current_state.game.black_pieces]

        for node in (white_pieces if opposite_player == "white" else black_pieces):
            if len(self.variants_node(node, current_state, white_pieces, black_pieces, True)) > 0:
                return True
        return False


def min_max(state: State):
    if state.depth == 0 or state.game.final_game(current_state=state):
        state.score = state.game.estimate_score(state)
        return state

    # calculez toate mutarile posibile din starea curenta
    state.possible_moves = state.moves()
    scored_moves = [min_max(move) for move in state.possible_moves]
    # print(state.active_player, Game.MAX_PLAYER, Game.MIN_PLAYER)
    if state.active_player == Game.MAX_PLAYER:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        state.chosen_state = max(scored_moves, key=lambda x: x.score)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        state.chosen_state = min(scored_moves, key=lambda x: x.score)
    # print("went through minmax")
    state.score = state.chosen_state.score
    # print("finished min-max, current player (computer):", state.active_player)
    return state


def alpha_beta(alpha, beta, state: State):
    if state.depth == 0 or state.game.final_game():
        state.score = state.game.estimate_score(state.depth)
        return state

    if alpha > beta:
        return state  # este intr-un interval invalid deci nu o mai procesez

    state.possible_moves = state.moves()

    if state.active_player == Game.MAX_PLAYER:
        scor_curent = float('-inf')

        for mutare in state.possible_moves:
            # calculeaza scorul
            stare_noua = alpha_beta(alpha, beta, mutare)

            if scor_curent < stare_noua.score:
                state.chosen_state = stare_noua
                scor_curent = stare_noua.score
            if alpha < stare_noua.score:
                alpha = stare_noua.score
                if alpha >= beta:
                    break

    elif state.active_player == Game.MIN_PLAYER:
        scor_curent = float('inf')

        for mutare in state.possible_moves:

            stare_noua = alpha_beta(alpha, beta, mutare)

            if scor_curent > stare_noua.score:
                state.chosen_state = stare_noua
                scor_curent = stare_noua.score

            if beta > stare_noua.score:
                beta = stare_noua.score
                if alpha >= beta:
                    break
    state.score = state.chosen_state.score


if __name__ == "__main__":
    Game(debug=False).activate_display()

    while True:
        for ev in pygame.event.get():
            HelperClass.check_exit(ev)