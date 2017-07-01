
import pygame
import pygame.gfxdraw

from mygame.client.config.colors import YELLOW
from mygame.common.model.unit import Unit


class Sun(Unit):
    TYPE = "SUN"

    def __init__(self, coord):
        Unit.__init__(self, Sun.TYPE, coord)

    def draw(self, hexgrid):
        center = hexgrid.get_center_position(self.coord)
        pygame.gfxdraw.aacircle(hexgrid.surface, center[0], center[1], int(hexgrid.hex_width_half), YELLOW)
        pygame.gfxdraw.filled_circle(hexgrid.surface, center[0], center[1], int(hexgrid.hex_width_half), YELLOW)
        pass
