from games.DayOrNight.players.minimax import MinimaxDayOrNightPlayer
from games.DayOrNight.players.random import RandomDayOrNightPlayer
from games.DayOrNight.simulator import DayOrNightSimulator
from games.game_simulator import GameSimulator
from games.DayOrNight.players.human import HumanDayOrNightPlayer
def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 10
    #1000

    DayOrNight_simulations = [
        #uncomment to play as human
        # {
        #     "name": "Connect4 - Human VS Random",
        #     "player1": HumanConnect4Player("Human"),
        #     "player2": RandomConnect4Player("Random")
        # },
        {
            
              "name": "DayOrNight - Human VS Minimax",
              "player2": HumanDayOrNightPlayer("Human"),
              "player1": MinimaxDayOrNightPlayer("Minimax"),
              
              
            
            
            
            
            
        },
        # {
            
        #       "name": "Connect4 - Human VS Greedy",
        #     "player1": HumanConnect4Player("Human"),
        #     "player2": GreedyConnect4Player("Greedy")
            
        # },
        # {
        #     "name": "Connect4 - Random VS Random",
        #     "player1": RandomConnect4Player("Random 1"),
        #     "player2": RandomConnect4Player("Random 2")
        # },
        # {
        #     "name": "Connect4 - Greedy VS Random",
        #     "player1": GreedyConnect4Player("Greedy"),
        #     "player2": RandomConnect4Player("Random")
        # },
        # {
        #     "name": "Minimax VS Random",
        #     "player1": MinimaxConnect4Player("Minimax"),
        #     "player2": RandomConnect4Player("Random")
        # },
        # {
        #     "name": "Minimax VS Greedy",
        #     "player1": MinimaxConnect4Player("Minimax"),
        #     "player2": GreedyConnect4Player("Greedy")
        # }
    ]


    for sim in DayOrNight_simulations:
        run_simulation(sim["name"], DayOrNightSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
