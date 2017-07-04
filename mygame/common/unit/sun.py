import pygame
import pygame.gfxdraw

from mygame.client.config.colors import SELECTED_UNIT_OUTLINE_COLOR
from mygame.client.config.colors import UNIT_SUN_FILL_COLOR
from mygame.client.config.colors import UNIT_SUN_OUTLINE_COLOR
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.model.unit import Unit
from mygame.common.model.unitinfo import UnitInfo


class Sun(Unit):
    TYPE = 'SUN'
    VERSION = 1

    def __init__(self, unit_info):
        super(Sun, self).__init__(Sun.TYPE, unit_info)
        self.movable = False

    def get_actions(self, clicked_coord, clicked_unit):
        # The sun has no actions that it performs.
        return []

    def draw(self, hexgrid):
        center = hexgrid.get_center_position(self.unit_info.coord)
        pygame.gfxdraw.filled_circle(hexgrid.surface, center[0], center[1],
                                     int(hexgrid.hex_width * 1.5), UNIT_SUN_FILL_COLOR)
        pygame.gfxdraw.aacircle(hexgrid.surface, center[0], center[1],
                                int(hexgrid.hex_width * 1.5), UNIT_SUN_OUTLINE_COLOR)

        if self.selected:
            pygame.gfxdraw.aacircle(hexgrid.surface, center[0], center[1],
                                    int(hexgrid.hex_width * 2), SELECTED_UNIT_OUTLINE_COLOR)

    @staticmethod
    def read(iostream):
        version = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        if version == 1:
            unit_info = UnitInfo.read(iostream)
            return Sun(unit_info)
        else:
            raise Exception(f'Unsupported serialization version: {version}')

    def write(self, iostream):
        iostream.write(Sun.VERSION.to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        self.unit_info.write(iostream)
