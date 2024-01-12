# engine.py
# The responsibility of the game engine is to initialize the players, intialize the game logic and make the play and display the result

from computer_player import PlayerComputer
from human_player import PlayerHuman
from game_logic import GameLogic
import getpass

label_dict = {"R":"Rock", "P":"Paper","S":"Scissor"}
def create_players(game_type:str="HH"):
    """ Function to create players for Human-Human or Human-Computer play
        input --> game_type
        output --> tuple(player_1_object, player_2_object)
    """
    player_1_name = input("Player 1 enter your name: ")

    if len(player_1_name)==0:
        player_1 = PlayerHuman(name="player_1")
    else:
        player_1 = PlayerHuman(name=player_1_name)

    if game_type=="HH":
        player_2_name = input("Player 2 enter your name: ")
        if len(player_1_name)==0:
            player_2 = PlayerHuman(name='player_2')
        else:
            player_2 = PlayerHuman(name=player_2_name)
    
    if game_type=="HC":
        print("Initializing Computer player")
        player_2 = PlayerComputer()
        print(f"Computer Player Initialized by the name : {player_2.name}")

    return player_1, player_2

def get_moves(input_game_type, player_1, player_2):
    print()
    print("""Choices:
                R --> Rock
                P --> Paper
                S --> Scissor""")
    print()
    # Get the players moves
    player_1_move = getpass.getpass(f"{player_1.name}(R/P/S):")

    if input_game_type=="HH":
        player_2_move = getpass.getpass(f"{player_2.name}(R/P/S):")
    else:
        player_2_move = player_2.generate_move()
    
    # Add respective players moves to their individual move_list
    player_1.add_move(player_1_move)
    player_2.add_move(player_2_move)
    
    print(f"{player_1.name} showed {label_dict[player_1.moves[-1]]} | {player_2.name} showed {label_dict[player_2.moves[-1]]}")
    return player_1_move, player_2_move


def play_last_round(input_game_type, player_1, player_2,):
    
    # Get the moves of the players
    player_1_move, player_2_move = get_moves(input_game_type=input_game_type, 
                                             player_1=player_1, 
                                             player_2=player_2)
    
    result = game_logic.return_result(player_1_move, player_2_move)
    if result == 0:
        # num_rounds +=1
        player_1.increase_score() 
        return      
    elif result ==1:
        # num_rounds +=1
        player_2.increase_score()
        return
    elif result==2:
        # num_rounds+=1
        return


# def display_result(result_variable, max_score, round_num,player_1, player_2, last_round=False):
def display_result(player_1, player_2, last_round=False):
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


def play_game(input_game_type:str, max_score:int, player_1, player_2):
    num_rounds = 0
    while ((player_1.score < max_score) and (player_2.score < max_score) and (num_rounds<max_score*2)):
        
        player_1_move, player_2_move = get_moves(input_game_type=input_game_type,
                                                 player_1=player_1,
                                                 player_2 = player_2)
        
        result = game_logic.return_result(player_1_move, player_2_move)

        if result == 0:
            num_rounds +=1
            player_1.increase_score()       
        elif result ==1:
            num_rounds +=1
            player_2.increase_score()
        elif result==2:
            num_rounds+=1
        print(f"D : {player_1.moves}")
        print(f"D : {player_2.moves}")
        # display_result(result_variable=result, max_score=max_score, round_num=num_rounds, player_1=player_1, player_2=player_2)
        display_result(player_1=player_1, player_2=player_2)
    else:
        # display_result(max_score, round_num=num_rounds, player_1=player_1, player_2=player_2, last_round=True)
        if (num_rounds==max_score*2) and (player_1.score == player_2.score):
            print("=-=-=-=-=-=-=-=-= SCORES DRAW | LAST ROUND | SUDDEN DEATH =-=-=-=-=-=-=-=-=")
            # This is the last round and the scores are level, then we will have to execute this condition
            # Here what it does is that we let the players place each chance and look for the winner.
            play_last_round(input_game_type=input_game_type, player_1=player_1, player_2=player_2)
            display_result(player_1=player_1, player_2 = player_2, last_round=True)
        else:        
            display_result(player_1=player_1, player_2=player_2, last_round=True)





def main():
    # Intialize the player by getting input from the user if he want to play human-human or human-computer.
    print("Want to play Human-Human or Human-Computer")
    while True:
        input_game_type = input("Input HH for Human-Human, HC for Human-Computer --> ")
        if input_game_type == "HH":
            player_1, player_2 = create_players(game_type=input_game_type)
            break
        elif input_game_type == "HC":
            player_1, player_2 = create_players(game_type=input_game_type)
            break
        else:
            print("Invalid Game type, Enter either HH or HC")
    
    # Get max_score
    max_score = int(input("Enter Max Score : "))
    while max_score<=0:
        print("Max Score should be greater than 0")
        max_score = int(input("Re-Enter Max Score : "))

    # Next step is to prompt to play the game
    # First is to get the moves from the palyers
    # player_1, player_2 = create_players(game_type=input_game_type)

    play_game(input_game_type=input_game_type, max_score=max_score, player_1=player_1, player_2=player_2)

    return

if __name__=='__main__':
    print("=-=-=-=-=-=-=-=-= ROCK-PAPER-SCISSOR =-=-=-=-=-=-=-=-=")
    print("=-=-=-=-=-=-=-=-= Starting Game Engine =-=-=-=-=-=-=-=-=")
    print("=-=-=-=-=-=-=-=-= Initializing Game Logic =-=-=-=-=-=-=-=-=")
    game_logic = GameLogic()
    main()