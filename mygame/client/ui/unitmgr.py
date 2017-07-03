
import pygame

from mygame.common.msg.unit import UnitResponse


class UnitMgr:
    def __init__(self, hexgrid):
        self.hexgrid = hexgrid
        self.__units = {}

        self.__mouse_button = None
        self.__mouse_down_position = None
        self.__last_mouse_position = None

    def __len__(self):
        return len(self.__units)

    def __contains__(self, unit_id):
        return unit_id in self.__units

    def contains_id(self, unit_id):
        return unit_id in self.__units

    def contains(self, unit):
        return unit.unit_id in self.__units

    def add(self, unit):
        self.__units[unit.unit_id] = unit

    def remove(self, unit):
        if unit.unit_id in self.__units:
            del self.__units[unit.unit_id]

    def remove_by_id(self, unit_id):
        if unit_id in self.__units:
            del self.__units[unit_id]

    def get_by_id(self, unit_id):
        if unit_id in self.__units:
            return self.__units[unit_id]

    def get_by_type(self, unit_type):
        return [unit for unit in self.__units.values() if unit.unit_type == unit_type]

    def get_selected(self, selected=True):
        return [unit for unit in self.__units.values() if unit.selected == selected]

    def get_within(self, pos1, pos2):
        return [unit for unit in self.__units.values() if self.hexgrid.is_within(pos1, pos2, unit.coord)]

    def handle_events(self, events):
        for event in events:
            # print(f'Event: {event}')
            if event.type == pygame.MOUSEMOTION:
                self.__last_mouse_position = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouse_button = event.button
                self.__mouse_down_position = event.pos
                if self.__mouse_button == 1:
                    # User is starting a selection, deselect all selected units
                    selected_units = self.get_selected()
                    for unit in selected_units:
                        unit.selected = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.__mouse_button == 1:
                    # User used the left mouse button and made a selection, mark the appropriate units as selected
                    for unit in self.get_within(self.__mouse_down_position, self.__last_mouse_position):
                        unit.selected = True
                self.__mouse_button = None
                self.__mouse_down_position = None
            elif event.type == pygame.USEREVENT:
                if event.msg.msg_type == UnitResponse.TYPE:
                    for unit in event.msg.units:
                        self.add(unit)

    def draw(self):
        for unit in self.__units.values():
            unit.draw(self.hexgrid)
