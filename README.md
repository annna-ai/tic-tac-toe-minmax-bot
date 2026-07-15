
# Tic-Tac-Toe AI (Minimax)

A Python implementation of Tic-Tac-Toe where you play against an AI powered by the **Minimax algorithm**. The AI evaluates every possible move and always chooses the best available option, making it impossible to beat when played correctly.

## Features

* Human vs. AI gameplay
* AI uses the **Minimax algorithm** for optimal decision-making
* Built with **NumPy** for board management
* Detects wins across rows, columns, and diagonals
* Detects draw conditions
* Simple command-line interface

## How It Works

The game board is stored as a **3×3 NumPy array**. The human player is **X**, and the AI is **O**.

On each turn, the AI:

1. Finds all legal moves.
2. Simulates every possible future game using the **Minimax algorithm**.
3. Scores each move based on whether it leads to a win, loss, or draw.
4. Selects the move with the highest guaranteed outcome.

Because Minimax assumes both players make the best possible decisions, the AI will always play optimally.

## Requirements

* Python 3.x
* NumPy

Install NumPy with:

```bash
pip install numpy
```

## Running the Game

Run the program with:

```bash
python tic_tac_toe.py
```

You will be prompted to enter a row and column (0–2) for each move.

Example:

```text
Player X, enter row and col (e.g., 0 2):
```

## Project Structure

* `print_tic_tac_toe()` – Displays the game board.
* `make_move()` – Places a player's symbol on the board.
* `current_player()` – Determines whose turn it is.
* `legal_moves()` – Returns all available moves.
* `check_winner()` – Checks for winning rows, columns, or diagonals.
* `score()` – Evaluates terminal game states.
* `minimax()` – Recursively evaluates every possible move.
* `best_move()` – Selects the AI's optimal move.

## Future Improvements

* Add alpha-beta pruning to improve Minimax performance.
* Create a graphical interface using Pygame or Tkinter.
* Allow players to choose whether to play as X or O.
* Add multiple difficulty levels.
* Improve input validation for invalid coordinates.

## License

This project is open source and available under the MIT License.
