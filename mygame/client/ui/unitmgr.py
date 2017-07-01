

class UnitMgr:
    def __init__(self, surface):
        self.surface = surface
        self.__units = {}

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

    def handle_events(self, events):
        pass

    def draw(self):
        pass
