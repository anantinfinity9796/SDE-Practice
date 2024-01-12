# game.py

class GameLogic():
    def __init__(self):
        self._rules = {'R':{'beats':'S'},
                 'S':{'beats':'P'},
                 'P':{'beats':'R'}
                }
        
    @property
    def rules(self):
        return self._rules
    
    def return_result(self, move_1, move_2):
        # drop in a check if it a valid move or not:
        if move_1 not in self._rules.keys():
            raise ValueError(f"{move_1} not a valid move")
            return
        elif move_2 not in self._rules.keys():
            raise ValueError(f"{move_2} not a valid move")
            return
        else:      
            if move_1 == move_2:
                return 2
            elif self._rules[move_1]['beats'] == move_2:
                return 0
            elif self._rules[move_2]['beats'] == move_1:
                return 1
        
