from enum import Enum, auto


class GameState(Enum):
    INIT = auto()
    RUN = auto()
    RUN_AWAIT_INPUT = auto()
    END_WIN = auto()
    END_DRAW = auto()
    ERR = auto()
