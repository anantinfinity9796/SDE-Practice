# player.py
from abc import ABC

class Player(ABC):
    """ Class player is the base class of any type of player. It has the score as the only attribute"""
    def __init__(self):
        self._score = 0
        self._moves = []

    # Now we need the getter method of the base class
    @property
    def score(self):
        return self._score
    
    # Now we need the getter moves of the base class
    @property
    def moves(self):
        return self._moves
    
    def increase_score(self):
        self._score+=1
        return

    def add_move(self, move):
        self._moves.append(move)
        return

    def __str__(self):
        return f"Player(score={self._score}, moves={self._moves})"
    
    def __repr__(self):
        player_display_string=f"Player(score={self._score}, moves={self._moves})"
        return player_display_string
        