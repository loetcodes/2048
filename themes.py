#!/usr/bin/env python3
#--------------------------------------------------------------------
#
# Version: 1.0.0
# Date: 28-07-2020
# Author: loet
# MIT License
# Copyright (c) 2020 Louisa
#
#--------------------------------------------------------------------

""" Creates Themes used in the game. Consists of a Theme class used to
define a single theme, and functions used to create one single theme
or a dictionary of multiple themes.
"""

class Theme:
    """ Creates a single theme defining the colors used by the GUI.
    """
    def __init__(self):
        self.name = "Default"
        self.main_panel_colors = ("#313131", "#f9f6f2")
        self.side_panel_colors = ("#282828", "#C4C4C4")
        self.button_colors = ("#cdc1b4", "#776e65")
        self.grid_background = "#bbada0"
        self.cell_backgrounds = ("#cdc1b4", "#eee4da", "#ede0c8", "#f2b179",
                                 "#f59563", "#f67c5f", "#f65e3b", "#edcf72",
                                 "#edcc61", "#edc850", "#edc53f", "#edc22e")
        self.cell_text_colors = ("#776e65", "#776e65", "#776e65", "#f9f6f2",
                                 "#f9f6f2", "#f9f6f2", "#f9f6f2", "#f9f6f2",
                                 "#f9f6f2", "#f9f6f2", "#f9f6f2", "#f9f6f2")
        self.cell_colors = {}

    def init_cell_colors(self):
        """ Initializes the grid cell background and text colors.
        Returns a cell_colors dictionary with pair colors set
        (background, text).
        """
        for index, color in enumerate(self.cell_backgrounds):
            key = 2 ** index
            if index == 0:
                key = 0
            try:
                text_color = self.cell_text_colors[index]
            except IndexError:
                text_color = self.cell_text_colors[-1]
            self.cell_colors[key] = (color, text_color)
        self.cell_colors["default"] = (self.cell_backgrounds[-1],
                                       self.cell_text_colors[-1])
        return self.cell_colors

    def get_theme(self):
        """ Gets the name of a theme.
        """
        return self.name

    def get_cell_color(self, key):
        """ Gets the cell background color and text color.
        Returns a tuple if the key exists, otherwise returns the default colors
        """
        default_val = self.cell_colors.get("default")
        return self.cell_colors.get(key, default_val)


def create_theme(theme_name, styles):
    """ Creates a new theme from a theme_class. Overrides styles identified
    in the styles dictionary. Returns a new theme.
    """
    # creates the theme class
    new_theme = Theme()
    new_theme.name = theme_name

    # Override properties with those in styles
    for key, values in styles.items():
        try:
            curr_attr = new_theme.__getattribute__(key)
            if curr_attr:
                new_theme.__setattr__(key, values)
        except AttributeError as error:
            print(error)

    # Initialize the colors and return the theme
    new_theme.init_cell_colors()
    return new_theme


def create_all_themes(additional_themes=None):
    """ Creates themes that include a default theme and any additional
    themes from the given dictionary.
    Returns themes
    """
    all_themes = {}

    # Create the default theme
    default = Theme()
    default.init_cell_colors()
    all_themes[default.name] = default

    if additional_themes:
        # Create and add any additional themes
        for name, values in additional_themes.items():
            curr_theme = create_theme(name, values)
            all_themes[curr_theme.name] = curr_theme
    return all_themes


def main(themes_dict):
    """ Creates themes and prints the theme dictionary.
    Returns None.
    """
    # Create themes
    game_themes = create_all_themes(themes_dict)
    print("Game themes are now:", game_themes)


if __name__ == "__main__":
    from constants import ADDITIONAL_THEMES
    main(ADDITIONAL_THEMES)
