import copy

from my_implementation.main import Game

game1 = Game()
game2 = Game()

# game1.white_pieces.append(1)

game2.white_morrises = copy.deepcopy(game1.white_morrises)
game1.white_morrises.append(1)

print(game2.white_morrises, game1.white_morrises)