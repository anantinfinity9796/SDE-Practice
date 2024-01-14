# engine.py
# The responsibility of the game engine is to initialize the players, intialize the game logic and make the play and display the result

from computer_player import PlayerComputer
from human_player import PlayerHuman
from game_logic import GameLogic
from chutiya_computer import ChutiyaComputer



def create_players(input_game_type:str="HH"):
        """ Function to create players for Human-Human or Human-Computer play
            input --> game_type
            output --> tuple(player_1_object, player_2_object)
        """
        player_1_name = input("Player 1 enter your name: ")

        if len(player_1_name)==0:
            player_1 = PlayerHuman(name="player_1")
        else:
            player_1 = PlayerHuman(name=player_1_name)

        if input_game_type=="HH":
            player_2_name = input("Player 2 enter your name: ")
            if len(player_1_name)==0:
                player_2 = PlayerHuman(name='player_2')
            else:
                player_2 = PlayerHuman(name=player_2_name)
        
        if input_game_type=="HC":
            print("Initializing Computer player")
            player_2 = PlayerComputer()
            print(f"Computer Player Initialized by the name : {player_2.name}")
        
        if input_game_type=="HCC":
            print("Initializing Computer player")
            player_2 = ChutiyaComputer()
            print(f"Chituya Computer Player Initialized by the name : {player_2.name}")

        return player_1, player_2

def get_game_logic_inputs():
    input_game_type = None

    while True:
        if input_game_type not in ("HH","HC","HCC"):
            input_game_type = input("Input HH for Human-Human, HC for Human-Computer --> ")
            player_1, player_2 = create_players(input_game_type=input_game_type)
            break
        else:
            print("Invalid Game type, Enter either HH or HC")
    
    # Get max_score
    max_score = int(input("Enter Max Score : "))

    while max_score <= 0:
        print("Max Score should be greater than 0")
        max_score = int(input("Re-Enter Max Score : "))
    
    return player_1, player_2, max_score

def main():
    player_1, player_2, max_score = get_game_logic_inputs()
    game_logic = GameLogic(player_1=player_1, player_2=player_2)

    game_logic.play_game(max_score=max_score, player_1=player_1, player_2=player_2)

    return

if __name__=='__main__':
    print("=-=-=-=-=-=-=-=-= ROCK-PAPER-SCISSOR =-=-=-=-=-=-=-=-=")
    print("=-=-=-=-=-=-=-=-= Starting Game Engine =-=-=-=-=-=-=-=-=")
    print("=-=-=-=-=-=-=-=-= Initializing Game Logic =-=-=-=-=-=-=-=-=")
    
    main()