
import math
import pygame
import pygame.gfxdraw

from mygame.client.config.colors import SELECTED_UNIT_OUTLINE_COLOR
from mygame.client.config.colors import UNIT_RECON_DRONE_OUTLINE_COLOR
from mygame.common.model.unit import Unit


class ReconDrone(Unit):
    TYPE = 'RECON_DRONE'

    precomputed_rads = [(math.pi / 180) * (120 * i + 30) for i in range(0, 3)]
    precomputed_cos = [math.cos(rad) for rad in precomputed_rads]
    precomputed_sin = [math.sin(rad) for rad in precomputed_rads]

    def __init__(self, unit_id, coord):
        super(ReconDrone, self).__init__(ReconDrone.TYPE, unit_id, coord)

    def draw(self, hexgrid):
        center = hexgrid.get_center_position(self.coord)
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
    def read(iostream, unit_type, unit_id, coord):
        return ReconDrone(unit_id, coord)

    @staticmethod
    def write(iostream, unit):
        pass
