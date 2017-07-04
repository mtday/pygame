import math
import pygame
import pygame.gfxdraw

from mygame.client.config.colors import SELECTED_UNIT_OUTLINE_COLOR
from mygame.client.config.colors import UNIT_RECON_DRONE_OUTLINE_COLOR
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.model.unit import Unit
from mygame.common.model.unitinfo import UnitInfo


class ReconDrone(Unit):
    TYPE = 'RECON_DRONE'
    VERSION = 1

    precomputed_rads = [(math.pi / 180) * (120 * i + 30) for i in range(0, 3)]
    precomputed_cos = [math.cos(rad) for rad in precomputed_rads]
    precomputed_sin = [math.sin(rad) for rad in precomputed_rads]

    def __init__(self, unit_info):
        super(ReconDrone, self).__init__(ReconDrone.TYPE, unit_info)

    def draw(self, hexgrid):
        center = hexgrid.get_center_position(self.unit_info.coord)
        corner_points = [ReconDrone.get_point(center, hexgrid.hex_width_half, i) for i in range(0, 3)]
        pygame.draw.aalines(hexgrid.surface, UNIT_RECON_DRONE_OUTLINE_COLOR, True, corner_points)

        if self.selected:
            pygame.gfxdraw.aacircle(hexgrid.surface, center[0], center[1],
                                    int(hexgrid.hex_width_half * 1.4), SELECTED_UNIT_OUTLINE_COLOR)

    @staticmethod
    def get_point(center, radius, i):
        center_x, center_y = center
        return (center_x + radius * ReconDrone.precomputed_cos[i],
                center_y + radius * ReconDrone.precomputed_sin[i])

    @staticmethod
    def read(iostream):
        version = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        if version == 1:
            unit_info = UnitInfo.read(iostream)
            return ReconDrone(unit_info)
        else:
            raise Exception(f'Unsupported serialization version: {version}')

    def write(self, iostream):
        iostream.write(ReconDrone.VERSION.to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        self.unit_info.write(iostream)
