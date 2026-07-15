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


def legal_moves(matrix):
    # np.where returns (row_indices, col_indices); zip them into (row, col) tuples
    # so minimax can loop: for row, col in legal_moves(board): ...
    rows, cols = np.where(matrix == ' ')
    return list(zip(rows.tolist(), cols.tolist()))


def check_winner(matrix):
    """Return (player, how) if someone has won, otherwise None.
    how is a short description of the winning line.
    """
    for i in range(3):
        if matrix[i, 0] != ' ' and np.all(matrix[i, :] == matrix[i, 0]):
            return matrix[i, 0], f"row {i}"
        if matrix[0, i] != ' ' and np.all(matrix[:, i] == matrix[0, i]):
            return matrix[0, i], f"column {i}"

    if matrix[1, 1] != ' ':
        if matrix[0, 0] == matrix[1, 1] == matrix[2, 2]:
            return matrix[1, 1], "main diagonal"
        if matrix[0, 2] == matrix[1, 1] == matrix[2, 0]:
            return matrix[1, 1], "anti-diagonal"

    return None


def score(board, ai_symbol):
    """Terminal-position score from the AI's point of view.
    Returns 2 (AI win), 0 (AI loss), 1 (draw), or None if the game is still ongoing
    (minimax's recursive case — keep searching).
    """
    result = check_winner(board)
    if result is not None:
        winner, _ = result
        return 2 if winner == ai_symbol else 0

    if not legal_moves(board):
        return 1

    return None


def minimax(board, ai_symbol):
    """Score this position assuming both sides play optimally.

    On the AI's turn we take the move with the highest score (best case for us).
    On the opponent's turn we take the move with the lowest score (worst case for us).
    That way the value of a move is its best guaranteed outcome — the best worst-case.
    """
    terminal = score(board, ai_symbol)
    if terminal is not None:
        return terminal

    player = current_player(board)
    moves = legal_moves(board)

    if player == ai_symbol:
        best = 0  # worst possible score; we try to improve
        for row, col in moves:
            next_board = board.copy()
            make_move(next_board, row, col, player)
            best = max(best, minimax(next_board, ai_symbol))
        return best

    # Opponent: pick the move that hurts the AI the most
    best = 2  # best possible for AI; opponent tries to worsen it
    for row, col in moves:
        next_board = board.copy()
        make_move(next_board, row, col, player)
        best = min(best, minimax(next_board, ai_symbol))
    return best


def best_move(board, ai_symbol):
    """Try every legal move and return the (row, col) with the best minimax score."""
    chosen = None
    best_score = -1
    for row, col in legal_moves(board):
        next_board = board.copy()
        make_move(next_board, row, col, ai_symbol)
        move_score = minimax(next_board, ai_symbol)
        if move_score > best_score:
            best_score = move_score
            chosen = (row, col)
    return chosen


# --- GAME LOOP: you are X, the minimax bot is O ---
if __name__ == "__main__":
    AI_SYMBOL = 'O'
    board = empty_board.copy()

    print("Game started! You are X, the bot is O.")
    print("Enter coordinates from 0 to 2 (e.g., 1 1 for center)")

    while True:
        print_tic_tac_toe(board)
        player = current_player(board)

        if player == AI_SYMBOL:
            row, col = best_move(board, AI_SYMBOL)
            print(f"\nBot plays at {row} {col}")
        else:
            move = input(f"\nPlayer {player}, enter row and col (e.g., 0 2): ").split()
            row, col = int(move[0]), int(move[1])
            if board[row, col] != ' ':
                print("Spot taken! Try a different move.")
                continue

        board = make_move(board, row, col, player)

        result = check_winner(board)
        if result is not None:
            winner, how = result
            print_tic_tac_toe(board)
            print(f"\nPlayer {winner} wins on the {how}!")
            break

        if not legal_moves(board):
            print_tic_tac_toe(board)
            print("\nIt's a draw — no empty spots left.")
            break
