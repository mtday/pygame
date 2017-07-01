import math

from mygame.config.colors import GREEN
from mygame.config.colors import HEX_GRID_LINE_COLOR
from mygame.config.colors import RED
from mygame.config.colors import YELLOW
from mygame.config.settings import DEFAULT_HEX_RADIUS
from mygame.config.settings import DEFAULT_ZOOM
from mygame.model.coord import Coord
from mygame.model.hex import Hex


class HexGrid:
    precomputed_sqrt3 = math.sqrt(3)
    precomputed_sqrt3div2 = precomputed_sqrt3 / 2

    def __init__(self, surface):
        self.surface = surface
        self.zoom = DEFAULT_ZOOM
        self.hex_radius = DEFAULT_HEX_RADIUS
        self.hex_height = self.hex_radius * 2
        self.hex_vertical_increase = self.hex_height * 3 / 4
        self.hex_width = HexGrid.precomputed_sqrt3div2 * self.hex_height
        self.hex_width_half = self.hex_width / 2
        self.coord_offset_x = 0
        self.coord_offset_y = 0
        self.center_coord = Coord()
        self.hoover_coord = Coord()

    def set_mouse_position(self, position):
        position_x, position_y = position
        # Update the given positions based on the concept of 0, 0 being in the middle.
        mouse_x = position_x - self.surface.get_width() / 2 - self.coord_offset_x
        mouse_y = position_y - self.surface.get_height() / 2 - self.coord_offset_y
        # Determine the coordinate associated with the current mouse position.
        coord_x = (mouse_x * HexGrid.precomputed_sqrt3 / 3 - mouse_y / 3) / self.hex_radius
        coord_z = mouse_y * 2 / 3 / self.hex_radius
        self.hoover_coord = Coord(coord_x, -coord_x - coord_z, coord_z).add_coord(self.center_coord)

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

    def draw(self):
        self.__draw_grid()
        self.__draw_center()
        self.__draw_origin()
        self.__draw_hoover()

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

    def __draw_hoover(self):
        if self.hoover_coord:
            self.__draw_coord(self.hoover_coord, RED)

    def __draw_origin(self):
        self.__draw_coord(Coord(), GREEN)

    def __draw_coord(self, coord, color):
        offset = coord.subtract_coord(self.center_coord)
        # delta_x = coord.x - self.center_coord.x
        # delta_z = coord.z - self.center_coord.z
        # coord_x = self.hex_radius * HexGrid.precomputed_sqrt3 * (delta_x + delta_z / 2)
        # coord_y = self.hex_radius * 3 / 2 * delta_z
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
