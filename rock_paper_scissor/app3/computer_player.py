# playerComputer.py

from player import Player
import random

class PlayerComputer(Player):
    def __init__(self):
        super().__init__()
        self._name = "computer_"+str(random.choice([1,2,3]))
    
    @property
    def name(self):
        return self._name
    
    def generate_move(self):
        print("Generating move....")
        input_move = random.choice(["R","P","S"])
        self._moves.append(input_move)
        return input_move

    def __str__(self):
        computer_player_display_string=f"Player({self._name}, {self._score}, {self._moves})"
        return computer_player_display_string
    
    def __repr__(self):
        computer_player_display_string=f"Player(name={self._name}, score={self._score}, moves={self._moves})"
        return computer_player_display_string
    
    

