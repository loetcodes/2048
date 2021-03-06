#!/usr/bin/env python3
#--------------------------------------------------------------------
#
# Version: 1.0.0
# Date: 11-04-2020
# Author: loet
# Copyright: loet
# License: MIT license
#
#--------------------------------------------------------------------

"""
2048 main game play.
Models the game rules.
Works on any arbitrary width and height.
"""

import random
import utils
import constants


class TwentyFortyEight:
    """
    Runs the main game logic.
    Given a width and height, creates a 2048 game board with functionality.
    """
    def __init__(self, grid_width, grid_height):
        self._grid_cols = grid_width
        self._grid_rows = grid_height
        self._directions = dict()
        self._grid_values = []
        self._result = ""
        self._directions[constants.UP] = [(0, col) for col in range(self._grid_cols)]
        self._directions[constants.DOWN] = [(self._grid_rows - 1, col)
                                            for col in range(self._grid_cols)]
        self._directions[constants.LEFT] = [(row, 0) for row in range(self._grid_rows)]
        self._directions[constants.RIGHT] = [(row, self._grid_cols - 1)
                                             for row in range(self._grid_rows)]
        self.initialize_game()


    def __str__(self):
        """ Creates a string representation of the board.
        Primarily used for debugging.
        """
        board_str = [str(row) for row in self._grid_values]
        return "\n".join(board_str)


    def get_grid_height(self):
        """ Gets the height of the board.
        """
        return self._grid_rows


    def get_grid_width(self):
        """ Gets the width of the board.
        """
        return self._grid_cols


    def get_empty_positions(self):
        """ Gets a list of tuples with the empty positions.
        """
        empty_cells = []
        if self._grid_values:
            for row in range(self._grid_values):
                for col in range(row):
                    if self._grid_values[row][col] == 0:
                        empty_cells.append((row, col))
        return empty_cells


    def new_tile(self):
        """ Creates a new tile in a random empty position.
        Tile is 2 90% of the time or 4.
        """
        tile_options = [2] * 9 + [4]
        tile_row = random.randrange(0, self._grid_rows)
        tile_col = random.randrange(0, self._grid_cols)

        # Keep looking for a zero
        while self.get_tile(tile_row, tile_col) != 0:
            tile_row = random.randrange(0, self._grid_rows)
            tile_col = random.randrange(0, self._grid_cols)
        if self._grid_values and self._grid_values[tile_row][tile_col] == 0:
            tile_value = random.choice(tile_options)
            self.set_tile(tile_row, tile_col, tile_value)


    def get_tile(self, row, col):
        """ Gets a tile in the (row, col) position.
        """
        return self._grid_values[row][col]


    def set_tile(self, row, col, value):
        """ Sets a tile at the (row, col) position.
        """
        self._grid_values[row][col] = value


    def get_row_col_values(self, direction, position, length):
        """ Gets the values and positions in an entire row or column.
        """
        line_values = []
        line_section = []
        for num in range(length):
            row = position[0] + num * constants.OFFSETS[direction][0]
            col = position[1] + num * constants.OFFSETS[direction][1]
            tile = self.get_tile(row, col)
            line_values.append(tile)
            line_section.append((row, col))
        return line_values, line_section


    def get_score(self):
        """ Gets the current grid score.
        """
        return self._score

    def get_final_result(self):
        """ Gets the final game result
        """
        return self._result


    def set_final_result(self):
        """ Game is over, sets the final result. Game is won if their is
        atleast one 2048 tile.
        """
        message = "You Lost!"
        for row in self._grid_values:
            if 2048 in row:
                message = "You Won!"
                break
        self._result = message


    def any_valid_moves(self, current_grid):
        """ Makes a move in each direction checking if each position contains
        the same items. If the board doesn't change in any direction returns False.
        """
        for direction in constants.DIRECTIONS.values():
            self.move(direction)
            # Check if each position contains same items
            for row, values in enumerate(current_grid):
                if len(values) == len(self._grid_values[row]):
                    total = sum([1 for i, j in zip(current_grid, self._grid_values) if i == j])
                    if len(values) != total:
                        # Return the grid to its original state
                        self._grid_values = current_grid
                        return False
        return True


    def no_valid_moves(self):
        """ Checks if there are any more valid moves that result in a change
        to the game. Returns True or False
        """
        # If zero in grid, there are valid moves
        for row in self._grid_values:
            if 0 in row:
                return False

        # No empty tiles, copy grid and check any available moves
        base_grid = [[item for item in row] for row in self._grid_values]

        return self.any_valid_moves(base_grid)


    def move(self, direction):
        """ Moves all tiles in a given direction.
        Adds a new tile if any tiles are moved.
        Returns none.
        """
        # Initialize tile change and get starting indices
        tile_change = 0
        start_tile_indices = self._directions[direction]
        if direction <= 2:
            tiles_length = self.get_grid_height()
        else:
            tiles_length = self.get_grid_width()

        # Loop over indices, adding offsets to get rows or cols and values.
        for start_pos in start_tile_indices:
            # Get values and positions in an entire row or column.
            line_values, line_section = self.get_row_col_values(direction, start_pos, tiles_length)

            # Merge tiles in a line, then set new grid values.
            new_tiles = utils.merge(line_values)
            for pos in range(tiles_length):
                new_value = new_tiles[pos]
                row = line_section[pos][0]
                col = line_section[pos][1]
                self.set_tile(row, col, new_value)
                if new_value != line_values[pos]:
                    tile_change = 1
            # Score any merged_tiles
            self._score += utils.sum_new_tiles(line_values)

        # Check if any tile changed, add new tile.
        if tile_change == 1:
            self.new_tile()


    def initialize_game(self):
        """ Resets the game to an empty board with only 2 new tiles.
        Resets the score to 0
        """
        self._score = 0
        self._result = ""
        self._grid_values = [[0 for col in range(self._grid_cols)]
                             for row in range(self._grid_rows)]
        for _ in range(2):
            self.new_tile()
