# player class for storing player related data
import random
import time

import config
from pregenmessages import PregenMessages


class Player:
    # inits player with name, rgb color and an identifying symbol
    def __init__(self, name: str, color: list, identifier: str, human: bool = False):
        self.__name: str = name
        self.__color: list = color  # should be like [255, 255, 255]
        self.__human = human

        # for representation on the board and for checking during runtime. if both players have the same id,
        # they are treated as if they were in one team. this can be a possibility for more features, but
        # will be unwanted in most cases. It also will be used for console prints.
        self.__identifier: str = identifier

    def get_name(self) -> str:
        return self.__name

    def get_color(self) -> list:
        return self.__color

    def get_identifier(self) -> str:
        return self.__identifier

    # print custom message
    def msg(self, message: str):
        print('[%s]: %s' % (self.__identifier, message))

    # prints pregenerated messages
    def msg_pg(self, message: PregenMessages):
        msgs: dict = {
            PregenMessages.AWAIT_USER_INPUT: 'Awaiting Input: ',
            PregenMessages.INPUT_ERR_OUT_OF_RANGE: 'ERROR! Input out of range.',
            PregenMessages.INPUT_ERR_COLUMN_FULL: 'ERROR! Column already full.',
            PregenMessages.END_PLAYER_DRAW: 'No winner! The game ends in a draw.',
            PregenMessages.END_PLAYER_WIN: 'You win! Congratulations!',
            PregenMessages.END_PLAYER_LOOSE: 'You lost!',
            PregenMessages.INPUT_ERR_NAN: 'ERROR! Input is not a Number.'
        }
        self.msg(msgs[message])

    # returns column to place marker in. if not human choose a random column
    def get_input(self) -> str:
        if self.__human:
            return input()
        else:
            time.sleep(0.1)
            value = str(random.choice(range(1, config.SIZE_X)))
            print(value)
            return value
