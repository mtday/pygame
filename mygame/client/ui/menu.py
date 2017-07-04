import pygame
import pygame.gfxdraw

from mygame.client.config.colors import MENU_SELECTION_COLOR


class Menu:
    def __init__(self, hexgrid):
        self.hexgrid = hexgrid
        self.actions = None
        self.position = None
        self.visible = False

    def display_actions(self, actions, position):
        if len(actions) > 0 and position:
            self.actions = {}
            self.position = position
            for action in actions:
                if action.name in self.actions:
                    # Add the action to the list
                    self.actions[action.name] += action
                else:
                    self.actions[action.name] = [action]
            self.visible = True

    def clear_actions(self):
        self.actions = None
        self.position = None
        self.visible = False

    def draw(self):
        if self.visible:
            pygame.gfxdraw.aacircle(self.hexgrid.surface, self.position[0], self.position[1],
                                    int(self.hexgrid.hex_width_half), MENU_SELECTION_COLOR)
