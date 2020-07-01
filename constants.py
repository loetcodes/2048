#!/usr/bin/env python3
#--------------------------------------------------------------------
#
# Version: 1.0.0
# Date: 11-04-2020
# Author: loet
#
# MIT License
# Copyright (c) 2020 Louisa
#
#--------------------------------------------------------------------

"""
General Constants for 2048 Game.
"""

# Window and Grid size constants
WIDTH = 900
HEIGHT = 600
MIN_SIDE_PANEL = 300
GRID_SIZE = 4
GRID_PADDING = 10

# Direction values
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Basic texts
GAME_TITLE = "2048"
SCORE_TITLE = "Score"
NEW_GAME_TITLE = "NEW GAME"
INSTRUCTIONS = """ Use the arrow keys to
    merge the tiles to \n get the 2048 tile!"""

# Directions
DIRECTIONS = {
    "Up": UP,
    "Down": DOWN,
    "Left": LEFT,
    "Right": RIGHT
}

# Offsets for computing direction indices
OFFSETS = {
    UP: (1, 0),
    DOWN: (-1, 0),
    LEFT: (0, 1),
    RIGHT: (0, -1)
}

# Font
FONT = ("Verdana", 32, "bold")
TITLE_FONT = ("Verdana", 40, "bold")
TEXT_FONT = ("Verdana", 16, "bold")
SCORE_FONT = ("Verdana", 18, "bold")
BUTTON_FONT = ("Verdana", 14, "bold")

GAME_THEMES = {
    "Default Brown" : {
        "name": "Default Brown",
        "side_background": "#c9c9c9",
        "side_color": "#776e65",
        "main_background": "#313131",
        "main_color": "#f9f6f2",
        "grid_background": "#bbada0",
        "button_background": "#bbada0",
        "button_color": "#f9f6f2",
        "cell_backgrounds": ("#cdc1b4", "#eee4da", "#ede0c8", "#f2b179",
                             "#f59563", "#f67c5f", "#f65e3b", "#edcf72",
                             "#edcc61", "#edc850", "#edc53f", "#edc22e"),
        "cell_colors": ("#776e65", "#776e65", "#776e65", "#f9f6f2",
                        "#f9f6f2", "#f9f6f2", "#f9f6f2", "#f9f6f2",
                        "#f9f6f2", "#f9f6f2", "#f9f6f2", "#f9f6f2")
    },

    "Sci-fi Purple" : {
        "name": "Sci-fi Purple",
        "side_background": "#c9c9c9",
        "side_color": "#776e65",
        "main_background": "#313131",
        "main_color": "#f9f6f2",
        "grid_background": "#bbada0",
        "button_background": "#bbada0",
        "button_color": "#f9f6f2",
        "cell_backgrounds": ("#cdc1b4", "#eee4da", "#ede0c8", "#f2b179",
                             "#f59563", "#f67c5f", "#f65e3b", "#edcf72",
                             "#edcc61", "#edc850", "#edc53f", "#edc22e"),
        "cell_colors": ("#776e65", "#776e65", "#776e65", "#f9f6f2",
                        "#f9f6f2", "#f9f6f2", "#f9f6f2", "#f9f6f2",
                        "#f9f6f2", "#f9f6f2", "#f9f6f2", "#f9f6f2")
    }
}
