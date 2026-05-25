
from colorama import Fore, init
import time
import random

# Initialize colorama
init(autoreset=True)

# Game Board
game_board = [" " for _ in range(9)]

# Score Tracking
player_score = 0
ai_score = 0
draw_score = 0

# Display Position Guide

def show_positions():

    print(Fore.YELLOW + "\n📌 Position Guide")

    print(" 1 │ 2 │ 3 ")
    print("───┼───┼───")

    print(" 4 │ 5 │ 6 ")
    print("───┼───┼───")

    print(" 7 │ 8 │ 9 ")

# Display Game Board

def show_board():

    print(Fore.CYAN + "\n")

    print(f" {game_board[0]} │ {game_board[1]} │ {game_board[2]} ")
    print("───┼───┼───")

    print(f" {game_board[3]} │ {game_board[4]} │ {game_board[5]} ")
    print("───┼───┼───")

    print(f" {game_board[6]} │ {game_board[7]} │ {game_board[8]} ")

# Reset Board

def clear_board():

    global game_board
    game_board = [" " for _ in range(9)]

# Check Winner

def winner(symbol):

    winning_patterns = [

        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for pattern in winning_patterns:

        if all(game_board[position] == symbol for position in pattern):
            return True

    return False

# Check Draw

def draw():

    return " " not in game_board

# Player Move

def human_turn():

    try:

        choice = int(
            input(Fore.YELLOW + "\n🎯 Enter position (1-9): ")
        ) - 1

        if choice < 0 or choice > 8:

            print(Fore.RED + "⚠ Invalid Position!")
            human_turn()

        elif game_board[choice] != " ":

            print(Fore.RED + "⚠ Position already occupied!")
            human_turn()

        else:

            game_board[choice] = "X"
            time.sleep(0.5)

    except ValueError:

        print(Fore.RED + "⚠ Please enter numbers only!")
        human_turn()

# Minimax Algorithm

def smart_ai(is_ai_turn):

# AI Wins
    if winner("O"):
        return 1

# Player Wins
    if winner("X"):
        return -1

# Draw
    if draw():
        return 0

# AI Turn (Maximizing)
    if is_ai_turn:

        highest_score = -999

        for spot in range(9):

            if game_board[spot] == " ":

                game_board[spot] = "O"

                score = smart_ai(False)

                game_board[spot] = " "

                highest_score = max(highest_score, score)

        return highest_score

# Player Turn (Minimizing)
    else:

        lowest_score = 999

        for spot in range(9):

            if game_board[spot] == " ":

                game_board[spot] = "X"

                score = smart_ai(True)

                game_board[spot] = " "

                lowest_score = min(lowest_score, score)

        return lowest_score

# AI Move

def computer_turn():

    ai_messages = [

        "🤖 AI is calculating the best move...",
        "🧠 Thinking strategically...",
        "⚡ Predicting your next move...",
        "🎯 AI is planning something..."
    ]

    print(Fore.MAGENTA + "\n" + random.choice(ai_messages))

    time.sleep(1)

    best_score = -999
    best_position = 0

    for spot in range(9):

        if game_board[spot] == " ":

            game_board[spot] = "O"

            score = smart_ai(False)

            game_board[spot] = " "

            if score > best_score:

                best_score = score
                best_position = spot

    print(Fore.CYAN + f"🤖 AI selected position {best_position + 1}")

    game_board[best_position] = "O"

# Main Game Loop

while True:

    clear_board()

    print(Fore.GREEN + "\n" + "═" * 50)
    print("🤖 Welcome to ShraddhaXO AI")
    print("🎮 Challenge the Unbeatable Computer!")
    print("═" * 50)

    show_positions()

# Gameplay Loop
    while True:

        show_board()

        print(Fore.YELLOW + "\n❌ Your Turn")
        human_turn()

# Player Wins
        if winner("X"):

            show_board()

            print(Fore.GREEN + "\n🏆 Congratulations! You defeated the AI!")

            player_score += 1

            break

# Draw Check
        if draw():

            show_board()

            print(Fore.CYAN + "\n🤝 Match Draw!")

            draw_score += 1

            break

# AI Turn
        computer_turn()

# AI Wins
        if winner("O"):

            show_board()

            ai_win_messages = [

                "💀 AI Wins! Humans still need practice.",
                "🤖 Victory achieved by the machine!",
                "⚡ AI predicted all your moves!",
                "🧠 The AI remains undefeated!"
            ]

            print(Fore.RED + "\n" + random.choice(ai_win_messages))

            ai_score += 1

            break

# Draw Check
        if draw():

            show_board()

            print(Fore.CYAN + "\n🤝 Match Draw!")

            draw_score += 1

            break

# Scoreboard

    print(Fore.BLUE + "\n📊 SCOREBOARD")
    print(Fore.GREEN + f"🏆 Player Wins : {player_score}")
    print(Fore.RED + f"🤖 AI Wins     : {ai_score}")
    print(Fore.CYAN + f"🤝 Draws       : {draw_score}")

# Replay Option
    play_again = input(
        Fore.YELLOW + "\n🔁 Do you want to play again? (yes/no): "
    ).lower()

    if play_again != "yes":

        print(Fore.GREEN + "\n👋 Thanks for playing ShraddhaXO AI!")
        break