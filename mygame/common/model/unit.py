
class Unit:
    def __init__(self, unit_type, unit_id, coord):
        self.unit_type = unit_type
        self.unit_id = unit_id
        self.coord = coord
        self.selected = False
        self.movable = True

    def draw(self, hexgrid):
        pass
