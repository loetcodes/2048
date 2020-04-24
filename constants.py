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

# Direction values
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Direction dictionary
DIRECTIONS = {
    "Up" : UP,
    "Down" : DOWN,
    "Left" : LEFT,
    "Right" : RIGHT
}

# Offsets for computing direction indices
OFFSETS = {
    UP : (1, 0),
    DOWN : (-1, 0),
    LEFT : (0, 1),
    RIGHT : (0, -1)
}

# Font
FONT = ("Verdana", 32, "bold")
TITLE_FONT = ("Verdana", 40, "bold")
TEXT_FONT = ("Verdana", 16, "bold")
SCORE_FONT = ("Verdana", 18, "bold")
BUTTON_FONT = ("Verdana", 14, "bold")


# Default Brown theme
DEFAULT_THEME = {
    'side_background': "#c9c9c9",
    'side_color' : "#776e65",
    'main_background': "#313131",
    'main_color': "#f9f6f2",
    'grid_background': "#bbada0",
    'button_background': "#bbada0", 
    'button_color': "#f9f6f2",
    'cell_background': {
        0: "#cdc1b4",
        2: "#eee4da",
        4: "#ede0c8",
        8: "#f2b179",
        16: "#f59563",
        32: "#f67c5f",
        64: "#f65e3b",
        128: "#edcf72",
        256: "#edcc61",
        512: "#edc850",
        1024: "#edc53f",
        2048: "#edc22e"
    },
    'cell_color' : {
        0: "#776e65",
        2: "#776e65",
        4: "#776e65",
        8: "#f9f6f2",
        16: "#f9f6f2",
        32: "#f9f6f2",
        64: "#f9f6f2",
        128: "#f9f6f2",
        256: "#f9f6f2",
        512: "#f9f6f2",
        1024: "#f9f6f2",
        2048: "#f9f6f2"
    }
}












# Dark theme - Purple-blue
DARK_THEME = {
    'grid_background' : "",
    'empty_cell_background': "",
    'occupied_cell_background' : {
        2: "",
        4: "",
        8: "",
        16: "",
        32: "",
        64: "",
        128: "",
        256: "",
        512: "",
        1024: "",
        2048: ""
    },
    'occupied_cell_color' : {
        2: "",
        4: "",
        8: "",
        16: "",
        32: "",
        64: "",
        128: "",
        256: "",
        512: "",
        1024: "",
        2048: ""
    }
}

# Redish them - Red yellow
REDISH_THEME = {
    'grid_background' : "",
    'empty_cell_background': "",
    'occupied_cell_background' : {
        2: "",
        4: "",
        8: "",
        16: "",
        32: "",
        64: "",
        128: "",
        256: "",
        512: "",
        1024: "",
        2048: ""
    },
    'occupied_cell_color' : {
        2: "",
        4: "",
        8: "",
        16: "",
        32: "",
        64: "",
        128: "",
        256: "",
        512: "",
        1024: "",
        2048: ""
    }
}
