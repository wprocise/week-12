import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt


def update_board(current_board):
    # your code here ...
    # Copy board to not overwrite it
    board = current_board.copy()
    
    # Create new board from current board
    new_board = np.zeros_like(board)

    # Pad the array to stop the cells from wrapping and fewer neighbors
    padded = np.pad(board, pad_width=1, mode='constant', constant_values=0)

    # Count neighbors starting with top row, then left/right, then bottom row
    neighbor_count = (
        padded[0:-2, 0:-2] + padded[0:-2, 1:-1] + padded[0:-2, 2:] +
        padded[1:-1, 0:-2]                    + padded[1:-1, 2:] +   
        padded[2:,    0:-2] + padded[2:,    1:-1] + padded[2:,    2:]
    )




def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life. In this array, ` represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='plasma', cbar=False, square=True)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)