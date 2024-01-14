# game.py

class GameLogic():
    def __init__(self, player_1, player_2):
        """ The constructor for the game logic class is initialized with the player_1 and player_2 objects and rules_dict and label_dict"""

        self.player_1 = player_1
        self.player_2 = player_2

        self._rules = {'R':{'beats':'S'},
                 'S':{'beats':'P'},
                 'P':{'beats':'R'}
                }
        self._label_dict = {"R":"Rock", "P":"Paper","S":"Scissor"}
        
    @property
    def rules(self):
        return self._rules
    
    def calculate_result(self, player_1, player_2):

        print()
        print("""Choices --> R : Rock; P : Paper ; S : Scissor""")
        print()

        move_1, move_2 = player_1.generate_move(), player_2.generate_move()
        # drop in a check if it a valid move or not:
        if move_1 not in self._rules.keys():
            raise ValueError(f"{move_1} not a valid move")
            return
        elif move_2 not in self._rules.keys():
            raise ValueError(f"{move_2} not a valid move")
            return
        else:      
            if move_1 == move_2:
                print("Both the player playes the same move, the scores remains the same")
                self.display_result(player_1, player_2)
            elif self._rules[move_1]['beats'] == move_2:
                player_1.increase_score()
                self.display_result(player_1, player_2)
            elif self._rules[move_2]['beats'] == move_1:
                player_2.increase_score()
                self.display_result(player_1, player_2)

        
        print(f"D : {player_1.moves}")
        print(f"D : {player_2.moves}")        

    
    def display_result(self, player_1, player_2, last_round=False):

        print(f"{player_1.name} showed {self._label_dict[player_1.moves[-1]]} | {player_2.name} showed {self._label_dict[player_2.moves[-1]]}")
        score_string = f"=-=-=-=-= {player_1.name} = {player_1.score} | {player_2.name} = {player_2.score} =-=-=-=-=-= "
        if last_round:
            if player_1.score > player_2.score:
                    print()
                    print(f"GAME OVER : {player_1.name} WINS !!! | {player_2.name} will give party to {player_1.name}")
                    print()
                    print("=-=-=-=-=-=-=-=-= Final Scores =-=-=-=-=-=-=-=-=")
                    print(score_string)
            if player_1.score < player_2.score:
                    print()
                    print(f"GAME OVER : {player_2.name} WINS !!! | {player_1.name} will give party to {player_2.name}")
                    print()
                    print("=-=-=-=-=-=-=-=-= Final Scores =-=-=-=-=-=-=-=-=")
                    print(score_string)
            elif player_1.score == player_2.score:
                print("Both the players played same move")
                print()
                print(f"The Game ends in a draw with the scores --> {player_1.name} = {player_1.score} | {player_2.name} = {player_2.score}")
        else:
            print(score_string)
            
        return
    
    
    
    def play_game(self, max_score:int, player_1, player_2):
        num_rounds = 0
        while ((player_1.score < max_score) and (player_2.score < max_score) and (num_rounds<max_score*2)):
            
            self.calculate_result(player_1=player_1, player_2=player_2)
            # self.display_result(player_1=player_1, player_2=player_2)
            num_rounds+=1
        else:
            if (num_rounds==max_score*2) and (player_1.score == player_2.score):
                print("=-=-=-=-=-=-=-=-= SCORES DRAW | LAST ROUND | SUDDEN DEATH =-=-=-=-=-=-=-=-=")
                self.calculate_result(player_1=player_1, player_2=player_2)
                self.display_result(player_1=player_1, player_2 = player_2, last_round=True)
            else:        
                self.display_result(player_1=player_1, player_2=player_2, last_round=True)
