import logging
import math
import pygame

from mygame.common.msg.unitresponse import UnitResponse


class UnitMgr:
    def __init__(self, hexgrid, menu):
        self.log = logging.getLogger(__name__)
        self.hexgrid = hexgrid
        self.menu = menu
        self.__units = {}

        self.__mouse_button = None
        self.__mouse_down_position = None
        self.__last_mouse_position = None
        self.__dragging = False

    def __len__(self):
        return len(self.__units)

    def __contains__(self, unit_id):
        return unit_id in self.__units

    def contains_id(self, unit_id):
        return unit_id in self.__units

    def contains(self, unit):
        return unit.unit_info.unit_id in self.__units

    def add(self, unit):
        self.__units[unit.unit_info.unit_id] = unit

    def remove(self, unit):
        if unit.unit_info.unit_id in self.__units:
            del self.__units[unit.unit_info.unit_id]

    def remove_by_id(self, unit_id):
        if unit_id in self.__units:
            del self.__units[unit_id]

    def get_by_id(self, unit_id):
        if unit_id in self.__units:
            return self.__units[unit_id]

    def get_by_type(self, unit_type):
        return [unit for unit in self.__units.values() if unit.unit_type == unit_type]

    def get_at_coord(self, coord):
        for unit in self.__units.values():
            if unit.unit_info.coord == coord:
                return unit

    def get_selected(self, selected=True):
        return [unit for unit in self.__units.values() if unit.selected == selected]

    def get_within(self, pos1, pos2):
        return [unit for unit in self.__units.values() if self.hexgrid.is_within(pos1, pos2, unit.unit_info.coord)]

    def select_within(self, pos1, pos2):
        for unit in self.get_within(pos1, pos2):
            self.log.info(f'  Selecting unit {unit.unit_type} at {unit.unit_info.coord}')
            unit.selected = True

    def deselect_all(self):
        self.log.info(f'  Deselecting all')
        for unit in self.__units.values():
            if unit.selected:
                unit.selected = False

    @staticmethod
    def __distance_between(pos1, pos2):
        x_delta = pos2[0] - pos1[0]
        y_delta = pos2[1] - pos1[1]
        return math.sqrt((x_delta * x_delta) + (y_delta * y_delta))

    def __handle_mouse_move(self, event):
        self.__last_mouse_position = event.pos
        if self.__mouse_button and not self.__dragging:
            # If a mouse button is pressed and the cursor moves more than 5 pixels, consider it a drag.
            distance = UnitMgr.__distance_between(self.__mouse_down_position, self.__last_mouse_position)
            self.__dragging = distance >= 5

    def __handle_mouse_down(self, event):
        self.__dragging = False
        self.__mouse_button = event.button
        self.__mouse_down_position = event.pos
        # If the menu is already visible, close it down since the user is clicking off of it.
        if self.menu.visible:
            self.menu.clear_actions()
            self.deselect_all()

    def __handle_mouse_up(self, event):
        self.__last_mouse_position = event.pos
        if self.__mouse_button == 1:
            if self.__dragging:
                # User made a selection. First deselect everything then mark the appropriate units as selected.
                self.deselect_all()
                self.select_within(self.__mouse_down_position, self.__last_mouse_position)
            else:
                # User clicked, get the coord of the clicked cell.
                clicked_coord = self.hexgrid.get_coord(self.__last_mouse_position)
                # Get the center position of the clicked coord.
                clicked_coord_position = self.hexgrid.get_center_position(clicked_coord)
                # Get the unit in the clicked coordinate (may be None).
                clicked_unit = self.get_at_coord(clicked_coord)

                # Get the available actions for the selected units (if any).
                selected = self.get_selected()
                if len(selected) > 0:
                    # There are some selected units, get the actions.
                    actions = []
                    for unit in selected:
                        actions += unit.get_actions(clicked_coord, clicked_unit)
                    if len(actions) > 0:
                        self.menu.display_actions(actions, clicked_coord_position)
                    else:
                        # No actions available, treat the click as a deselect
                        self.deselect_all()
                        self.menu.clear_actions()
                else:
                    self.menu.clear_actions()
        self.__mouse_button = None
        self.__mouse_down_position = None

    def handle_events(self, events):
        for event in events:
            # print(f'Event: {event}')
            if event.type == pygame.MOUSEMOTION:
                self.__handle_mouse_move(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.__handle_mouse_down(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.__handle_mouse_up(event)
            elif event.type == pygame.USEREVENT:
                if event.msg.msg_type == UnitResponse.TYPE:
                    for unit in event.msg.units:
                        self.add(unit)

    def draw(self):
        for unit in self.__units.values():
            unit.draw(self.hexgrid)
