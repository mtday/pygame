
import pygame
import pygame.gfxdraw

from mygame.client.config.colors import SELECTED_UNIT_OUTLINE_COLOR
from mygame.client.config.colors import UNIT_PLANET_FILL_COLOR
from mygame.client.config.colors import UNIT_PLANET_OUTLINE_COLOR
from mygame.common.model.unit import Unit


class Planet(Unit):
    TYPE = 'PLANET'

    def __init__(self, unit_id, coord):
        super(Planet, self).__init__(Planet.TYPE, unit_id, coord)
        self.movable = False

    def draw(self, hexgrid):
        center = hexgrid.get_center_position(self.coord)
        pygame.gfxdraw.filled_circle(hexgrid.surface, center[0], center[1],
                                     int(hexgrid.hex_width_half), UNIT_PLANET_FILL_COLOR)
        pygame.gfxdraw.aacircle(hexgrid.surface, center[0], center[1],
                                int(hexgrid.hex_width_half), UNIT_PLANET_OUTLINE_COLOR)

        if self.selected:
            pygame.gfxdraw.aacircle(hexgrid.surface, center[0], center[1],
                                    int(hexgrid.hex_width_half * 1.4), SELECTED_UNIT_OUTLINE_COLOR)

    @staticmethod
    def read(iostream, unit_type, unit_id, coord):
        return Planet(unit_id, coord)

    @staticmethod
    def write(iostream, unit):
        pass
