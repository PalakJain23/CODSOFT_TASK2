import math

board = [" " for _ in range(9)]

def reset_board():
    global board
    board = [" " for _ in range(9)]


def print_board():
    print()
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")
    print()


def check_winner(b, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(b[pos] == player for pos in combo) for combo in win_combinations)


def is_full(b):
    return " " not in b


def available_moves(b):
    return [i for i in range(9) if b[i] == " "]


def minimax(b, depth, alpha, beta, is_maximizing):
    if check_winner(b, "O"):
        return 1
    elif check_winner(b, "X"):
        return -1
    elif is_full(b):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in available_moves(b):
            b[move] = "O"
            eval = minimax(b, depth + 1, alpha, beta, False)
            b[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves(b):
            b[move] = "X"
            eval = minimax(b, depth + 1, alpha, beta, True)
            b[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def ai_move():
    best_score = -math.inf
    best_move = None
    for move in available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, -math.inf, math.inf, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = "O"


def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in available_moves(board):
                board[move] = "X"
                break
            else:
                print("Invalid move! Try again.")
        except:
            print("Please enter a number between 1 and 9.")


from tic_tac_toe import *

def play_game():
    reset_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and AI is 'O'.")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()
        if check_winner(board, "O"):
            print("💻 AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
