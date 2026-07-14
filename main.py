import numpy as np

empty_board = np.full((3, 3), ' ')


def print_tic_tac_toe(matrix):
    row_strings = [
        f" {matrix[i, 0]} | {matrix[i, 1]} | {matrix[i, 2]} " for i in range(3)]
    print("\n-----------\n".join(row_strings))


def make_move(matrix, row, col, player):
    matrix[row, col] = player
    return matrix


def current_player(matrix):
    # X goes first; when X and O counts are equal it's X's turn,
    # otherwise O plays to catch up.
    x_count = np.count_nonzero(matrix == 'X')
    o_count = np.count_nonzero(matrix == 'O')
    return 'X' if x_count == o_count else 'O'


# --- SIMPLE GAME LOOP ---
board = empty_board

print("Game started! Enter coordinates from 0 to 2 (e.g., 1 1 for center)")

while True:
    print_tic_tac_toe(board)
    player = current_player(board)

    # Get user input and split it into row and column integers
    move = input(f"\nPlayer {player}, enter row and col (e.g., 0 2): ").split()
    row, col = int(move[0]), int(move[1])

    # Check if the spot is already taken
    if board[row, col] != ' ':
        print("Spot taken! Try a different move.")
        continue  # Skips the rest of the loop and asks the same player again

    # Apply the move to your matrix
    board = make_move(board, row, col, player)
