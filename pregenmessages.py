from enum import Enum, auto


class PregenMessages(Enum):
    AWAIT_USER_INPUT = auto()
    INPUT_ERR_NAN = auto()
    INPUT_ERR_OUT_OF_RANGE = auto()
    INPUT_ERR_COLUMN_FULL = auto()
    END_PLAYER_DRAW = auto()
    END_PLAYER_WIN = auto()
    END_PLAYER_LOOSE = auto()
