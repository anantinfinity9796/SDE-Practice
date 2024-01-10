# player.py


class Player():
    """ Class defining the player and its methods to play the game"""

    def __init__(self, name:str='default_player', score:int=0, moves:list=None ) -> None:
        self._name=name
        self._score=score
        self._moves=moves

    @property
    def score(self):
        """ Get the current score of the player"""
        return self._score
    
    @property
    def name(self):
        """ Getter method for the name property"""
        return self._name
    
    def increase_score(self):
        self._score+=1
        return
        