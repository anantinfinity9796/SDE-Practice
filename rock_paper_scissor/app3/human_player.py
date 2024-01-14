# playerHuman.py
from player import Player
import getpass

class PlayerHuman(Player):
    def __init__(self, name:str):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name
    
    def generate_move(self):

        input_move = getpass.getpass(f"{self._name}(R/P/S):")
        
        # Add the move to the players moves list
        self._moves.append(input_move)

        return input_move
    
    def __str__(self):
        human_player_display_string=f"Player({self._name}, {self._score}, {self._moves})"
        return human_player_display_string
    
    def __repr__(self):
        human_player_display_string=f"Player(name={self._name}, score={self._score}, moves={self._moves})"
        return human_player_display_string
    
    