# rcp_main.py file
import getpass
from player import Player


rule_dict = {'R':{'beats':'S'},
                 'S':{'beats':'P'},
                 'P':{'beats':'R'}
                }
label_dict = {"R":"Rock", "P":"Paper","S":"Scissor"}

def get_result_for_move(rule_dict, player_1_move, player_2_move):
    
    if rule_dict[player_1_move]['beats'] == player_2_move:
        return 0
    elif rule_dict[player_2_move]['beats'] == player_1_move:
        return 1
    else:
        return 2



def main():
    
    player_1_name = input("Player_1 enter your name : ")
    print()
    if len(player_1_name)==0:
        player_1_name = 'default_player_1'
    player_2_name = input("Player_2 enter your name : ")
    if len(player_2_name)==0:
        player_2_name = 'default_player_2'
    print()

    max_score = int(input("Enter Max Score : "))
    while max_score<=0:
        print("Max Score should be greater than 0")
        max_score = int(input("Re-Enter Max Score : "))

            


    # create the players objects
    player_1 = Player(player_1_name)
    player_2 = Player(player_2_name)

    num_rounds = 0
    while ((player_1.score < max_score) and (player_2.score < max_score) and (num_rounds<max_score*2)):
        print()
        print("""Choices:
                    R --> Rock
                    P --> Paper
                    S --> Scissor""")
        print()
        # Get the players moves
        player_1_move = getpass.getpass(f"{player_1_name}(R/P/S):")
        player_2_move = getpass.getpass(f"{player_2_name}(R/P/S):")

        
        print(f"{player_1_name} showed {label_dict[player_1_move]} | {player_2_name} showed {label_dict[player_2_move]}")
        result = get_result_for_move(rule_dict, player_1_move=player_1_move, player_2_move=player_2_move)

        
        if result == 0:
            num_rounds +=1
            # increase the score for player_1
            player_1.increase_score()
            
        elif result ==1:
            num_rounds +=1
            # increase the score for player_2
            player_2.increase_score()
        
        elif result==2:
            num_rounds+=1
            print(f"=-=-=-=-=This round is a DRAW | SCORES Remain the same =-=-=-=-=")
            
        print(f"=-=-=-=-= {player_1_name} = {player_1.score} | {player_2_name} = {player_2.score} =-=-=-=-=-=")

    else:
        # num_rounds+=1
        if player_1.score > player_2.score:
                print()
                print(f"GAME OVER : {player_1_name} WINS !!! | {player_2_name} will give party to {player_1_name}")
                print()
                print("=-=-=-=-=-=-=-=-= Final Scores =-=-=-=-=-=-=-=-=")
                print(f"=-=-=-=-= {player_1_name} = {player_1.score} | {player_2_name} = {player_2.score} =-=-=-=-=-=")
                
                
        elif player_1.score < player_2.score:
            print()
            print(f"GAME OVER : {player_2_name} WINS !!! | {player_1_name} will give party to {player_2_name}")
            print()
            print("=-=-=-=-=-=-=-=-= Final Scores =-=-=-=-=-=-=-=-=")
            print(f"=-=-=-=-= {player_1_name} = {player_1.score} | {player_2_name} = {player_2.score} =-=-=-=-=-=")
        
        elif (player_1.score==player_2.score):
            print("=-=-=-=-=-=-=-=-= SCORES DRAW | LAST ROUND | SUDDEN DEATH =-=-=-=-=-=-=-=-=")

            player_1_move = getpass.getpass(f"{player_1_name}(R/P/S):")
            player_2_move = getpass.getpass(f"{player_2_name}(R/P/S):")

            result = get_result_for_move(rule_dict, player_1_move=player_1_move, player_2_move=player_2_move)

            if result == 0:
                # increase the number of rounds and icrease the score for player_1
                player_1.increase_score()
                print()
                print(f"GAME OVER : {player_1_name} WINS !!! | {player_2_name} will give party to {player_1_name}")
                print()
                print("=-=-=-=-=-=-=-=-= Final Scores =-=-=-=-=-=-=-=-=")
                print(f"=-=-=-=-= {player_1_name} = {player_1.score} | {player_2_name} = {player_2.score} =-=-=-=-=-=")
                
            elif result ==1:
                player_2.increase_score()
                print()
                print(f"GAME OVER : {player_2_name} WINS !!! | {player_1_name} will give party to {player_2_name}")
                print()
                print("=-=-=-=-=-=-=-=-= Final Scores =-=-=-=-=-=-=-=-=")
                print(f"=-=-=-=-= {player_1_name} = {player_1.score} | {player_2_name} = {player_2.score} =-=-=-=-=-=")
                
            elif result == 2:
                print("Both the players played same move")
                print()
                print(f"{player_1_name} showed {label_dict[player_1_move]} | {player_2_name} showed {label_dict[player_2_move]}")
                print()
                print(f"The Game ends in a draw with the scores --> {player_1_name} = {player_1.score} | {player_2_name} = {player_2.score}")
    return

if __name__=="__main__": 
    print()
    print("=-=-=-=-=-=-=-=-= ROCK-PAPER-SCISSOR =-=-=-=-=-=-=-=-=")
    print()
    # print("=-=-=-=-=-=-=-=-= Get ready to Play =-=-=-=-=-=-=-=-=")
    main()