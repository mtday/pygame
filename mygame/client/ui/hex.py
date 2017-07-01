import math
import pygame
import pygame.gfxdraw


class Hex:
    precomputed_rads = [(math.pi / 180) * (60 * i + 30) for i in range(0, 6)]
    precomputed_cos = [math.cos(rad) for rad in precomputed_rads]
    precomputed_sin = [math.sin(rad) for rad in precomputed_rads]

    @staticmethod
    def draw_circle(surface, center, radius, color):
        pygame.gfxdraw.aacircle(surface, int(center[0]), int(center[1]), int(radius), color)

    @staticmethod
    def draw_hex(surface, center, radius, color):
        corner_points = [Hex.get_point(center, radius, i) for i in range(0, 6)]
        pygame.draw.aalines(surface, color, True, corner_points)

    @staticmethod
    def get_point(center, radius, i):
        center_x, center_y = center
        return (center_x + radius * Hex.precomputed_cos[i],
                center_y + radius * Hex.precomputed_sin[i])
