import math
import pygame

from mygame.client.config.settings import HEX_RADIUS_DEFAULT
from mygame.client.config.settings import HEX_RADIUS_MAX
from mygame.client.config.settings import HEX_RADIUS_MID
from mygame.client.config.settings import HEX_RADIUS_MIN
from mygame.client.ui.hex import Hex
from mygame.common.model.coord import Coord


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

        self.__coord_offset_x = 0
        self.__coord_offset_y = 0
        self.__center_coord = Coord()
        self.__hover_coord = Coord()

        self.__last_mouse_position = None
        self.__mouse_down_position = None

    def handle_events(self, events):
        for event in events:
            # print(f'Event: {event}')
            if event.type == pygame.MOUSEMOTION:
                self.__set_mouse_position(event.pos)
                if self.__mouse_down_position:
                    # The user is dragging the window rectangle.
                    offset = (self.__mouse_down_position[0] - event.pos[0],
                              self.__mouse_down_position[1] - event.pos[1])
                    self.__mouse_down_position = event.pos
                    self.__drag_grid(offset)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouse_down_position = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                self.__mouse_down_position = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    self.__zoom_in()
                if event.key == pygame.K_MINUS or event.key == pygame.K_UNDERSCORE:
                    self.__zoom_out()
        pass

    def __set_mouse_position(self, position):
        # Save the position so we can fix the hover coordinate after zoom changes.
        self.__last_mouse_position = position
        position_x, position_y = position
        # Update the given positions based on the concept of 0, 0 being in the middle.
        mouse_x = position_x - self.surface.get_width() / 2 - self.__coord_offset_x
        mouse_y = position_y - self.surface.get_height() / 2 - self.__coord_offset_y
        # Determine the coordinate associated with the current mouse position.
        coord_x = (mouse_x * HexGrid.precomputed_sqrt3 / 3 - mouse_y / 3) / self.hex_radius
        coord_z = mouse_y * 2 / 3 / self.hex_radius
        self.__hover_coord = Coord(coord_x, -coord_x - coord_z, coord_z).add_coord(self.__center_coord)

    def __drag_grid(self, offset):
        self.__coord_offset_x = self.__coord_offset_x - offset[0]
        self.__coord_offset_y = self.__coord_offset_y - offset[1]
        if abs(self.__coord_offset_x) > self.hex_width:
            delta = int(self.__coord_offset_x / self.hex_width)
            self.__coord_offset_x = self.__coord_offset_x - delta * self.hex_width
            self.__center_coord = self.__center_coord.add(-delta, delta, 0)
        height_delta = self.hex_height * 3 / 2
        if abs(self.__coord_offset_y) > height_delta:
            delta = int(self.__coord_offset_y / height_delta)
            self.__coord_offset_y = self.__coord_offset_y - delta * height_delta
            self.__center_coord = self.__center_coord.add(delta, delta, -2 * delta)

    def __zoom_in(self):
        if self.hex_radius < HEX_RADIUS_MAX:
            delta = 4 if self.hex_radius >= HEX_RADIUS_MID else 2
            self.hex_radius = self.hex_radius + delta
            self.__set_size_vars()
            if self.__last_mouse_position:
                self.__set_mouse_position(self.__last_mouse_position)

    def __zoom_out(self):
        if self.hex_radius > HEX_RADIUS_MIN:
            delta = 2 if self.hex_radius <= HEX_RADIUS_MID else 4
            self.hex_radius = self.hex_radius - delta
            self.__set_size_vars()
            if self.__last_mouse_position:
                self.__set_mouse_position(self.__last_mouse_position)

    def __set_size_vars(self):
        self.hex_height = self.hex_radius * 2
        self.hex_vertical_increase = self.hex_height * 3 / 4
        self.hex_width = HexGrid.precomputed_sqrt3div2 * self.hex_height
        self.hex_width_half = self.hex_width / 2

    def draw(self):
        self.__draw_hover()

    def __draw_hover(self):
        # Hex.draw_circle(self.surface, self.__last_mouse_position, int(self.hex_width_half), HOVER_HEX_COLOR)
        pass

    def get_center_position(self, coord):
        offset = coord.subtract_coord(self.__center_coord)
        coord_x = self.hex_radius * HexGrid.precomputed_sqrt3 * (offset.x + offset.z / 2)
        coord_x = coord_x + self.surface.get_width() / 2 + self.__coord_offset_x
        coord_y = self.hex_radius * 3 / 2 * offset.z
        coord_y = coord_y + self.surface.get_height() / 2 + self.__coord_offset_y
        return int(coord_x), int(coord_y)

    def __draw_coord(self, coord, color):
        Hex.draw_circle(self.surface, self.get_center_position(coord), int(self.hex_width_half), color)
