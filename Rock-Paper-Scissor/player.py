# player.py


class Player():
    """ Class defining the player and its methods to play the game"""

    def __init__(self, name:str='default_player', score:int=0, moves:list=[] ) -> None:
        self._name=name
        self._score=score
        self._moves=moves

    @property
    def score(self):
        """ Getter Method for score attribute"""
        return self._score
    
    @property
    def name(self):
        """ Getter method for the name attribute"""
        return self._name
    
    @property
    def moves(self):
        """ Getter method for moves list"""
        return self._moves
    
    def increase_score(self):
        self._score+=1
        return
        