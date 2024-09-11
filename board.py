class Board:
    CLEAN_TILE = 0
    WALL_TILE = 1
    DIRT_TILE = 2

    def __init__(self, board_array: list):
        self.board_array = board_array
        self.board_size = len(self.board_array)

    def generate_dirt(self, dirt_quantity: int):

        # TODO:
        number_of_dirt_in_board = 0
        print(self.board_array)
