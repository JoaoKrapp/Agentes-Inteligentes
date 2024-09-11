import matplotlib.pyplot as plt
import time

from board import Board
from cleaner import Cleaner

BOARD_ARRAY = [
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 2],
]

board = Board(BOARD_ARRAY)
cleaner = Cleaner(board)


def main():
    for i in range(10):
        cleaner.show_board()
        movement_successful = cleaner.move_right()

        if not movement_successful:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
