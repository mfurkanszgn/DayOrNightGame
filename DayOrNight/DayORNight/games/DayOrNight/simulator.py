from games.DayOrNight.player import DayOrNightPlayer
from games.DayOrNight.state import DayOrNightState
from games.game_simulator import GameSimulator


class DayOrNightSimulator(GameSimulator):

    def __init__(self, player1: DayOrNightPlayer, player2: DayOrNightPlayer, num_rows: int =7, num_cols: int =7):
        super(DayOrNightSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the DayOrNight grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_game(self):
        return DayOrNightState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: DayOrNightState):
        # ignored for this simulator
        pass

    def end_game(self, state: DayOrNightState):
        # ignored for this simulator
        pass
