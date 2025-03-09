import random

# Function to display the game board
def display_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


# Function to check for a winner
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False


# Function to check for a draw
def check_draw(board):
    return "_" not in board


# Minimax algorithm for AI move
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "O"):  # AI win
        return 1
    if check_winner(board, "X"):  # Player win
        return -1
    if check_draw(board):  # Draw
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        available_moves = [i for i, spot in enumerate(board) if spot == "_"]
        for move in available_moves:
            board[move] = "O"  # AI move
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = "_"
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        available_moves = [i for i, spot in enumerate(board) if spot == "_"]
        for move in available_moves:
            board[move] = "X"  # Player move
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = "_"
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


# Function for AI move using Minimax
def ai_move(board):
    best_move = -1
    best_value = float('-inf')
    available_moves = [i for i, spot in enumerate(board) if spot == "_"]

    for move in available_moves:
        board[move] = "O"  # AI move
        move_value = minimax(board, 0, False, float('-inf'), float('inf'))
        board[move] = "_"

        if move_value > best_value:
            best_value = move_value
            best_move = move

    return best_move


# Function to play a game
def play_game():
    while True:
        board = ["_" for _ in range(9)]  # Initialize the board with underscores
        current_player = "X"  # Player X starts the game
        ai_player = "O"  # AI will be "O"

        while True:
            display_board(board)

            # Player's turn
            if current_player == "X":
                try:
                    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
                    if board[move] != "_":
                        print("That space is already taken. Try again.")
                        continue
                except (ValueError, IndexError):
                    print("Invalid move. Please enter a number between 1 and 9.")
                    continue
            # AI's turn
            else:
                print(f"AI ({ai_player}) is making its move...")
                move = ai_move(board)

            board[move] = current_player

            # Check if the current player has won
            if check_winner(board, current_player):
                display_board(board)
                if current_player == "X":
                    print("Player X wins!")
                else:
                    print("AI (O) wins!")
                break

            # Check for a draw
            if check_draw(board):
                display_board(board)
                print("It's a draw!")
                break

            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

        # Ask if the players want to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break


# Run the game
if __name__ == "__main__":
    play_game()