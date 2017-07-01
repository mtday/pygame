import math
import pygame

from mygame.config.colors import BLACK
from mygame.config.colors import GREEN
from mygame.config.colors import HEX_GRID_LINE_COLOR
from mygame.config.colors import RED
from mygame.config.colors import YELLOW
from mygame.config.settings import FONT_NAME_DEFAULT
from mygame.config.settings import HEX_RADIUS_DEFAULT
from mygame.config.settings import HEX_RADIUS_MIN
from mygame.config.settings import HEX_RADIUS_MAX
from mygame.model.coord import Coord
from mygame.model.hex import Hex


class HexGrid:
    precomputed_sqrt3 = math.sqrt(3)
    precomputed_sqrt3div2 = precomputed_sqrt3 / 2

    def __init__(self, surface):
        self.surface = surface

        self.hex_radius = HEX_RADIUS_DEFAULT
        self.hex_height = None
        self.hex_vertical_increase = None
        self.hex_width = None
        self.hex_width_half = None
        self.__set_size_vars()

        self.coord_offset_x = 0
        self.coord_offset_y = 0
        self.center_coord = Coord()
        self.hover_coord = Coord()

        self.last_mouse_position = None

    def set_mouse_position(self, position):
        # Save the position so we can fix the hover coordinate after zoom changes.
        self.last_mouse_position = position
        position_x, position_y = position
        # Update the given positions based on the concept of 0, 0 being in the middle.
        mouse_x = position_x - self.surface.get_width() / 2 - self.coord_offset_x
        mouse_y = position_y - self.surface.get_height() / 2 - self.coord_offset_y
        # Determine the coordinate associated with the current mouse position.
        coord_x = (mouse_x * HexGrid.precomputed_sqrt3 / 3 - mouse_y / 3) / self.hex_radius
        coord_z = mouse_y * 2 / 3 / self.hex_radius
        self.hover_coord = Coord(coord_x, -coord_x - coord_z, coord_z).add_coord(self.center_coord)

    def drag_grid(self, offset):
        self.coord_offset_x = self.coord_offset_x - offset[0]
        self.coord_offset_y = self.coord_offset_y - offset[1]
        if abs(self.coord_offset_x) > self.hex_width:
            delta = int(self.coord_offset_x / self.hex_width)
            self.coord_offset_x = self.coord_offset_x - delta * self.hex_width
            self.center_coord = self.center_coord.add(-delta, delta, 0)
        height_delta = self.hex_height * 3 / 2
        if abs(self.coord_offset_y) > height_delta:
            delta = int(self.coord_offset_y / height_delta)
            self.coord_offset_y = self.coord_offset_y - delta * height_delta
            self.center_coord = self.center_coord.add(delta, delta, -2 * delta)

    def zoom_in(self):
        if self.hex_radius < HEX_RADIUS_MAX:
            delta = 4 if self.hex_radius >= HEX_RADIUS_DEFAULT else 2
            self.hex_radius = self.hex_radius + delta
            self.__set_size_vars()
            if self.last_mouse_position:
                self.set_mouse_position(self.last_mouse_position)

    def zoom_out(self):
        if self.hex_radius > HEX_RADIUS_MIN:
            delta = 2 if self.hex_radius <= HEX_RADIUS_DEFAULT else 4
            self.hex_radius = self.hex_radius - delta
            self.__set_size_vars()
            if self.last_mouse_position:
                self.set_mouse_position(self.last_mouse_position)

    def __set_size_vars(self):
        self.hex_height = self.hex_radius * 2
        self.hex_vertical_increase = self.hex_height * 3 / 4
        self.hex_width = HexGrid.precomputed_sqrt3div2 * self.hex_height
        self.hex_width_half = self.hex_width / 2

    def draw(self):
        self.__draw_grid()
        self.__draw_center()
        self.__draw_origin()
        self.__draw_hover()

        font = pygame.font.SysFont(FONT_NAME_DEFAULT, 15)
        self.surface.blit(font.render(f'{self.hex_radius}', True, YELLOW, BLACK), (10, 10))

    def __draw_grid(self):
        top_left = self.__get_top_left_coord_center()
        rows = int(self.surface.get_height() / self.hex_vertical_increase) + 1
        cols = int(self.surface.get_width() / self.hex_width) + 1
        for r in range(0, rows):
            for c in range(0, cols):
                hex_offset = int((r % 2) * self.hex_width_half)
                center = (top_left[0] + c * self.hex_width + hex_offset, top_left[1] + r * self.hex_vertical_increase)
                Hex.draw_hex(self.surface, center, self.hex_radius, HEX_GRID_LINE_COLOR)

    def __draw_center(self):
        self.__draw_coord(self.center_coord, YELLOW)

    def __draw_hover(self):
        if self.hover_coord:
            self.__draw_coord(self.hover_coord, RED)

    def __draw_origin(self):
        self.__draw_coord(Coord(), GREEN)

    def __draw_coord(self, coord, color):
        offset = coord.subtract_coord(self.center_coord)
        coord_x = self.hex_radius * HexGrid.precomputed_sqrt3 * (offset.x + offset.z / 2)
        coord_x = coord_x + self.surface.get_width() / 2 + self.coord_offset_x
        coord_y = self.hex_radius * 3 / 2 * offset.z
        coord_y = coord_y + self.surface.get_height() / 2 + self.coord_offset_y
        Hex.draw_circle(self.surface, (coord_x, coord_y), self.hex_width_half, color, coord)

    def __get_top_left_coord_center(self):
        top_left = (self.surface.get_width() / 2 + self.coord_offset_x,
                    self.surface.get_height() / 2 + self.coord_offset_y)
        while top_left[0] >= 0 or top_left[1] >= 0:
            if top_left[0] >= 0:
                if top_left[1] >= 0:
                    top_left = (top_left[0] - self.hex_width_half, top_left[1] - self.hex_vertical_increase)
                else:
                    top_left = (top_left[0] - self.hex_width, top_left[1])
            elif top_left[1] >= 0:
                top_left = (top_left[0], top_left[1] - self.hex_height)
        return top_left
