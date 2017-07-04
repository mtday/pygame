

class Unit:
    def __init__(self, unit_type, unit_info):
        self.unit_type = unit_type
        self.unit_info = unit_info
        self.movable = True
        self.selected = False

    def draw(self, hexgrid):
        pass

    @staticmethod
    def read(iostream):
        pass

    def write(self, iostream):
        pass

    def __eq__(self, other):
        return self.unit_info.unit_id == other.unit_info.unit_id

    def __str__(self):
        return f'Unit[unit_type={self.unit_type}, unit_info={self.unit_info}]'
