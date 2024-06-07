
def start_game():
    player_1_score = 0
    player_2_score = 0 
    draw_score = 0

    player1 = input("Player 1, enter your name:")
    player2 = input("Player 2, enter your name:")
    player_1_score, player_2_score, draw_score = play_game(player1, player2, player_1_score, player_2_score, draw_score)
    play_again = input("Would you like to play again? Type 'y' or 'n:")
    while play_again.lower() == "y":
        player_1_score, player_2_score, draw_score = play_game(player1, player2, player_1_score, player_2_score, draw_score)
        play_again = input("Would you like to play again? Type 'y' to play again, or anything else to quit:")

def play_game(player1, player2, player_1_score, player_2_score, draw_score):

    p1 = int(input(f"{player1}, enter your choice: 1 for rock, 2 for paper, 3 for scissors: "))
    p2 = int(input(f"{player2}, enter your choice: 1 for rock, 2 for paper, 3 for scissors: "))
    # rock and rock
    if p1 == 1 and p2 == 1: 
        draw_score = draw_score + 1
        print(f"Draw: {player1} chose ROCK and {player2} chose ROCK")
    # rock and paper
    elif p1 == 1 and p2 == 2:
        player_2_score = player_2_score + 1
        print(f"{player2} wins: {player1} chose ROCK and {player2} chose PAPER")
    # paper and rock
    elif p1 == 2 and p2 == 1:
        player_1_score = player_1_score + 1
        print(f"{player1} wins: {player1} chose PAPER and {player2} chose ROCK")
    # rock and scissors 
    elif p1 == 1 and p2 == 3:
        player_1_score = player_1_score + 1
        print(f"{player1} wins: {player1} chose ROCK and {player2} chose SCISSORS")
    # scissors and rock 
    elif p1 == 3 and p2 == 1:
        player_2_score = player_2_score + 1
        print(f"{player2} wins: {player1} chose SCISSORS and {player2} chose ROCK")
    # paper and scissors
    elif p1 == 2 and p2 == 3:
        player_2_score = player_2_score + 1
        print(f"{player2} wins: {player1} chose PAPER and {player2} chose SCISSORS")
    # paper and paper
    elif p1 == 2 and p2 == 2:
        draw_score = draw_score + 1
        print(f"Draw: {player1} chose PAPER and {player2} chose PAPER")
    # scissors and scissors
    elif p1 == 3 and p2 == 3:
        draw_score = draw_score + 1
        print(f"Draw: {player1} chose SCISSORS and {player2} chose SCISSORS")
    # scissors and paper
    elif p1 == 3 and p2 == 2:
        player_1_score = player_1_score + 1
        print(f"{player1} wins: {player1} chose SCISSORS and {player2} chose PAPER")
    else:
        print("Incorrect selections - play again!")
    
    print(f"{player1} score: {player_1_score}")
    print(f"{player2} score: {player_2_score}")
    print(f"Number of draws: {draw_score}")
    return player_1_score, player_2_score, draw_score

start_game()

# # plan:
# # 9 possible options 
# 1) rock && paper - paper wins ✅
# 2) rock && scissors - Rock wins ✅
# 3) rock && rock - draw ✅
# 4) paper && scissors - scissors wins ✅
# 5) paper && paper - draw ✅
# 6) paper && rock - paper wins ✅
# 7) scissors && scissors - draw ✅
# 8) scissors && rock - rock wins ✅
# 9) scissors && paper - scissors wins
