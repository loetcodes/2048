#!/usr/bin/env python3
#--------------------------------------------------------------------
#
# Version: 1.0.0
# Date: 17-04-2020
# Author: loet
# MIT License
# Copyright (c) 2020 Louisa
#
#--------------------------------------------------------------------

"""
2048 Game GUI.
"""

import tkinter as tk
import constants
from game import TwentyFortyEight

class GameTheme:
    """ Class that creates themes used by the GUI
    """
    def __init__(self, theme_dict):
        self.name = theme_dict["name"]
        self.grid_background = theme_dict["grid_background"]
        self.side_panel_colors = (theme_dict["side_background"],
                                  theme_dict["side_color"])
        self.main_panel_colors = (theme_dict["main_background"],
                                  theme_dict["main_color"])
        self.button_colors = (theme_dict["button_background"],
                              theme_dict["button_color"])
        self.cell_colors = self.init_colors(theme_dict["cell_backgrounds"],
                                            theme_dict["cell_colors"])

    @staticmethod
    def init_colors(background_colors, text_colors):
        """ Initializes the grid cell background and text colors.
        Returns a dictionary with pair colors set (background, text).
        """
        cell_colors = {}
        for index, color in enumerate(background_colors):
            key = 2 ** index
            if index == 0:
                key = 0
            try:
                text_color = text_colors[index]
            except IndexError:
                text_color = text_colors[-1]
            cell_colors[key] = (color, text_color)
        cell_colors["default"] = (background_colors[-1], text_colors[-1])
        return cell_colors

    def get_theme(self):
        """ Gets the name of a theme
        """
        return self.name

    def get_cell_colors(self, key):
        """ Gets the cell background color and text color.
        Returns a tuple if the key exists, otherwise returns the default colors
        """
        default_val = self.cell_colors.get("default")
        return self.cell_colors.get(key, default_val)


