
import pygame
import pygame.gfxdraw

from mygame.client.config.colors import UNIT_SUN_FILL_COLOR
from mygame.client.config.colors import UNIT_SUN_OUTLINE_COLOR
from mygame.common.model.unit import Unit


class Sun(Unit):
    TYPE = "SUN"

    def __init__(self, unit_id, coord):
        Unit.__init__(self, Sun.TYPE, unit_id, coord)

    def draw(self, hexgrid):
        center = hexgrid.get_center_position(self.coord)
        pygame.gfxdraw.filled_circle(hexgrid.surface, center[0], center[1],
                                     int(hexgrid.hex_width_half), UNIT_SUN_OUTLINE_COLOR)
        pygame.gfxdraw.aacircle(hexgrid.surface, center[0], center[1],
                                int(hexgrid.hex_width_half), UNIT_SUN_FILL_COLOR)
