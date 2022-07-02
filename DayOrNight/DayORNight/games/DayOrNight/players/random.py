from random import randint

from games.DayOrNight.action import DayOrNightAction
from games.DayOrNight.player import DayOrNightPlayer
from games.DayOrNight.state import DayOrNightState
from games.state import State


class RandomDayOrNightPlayer(DayOrNightPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DayOrNightState):
        
        return DayOrNightAction(randint(0, state.get_num_rows()),randint(0, state.get_num_cols()),2)
# şuanlık option (ustteki return icindeki son "2" ) olarak 2 verdim cunku sadece ekleme yapabiliyor.
    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
