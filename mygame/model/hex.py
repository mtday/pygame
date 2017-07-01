import math
import pygame

from mygame.config.colors import BLACK
from mygame.config.colors import YELLOW
from mygame.config.settings import DEFAULT_FONT_NAME
from pygame import gfxdraw


class Hex:
    precomputed_rads = [(math.pi / 180) * (60 * i + 30) for i in range(0, 6)]
    precomputed_cos = [math.cos(rad) for rad in precomputed_rads]
    precomputed_sin = [math.sin(rad) for rad in precomputed_rads]

    @staticmethod
    def draw_circle(surface, center, radius, color, coord=None):
        pygame.gfxdraw.aacircle(surface, int(center[0]), int(center[1]), int(radius), color)
        # int_center = (int(center[0]), int(center[1]))
        # pygame.draw.circle(surface, color, int_center, radius, 1)

        if coord:
            font = pygame.font.SysFont(DEFAULT_FONT_NAME, 15)
            x_label = coord.x if coord.x != 0 else "x"
            y_label = coord.y if coord.y != 0 else "y"
            z_label = coord.z if coord.z != 0 else "z"
            x_corner = Hex.get_point(center, radius, 5)
            y_corner = Hex.get_point(center, radius, 3)
            z_corner = Hex.get_point(center, radius, 1)
            x_pos = (x_corner[0] - 7, x_corner[1] - 0)
            y_pos = (y_corner[0] + 4, y_corner[1] - 0)
            z_pos = (z_corner[0] - 2, z_corner[1] - 12)
            surface.blit(font.render(f'{x_label}', True, YELLOW, BLACK), x_pos)
            surface.blit(font.render(f'{y_label}', True, YELLOW, BLACK), y_pos)
            surface.blit(font.render(f'{z_label}', True, YELLOW, BLACK), z_pos)

    @staticmethod
    def draw_hex(surface, center, radius, color, coord=None):
        corner_points = [Hex.get_point(center, radius, i) for i in range(0, 6)]
        pygame.draw.aalines(surface, color, True, corner_points)

        if coord:
            font = pygame.font.SysFont(DEFAULT_FONT_NAME, 15)
            x_label = coord.x if coord.x != 0 else "x"
            y_label = coord.y if coord.y != 0 else "y"
            z_label = coord.z if coord.z != 0 else "z"
            x_pos = (corner_points[5][0] - 7, corner_points[5][1] - 0)
            y_pos = (corner_points[3][0] + 4, corner_points[3][1] - 0)
            z_pos = (corner_points[1][0] - 2, corner_points[1][1] - 12)
            surface.blit(font.render(f'{x_label}', True, YELLOW, BLACK), x_pos)
            surface.blit(font.render(f'{y_label}', True, YELLOW, BLACK), y_pos)
            surface.blit(font.render(f'{z_label}', True, YELLOW, BLACK), z_pos)

    @staticmethod
    def get_point(center, radius, i):
        center_x, center_y = center
        return (center_x + radius * Hex.precomputed_cos[i],
                center_y + radius * Hex.precomputed_sin[i])
