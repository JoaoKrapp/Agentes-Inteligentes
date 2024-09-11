import random
import matplotlib.pyplot as plt

from board import Board


class Cleaner:
    def __init__(self, board: Board):
        self.board = board
        self.pos_x, self.pos_y = self.generate_random_position()

    def generate_random_position(self):
        """
        Generates a random position on the board that is not a wall tile
        """

        agent_position_x = random.randint(0, self.board.board_size - 1)
        agent_position_y = random.randint(0, self.board.board_size - 1)

        while self.board.board_array[agent_position_x][agent_position_y] == self.board.WALL_TILE:
            agent_position_x = random.randint(0, self.board.board_size - 1)
            agent_position_y = random.randint(0, self.board.board_size - 1)

        return 0, 0
        # return agent_position_x, agent_position_y

    def show_board(self):
        """
        Displays the board using matplotlib
        """

        # Change the color scheme
        plt.imshow(self.board.board_array, 'gray')
        plt.nipy_spectral()

        # Setting agent in the environment
        plt.plot([self.pos_x], [self.pos_y], marker='o', color='r', ls='')

        plt.show(block=False)

        # Wait 0.5 second to see the cleaner working
        plt.pause(1)
        plt.clf()

    def detect_out_of_bounds(self, new_position) -> bool:
        """
        Detects if the cleaner is going out of the array, no matter what coordinate we are talking about,
        it should never be less than 0 or greater than 5
        """
        if (new_position > self.board.board_size - 1) or new_position < 0:
            return True
        else:
            return False

    def move_right(self) -> bool:
        """
        Moves the cleaner right by one
        :returns: If the movement was successful
        """

        try:
            new_x_position = self.pos_x + 1
            wall_collision = self.board.board_array[self.pos_y][new_x_position] == self.board.WALL_TILE

            # Verify collisions
            if wall_collision:
                return False
            else:
                self.pos_x += 1
                return True

        except IndexError:
            return False


