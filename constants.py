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

# Additional themes are defined and added here.
ADDITIONAL_THEMES = {
    "Sunset" : {
        "name": "Sunset",
        "button_colors": ("#414141", "#f9f6f2"),
        "grid_background": "#282828",
        "cell_backgrounds": ("#414141", "#FE957E", "#FF9153", "#DD1313",
                             "#AE0000", "#FE640E", "#AA5D02", "#AD9C00",
                             "#7B6F00", "#E12043", "#B90F1A", "#EDC22E"),
        "cell_text_colors": ("#F8F8F8", "#F8F8F8", "#F8F8F8", "#F8F8F8",
                             "#F8F8F8", "#F8F8F8", "#F8F8F8", "#F8F8F8",
                             "#F8F8F8", "#F8F8F8", "#F8F8F8", "#F8F8F8")
    },

    "Sci-fi" : {
        "name": "Sci-fi",
        "main_panel_colors": ("#313131", "#f9f6f2"),
        "side_panel_colors": ("#282828", "#C4C4C4"),
        "grid_background": "#29132E",
        "cell_backgrounds": ("#321450", "#BF01AC", "#780196", "#7A3DFF",
                             "#4000CA", "#02BCBC", "#077B7B", "#D80369",
                             "#9D004B", "#CB9E00", "#937200", "#14A73D"),
        "cell_text_colors": ("#F8F8F8", "#F8F8F8", "#F8F8F8", "#F8F8F8",
                             "#F8F8F8", "#F8F8F8", "#F8F8F8", "#F8F8F8",
                             "#F8F8F8", "#F8F8F8", "#F8F8F8", "#F8F8F8")
    }
}
