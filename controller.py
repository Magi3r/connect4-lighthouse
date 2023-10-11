from time import sleep
from board import Board
from gamestates import GameState
from player import Player
from pregenmessages import PregenMessages


# GameController class for core gameplay
class GameController:
    def __init__(self, player1: Player, player2: Player, print_board_callback=lambda board: None, loop: bool = False,
                 animations: bool = False):
        self.__game_state: GameState = GameState.INIT
        self.__board: Board = Board()
        self.__active_player: Player = player1
        self.__inactive_player: Player = player2
        self.__print_board_callback = print_board_callback
        self.__loop: bool = loop
        self.__animations = animations

        print(">> Game initialized.")

    # starts the game by setting its game state
    def start(self):
        self.__game_state = GameState.RUN
        print(">> Game started.")
        self.run()

    # main loop through the game
    def run(self):
        self.__print_board_callback(self.__board)
        while self.__game_state is GameState.RUN:
            self.place_marker(self.__active_player)
            self.__print_board_callback(self.__board)
            if self.__board.check_win(self.__active_player):
                self.__game_state = GameState.END_WIN
            elif self.__board.check_draw():
                self.__game_state = GameState.END_DRAW
            else:
                self.__active_player, self.__inactive_player = self.__inactive_player, self.__active_player

        self.end()

    def get_game_state(self) -> GameState:
        return self.__game_state

    def get_board(self) -> Board:
        return self.__board

    def get_active_player(self) -> Player:
        return self.__active_player

    def get_inactive_player(self) -> Player:
        return self.__inactive_player

    # awaits user input and places the marker
    def place_marker(self, player: Player):
        self.__game_state = GameState.RUN_AWAIT_INPUT
        while self.__game_state is GameState.RUN_AWAIT_INPUT:
            # print(self.__board.get_board())
            player.msg_pg(PregenMessages.AWAIT_USER_INPUT)
            player_input: str = player.get_input()
            if player_input.isdecimal():
                player_input_int: int = int(player_input)
                if player_input_int not in range(1, self.__board.get_length() + 1):
                    player.msg_pg(PregenMessages.INPUT_ERR_OUT_OF_RANGE)
                elif self.__board.get_board()[player_input_int - 1] is not None:
                    player.msg_pg(PregenMessages.INPUT_ERR_COLUMN_FULL)
                else:
                    self.__board.set_marker(player_input_int - 1, self.__active_player, self.__inactive_player,
                                            self.__animations, animation_callback=self.__print_board_callback)
                    self.__game_state = GameState.RUN
            else:
                player.msg_pg(PregenMessages.INPUT_ERR_NAN)

    # handles what happens after a win or a draw
    def end(self):
        if self.__game_state is GameState.END_DRAW:
            self.__active_player.msg_pg(PregenMessages.END_PLAYER_DRAW)
            self.__inactive_player.msg_pg(PregenMessages.END_PLAYER_DRAW)
        elif self.__game_state is GameState.END_WIN:
            self.__active_player.msg_pg(PregenMessages.END_PLAYER_WIN)
            self.__inactive_player.msg_pg(PregenMessages.END_PLAYER_LOOSE)
        if self.__loop:
            sleep(3)
            self.reset()

    # resets the game, basically by clearing the board
    def reset(self):
        print(">> Game reset.")
        self.__game_state: GameState = GameState.INIT
        self.__board: Board = Board(self.__board.get_length(), self.__board.get_height())

        print(">> Game initialized.")
        self.start()
