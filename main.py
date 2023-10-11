# main class for starting the game
from time import sleep

import config
from board import Board
from controller import GameController
from lighthouse_connector import LighthouseConnector
from player import Player


# prints board to console
def print_board(board: Board):
    temp_str = ""
    for i in range(1, board.get_length()):
        temp_str += f" {i},"
    last_i = 0
    for i in range(board.get_length(), board.get_height() * board.get_length() + 1, board.get_length()):
        print(str(board.get_board()[last_i:i]).replace("None", " ").replace("'",""))
        last_i = i
    print("\n")


# draws board on lighthouse
def draw_board(board: Board):
    img: list = lh.get_empty_image()
    colors: dict = {
        player1.get_identifier(): player1.get_color(),
        player2.get_identifier(): player2.get_color(),
        None: [42, 42, 42],
        "border": [0, 0, 0]
    }

    for y in range(board.get_height()):
        for x in range(board.get_length()):
            if x == 0:
                img[y * 2][x] = colors["border"]
                img[y * 2 + 1][x] = colors["border"]
            for i in range(1, 3):
                img[y * 2][x * 2 + i] = colors[board.get_board()[(y * board.get_length()) + x]]
                img[y * 2 + 1][x * 2 + i] = colors[board.get_board()[(y * board.get_length()) + x]]
            if x == board.get_length() - 1:
                img[y * 2][x * 2 + 3] = colors["border"]
                img[y * 2 + 1][x * 2 + 3] = colors["border"]
    lh.draw(img)
    sleep(0.1)


# prints board to console and draws on lighthouse
def draw_both(board: Board):
    print_board(board)
    draw_board(board)


# does as the name said, but returns empty function if name not found
def parse_draw_method_from_config(method_string):
    method_dict = {'console': print_board,
                   'lighthouse': draw_board,
                   'both': draw_both
                   }
    if method_string not in method_dict:
        return lambda x: None
    else:
        return method_dict[method_string]


# entry point of program
if __name__ == "__main__":
    lh = LighthouseConnector()
    player1 = Player("Player1", config.p1_color, "X", human=config.player1_human)
    player2 = Player("Player2", config.p2_color, "o", human=config.player2_human)
    enable_animations = config.animations and config.draw_method.lower() == 'lighthouse'
    if config.animations and not config.draw_method.lower() == 'lighthouse':
        print("Auto disable animations due to console output.")
    game = GameController(player1, player2, animations=enable_animations, loop=config.loop,
                          print_board_callback=parse_draw_method_from_config(config.draw_method.lower()))
    game.start()
    lh.stop()

""" code for multithreading which will most likely never be implemented
while True:
    if game.get_game_state() is GameState.RUN:
        print_board(game.get_board())
    if game.get_game_state() is GameState.RUN_AWAIT_INPUT:
        print(">> awaiting input")
    if game.get_game_state() is GameState.END_DRAW:
        print_board(game.get_board())
        print("No one won.")
    if game.get_game_state() is GameState.END_WIN:
        print("Player '%s' won!" % (game.get_active_player().get_name()))
    sleep(2)
"""
