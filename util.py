# elif (player_1.score==player_2.score):
#             print("=-=-=-=-=-=-=-=-= SCORES DRAW | LAST ROUND | SUDDEN DEATH =-=-=-=-=-=-=-=-=")

#             player_1_move = getpass.getpass(f"{player_1_name}(R/P/S):")
#             player_2_move = getpass.getpass(f"{player_2_name}(R/P/S):")

#             result = get_result_for_move(rule_dict, player_1_move=player_1_move, player_2_move=player_2_move)

#             if result == 0:
#                 # increase the number of rounds and icrease the score for player_1
#                 player_1.increase_score()
#                 print()
#                 print(f"GAME OVER : {player_1_name} WINS !!! | {player_2_name} will give party to {player_1_name}")
#                 print()
#                 print("=-=-=-=-=-=-=-=-= Final Scores =-=-=-=-=-=-=-=-=")
#                 print(f"=-=-=-=-= {player_1_name} = {player_1.score} | {player_2_name} = {player_2.score} =-=-=-=-=-=")
                
#             elif result ==1:
#                 player_2.increase_score()
#                 print()
#                 print(f"GAME OVER : {player_2_name} WINS !!! | {player_1_name} will give party to {player_2_name}")
#                 print()
#                 print("=-=-=-=-=-=-=-=-= Final Scores =-=-=-=-=-=-=-=-=")
#                 print(f"=-=-=-=-= {player_1_name} = {player_1.score} | {player_2_name} = {player_2.score} =-=-=-=-=-=")
                
#             elif result == 2:
#                 print("Both the players played same move")
#                 print()
#                 print(f"The Game ends in a draw with the scores --> {player_1_name} = {player_1.score} | {player_2_name} = {player_2.score}")