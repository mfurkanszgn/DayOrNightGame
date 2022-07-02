from games.DayOrNight.action import DayOrNightAction
from games.DayOrNight.player import DayOrNightPlayer
from games.DayOrNight.state import DayOrNightState


class HumanDayOrNightPlayer(DayOrNightPlayer):

    def __init__(self, name):
        super().__init__(name)
    
    def get_action(self, state: DayOrNightState):
        state.display()
        move=1
        drop=2
        
        while True:
            # noinspection PyBroadException
            try:
                
                print("Move  1")
                print("Drop  2")
                option= int(input("Chose option"))
                if option==1 or option==2 :
                  
                    return DayOrNightAction((int(input(f"Player {state.get_acting_player()}, choose a row: "))),
                                          (int(input(f"Player {state.get_acting_player()}, choose a column: "))),option)
                else :
                    state.display()
            except Exception:
                
                continue

    def event_action(self, pos: int, action, new_state: DayOrNightState):
        # ignore
        pass

    def event_end_game(self, final_state: DayOrNightState):
        # ignore
        pass
