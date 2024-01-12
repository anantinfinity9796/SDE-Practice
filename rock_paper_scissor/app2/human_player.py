# playerHuman.py
from player import Player

class PlayerHuman(Player):
    def __init__(self, name:str='default_human_player'):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name
    
    def __str__(self):
        human_player_display_string=f"Player({self._name}, {self._score}, {self._moves})"
        return human_player_display_string
    
    def __repr__(self):
        human_player_display_string=f"Player(name={self._name}, score={self._score}, moves={self._moves})"
        return human_player_display_string
    
    