class GameGui(tk.Frame):
    """ Class that runs the game GUI.
    """
    def __init__(self, game, dimensions, theme, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.game = game
        self.dimensions = dimensions
        self.theme = theme
        self.grid_cells = []
        self.score = None
        self.final_result = None
        self.aspect_ratio = 1.0
        self.bind_direction_keys()
        self.panel_width = self.get_side_panel_width()
        self.init_panels()
        self.init_side_content()
        self.grid_widget = self.init_grid_widget()
        self.init_grid_cells()
        self.constrain_content(self.grid_widget, self.main_container, self.aspect_ratio)
        self.mainloop()

    def init_panels(self):
        """ Initializes window panels of given width and window height
        Returns a Frame.
        """
        # Main container and left side panel
        main_panel_colors = self.theme.main_panel_colors
        side_panel_colors = self.theme.side_panel_colors
        self.main_container = tk.Frame(bg=main_panel_colors[0],
                                       width=self.dimensions["height"])
        self.main_container.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.RIGHT)
        if self.panel_width >= constants.MIN_SIDE_PANEL:
            self.side_panel = tk.Frame(bg=side_panel_colors[0], width=self.panel_width)
            self.side_panel.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)

    def init_side_content(self):
        """ Initializes side panel content, i.e the title, instructions, score and new game
        button if the side panel is of atleast minimum width.
        """
        if self.panel_width >= constants.MIN_SIDE_PANEL:
            self.init_text()
            self.init_score()
            self.display_result()
            self.new_game_button()

    def init_text(self):
        """ Initializes the side panel with the Game title and instructions.
        """
        # Add the title label and instructions.
        title_style = constants.TITLE_FONT
        info_style = constants.TEXT_FONT
        title_width = self.panel_width // 6
        cell_colors = self.theme.get_cell_colors(2048)
        title = tk.Label(master=self.side_panel, text=constants.GAME_TITLE,
                         bg=cell_colors[0], fg=cell_colors[1],
                         justify=tk.CENTER, font=title_style,
                         padx=title_width, pady=title_width//2)
        title.pack()
        info_text = constants.INSTRUCTIONS
        side_panel_colors = self.theme.side_panel_colors
        info = tk.Label(master=self.side_panel, text=info_text,
                        bg=side_panel_colors[0], fg=side_panel_colors[1],
                        justify=tk.CENTER, font=info_style, padx=20, pady=title_width)
        info.pack()

    def init_score(self):
        """ Initializes the side panel with the Game score content.
        """
        # Add Score title and value to the panel
        score_style = constants.SCORE_FONT
        score_width = self.panel_width // 10
        side_panel_colors = self.theme.side_panel_colors
        score_name = tk.Label(master=self.side_panel, text=constants.SCORE_TITLE,
                              bg=side_panel_colors[0], fg=side_panel_colors[1],
                              justify=tk.CENTER, font=score_style,
                              padx=score_width, pady=score_width//2)
        score_name.pack()
        score_value = str(self.game.get_score())
        self.score = tk.Label(master=self.side_panel, text=score_value,
                              bg=side_panel_colors[0], fg=side_panel_colors[1],
                              justify=tk.CENTER, font=score_style)
        self.score.pack()

    def new_game_button(self):
        """ Button that starts a new game.
        """
        button_width = self.panel_width // 10
        button_style = constants.BUTTON_FONT
        button_colors = self.theme.button_colors
        button_name = tk.Label(master=self.side_panel, text=constants.NEW_GAME_TITLE,
                               bg=button_colors[0], fg=button_colors[1],
                               justify=tk.CENTER, font=button_style,
                               padx=button_width, pady=button_width//2)
        button_name.pack(pady=button_width)
        button_name.bind('<Button-1>', self.new_game)

    def display_result(self):
        """ Displays the final result of the current game.
        Whether they won or lost.
        """
        result_value = self.game.get_final_result()
        result_width = self.panel_width // 10
        result_style = constants.SCORE_FONT
        side_panel_colors = self.theme.side_panel_colors
        self.final_result = tk.Label(master=self.side_panel, text=result_value,
                                     bg=side_panel_colors[0], fg=side_panel_colors[1],
                                     justify=tk.CENTER, font=result_style,
                                     padx=result_width, pady=result_width//2)
        self.final_result.pack(pady=result_width//2)

    def key_down(self, event):
        """ Keydown event handler for directions
        """
        direction_name = event.keysym
        if direction_name in constants.DIRECTIONS.keys():
            # Move tiles based on directions, then update display
            value = constants.DIRECTIONS[direction_name]
            self.game.move(value)

        # Check if any more valid moves, if not, end game, display result.
        if self.game.no_valid_moves():
            self.game.set_final_result()
        self.update_gui()

    def bind_direction_keys(self):
        """ Bind main key directions to events.
        """
        for name in constants.DIRECTIONS:
            direction = "<" + name + ">"
            self.master.bind(direction, self.key_down)

    def get_side_panel_width(self):
        """ Gets the side panel width.
        Returns the panel width.
        """
        panel_width = self.dimensions["width"] - self.dimensions["height"]
        if panel_width >= 50:
            return panel_width
        return 0

    def init_grid_widget(self):
        """ Initializes a grid widget frame.
        Returns a Frame.
        """
        # Creates a grid container frame and places in center.
        inner_height = self.dimensions["height"] - self.dimensions["outer_padding"]
        grid_container = tk.Frame(master=self.main_container, bg=self.theme.grid_background)
        grid_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER,
                             width=inner_height, height=inner_height)
        return grid_container

    def init_grid_cells(self):
        """ Initializes the grid cells that hold game display values.
        Sets the grid_cell matrix.
        """
        grid_size = self.dimensions["grid_size"]
        inner_height = self.dimensions["height"] - self.dimensions["outer_padding"]
        padding = self.dimensions["inner_padding"]
        cell_width = (inner_height - padding * 2) // grid_size
        for i in range(grid_size):
            grid_row = []
            self.grid_widget.rowconfigure(i, weight=1)
            self.grid_widget.columnconfigure(i, weight=1)
            for j in range(grid_size):
                # Get tile value
                num = self.game.get_tile(i, j)
                num_txt = str(num) if num else ""
                # Set cell value, colors and label, append to grid cells.
                colors = self.theme.get_cell_colors(num)
                cell = tk.Frame(master=self.grid_widget, bg=colors[0])
                cell.grid(row=i, column=j, padx=padding, pady=padding)
                content = tk.Label(master=cell, text=num_txt,
                                   bg=colors[0], fg=colors[1],
                                   justify=tk.CENTER, font=constants.FONT,
                                   width=cell_width, height=cell_width)
                content.pack()
                grid_row.append(content)
            self.grid_cells.append(grid_row)

    def constrain_content(self, content_frame, padding_frame, aspect_ratio):
        """ Constrains a content panel within a padding panel based on an
        aspect ratio and a resize event.
        """
        outer_padding = self.dimensions["outer_padding"]
        def set_aspect(event):
            """ Resizes the content frame to fit either the width of height
            based on the aspect ratio.
            """
            # Get current widths, check new heights and widths, place window
            desired_width = event.width - outer_padding
            desired_height = int(desired_width / aspect_ratio)
            if desired_height > event.height:
                desired_height = event.height - outer_padding
                desired_width = int(desired_height * aspect_ratio)
            content_frame.place(in_=padding_frame, relx=0.5, rely=0.5,
                                anchor=tk.CENTER, width=desired_width, height=desired_height)
        padding_frame.bind("<Configure>", set_aspect)

    def update_gui(self):
        """ Updates the gui grid cells with new values from the game and new score.
        """
        # Update grid cells
        total_rows = self.game.get_grid_height()
        total_cols = self.game.get_grid_width()
        for row in range(total_rows):
            for col in range(total_cols):
                # Get new tile
                curr_cell = self.grid_cells[row][col]
                tile = self.game.get_tile(row, col)
                tile_txt = str(tile) if tile != 0 else ""

                # Tiles past the max 2048 receive the default colors
                tile_colors = self.theme.get_cell_colors(tile)

                # Set new background and label
                curr_cell.configure(text=tile_txt, bg=tile_colors[0],
                                    fg=tile_colors[1])
        # Update score, game message and pending tasks
        try:
            new_score = str(self.game.get_score())
            self.score.configure(text=new_score)
            result = self.game.get_final_result()
            self.final_result.configure(text=result)
        except AttributeError:
            pass
        self.update_idletasks()

    def new_game(self, event):
        """ Starts a new game on the gui.
        """
        event.widget.focus_set()
        self.game.initialize_game()
        self.update_gui()


class Window:
    """ Class controls the window
    """
    def __init__(self, title, game_constants):
        self.root = tk.Tk()
        self.title = title
        self.grid_dimensions = self.init_dimensions(game_constants)
        self.themes = self.init_themes(game_constants.GAME_THEMES)
        self.set_main_theme("Default Brown")
        self.init_window()

    @staticmethod
    def init_dimensions(game_constants):
        """ Initializes a dictionary with the basic window and game dimensions.
        Returns a dictionary
        """
        dimensions = {
            "width" : game_constants.WIDTH,
            "height" : game_constants.HEIGHT,
            "inner_padding" : game_constants.GRID_PADDING,
            "outer_padding" : game_constants.GRID_PADDING * 4,
            "grid_size" : game_constants.GRID_SIZE
        }
        return dimensions

    @staticmethod
    def init_themes(themes_list):
        """ Initializes the themes dictionary with all the themes.
        Sets the main theme on start up
        """
        themes = {}
        for key, values in themes_list.items():
            themes[key] = GameTheme(values)
        return themes

    def set_main_theme(self, theme_name):
        """ Sets the main theme in use.
        """
        self.main_theme = self.themes.get(theme_name)

    def init_window(self):
        """ Initialize the window values
        """
        pass

    def run_gui(self):
        """ Instantiates the window, and runs the main game gui
        """
        grid_size = self.grid_dimensions["grid_size"]
        new_game = TwentyFortyEight(grid_size, grid_size)
        app = GameGui(new_game, self.grid_dimensions, self.main_theme, self.root)
        app.mainloop()


if __name__ == "__main__":
    Window('2048 game', constants).run_gui()
