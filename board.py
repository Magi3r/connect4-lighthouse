# Board class for managing the board
from player import Player


class Board:
    def __init__(self, x: int = 13, y: int = 7):
        self.__length: int = x  # default size is 13
        self.__height: int = y  # default size is 7
        self.__board: list = [None] * x * y
        print(len(self.__board))

    def get_board(self) -> list:
        return self.__board

    def get_length(self) -> int:
        return self.__length

    def get_height(self) -> int:
        return self.__height

    def set_marker(self, col: int, active_player: Player, inactive_player: Player, animations: bool,
                   animation_callback=lambda board: None) -> None:
        pos: int = col
        for i in range(col, (self.__height - 1) * self.__length + col + 1, self.__length):
            if self.__board[i] is active_player.get_identifier() or self.__board[i] is inactive_player.get_identifier():
                self.__board[pos] = active_player.get_identifier()
                return
            else:
                if animations:
                    self.__board[pos] = active_player.get_identifier()
                    animation_callback(self)
                    self.__board[pos] = None
                pos = i
        self.__board[pos] = active_player.get_identifier()

    def check_win(self, player: Player) -> bool:
        return self.__check_rows(player) or self.__check_cols(player) or self.__check_diag(player)

    def check_draw(self) -> bool:
        return None not in self.__board

    def __check_rows(self, player: Player) -> bool:
        for y in range(self.__height):
            for x in range(self.__length - 3):
                if self.__check_row(x, y, player):
                    return True
        return False

    def __check_cols(self, player: Player) -> bool:
        for y in range(self.__height - 3):
            for x in range(self.__length):
                if self.__check_col(x, y, player):
                    return True
        return False

    def __check_diag(self, player: Player) -> bool:
        for y in range(self.__height):
            for x in range(self.__length):
                if self.__check_left_diag(x, y, player):
                    return True
                if self.__check_right_diag(x, y, player):
                    return True
        return False

    def __check_row(self, x: int, y: int, player: Player) -> bool:
        start: int = y * self.__length + x
        for pos in range(start, start + 4):
            if not self.__board[pos] is player.get_identifier():
                return False
        return True

    def __check_col(self, x: int, y: int, player: Player) -> bool:
        start: int = y * self.__length + x
        for i in range(4):
            if not self.__board[start + i * self.__length - 1] is player.get_identifier():
                return False
        return True

    def __check_left_diag(self, x: int, y: int, player: Player) -> bool:
        for i in range(1, 5):
            pos = y * self.__length + x
            if pos > len(self.__board) - 1 or self.__board[pos] is not player.get_identifier():
                return False
            y += 1
            x -= 1
        return True

    def __check_right_diag(self, x: int, y: int, player: Player) -> bool:
        for i in range(1, 5):
            pos = y * self.__length + x
            if y > self.__height - 1 or x > self.__length - 1 or self.__board[pos] is not player.get_identifier():
                return False
            y += 1
            x += 1
        return True
