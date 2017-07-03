
from mygame.common.config.settings import BYTE_ENCODING
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.model.coord import Coord


class Unit:
    def __init__(self, unit_type, unit_id, coord):
        self.unit_type = unit_type
        self.unit_id = unit_id
        self.coord = coord

        self.movable = True
        self.selected = False

    def draw(self, hexgrid):
        pass

    @staticmethod
    def read(iostream, unit_type, unit_id, coord):
        unit_type_len = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=True)
        unit_type = str(iostream.read(unit_type_len), BYTE_ENCODING)
        unit_id_len = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=True)
        unit_id = str(iostream.read(unit_id_len), BYTE_ENCODING)
        coord = Coord.read(iostream)
        return unit_type, unit_id, coord

    @staticmethod
    def write(iostream, unit):
        unit_type_bytes = bytes(unit.unit_type, BYTE_ENCODING)
        iostream.write(len(unit_type_bytes).to_bytes(1, byteorder=BYTE_ORDER, signed=True))
        iostream.write(unit_type_bytes)
        unit_id_bytes = bytes(unit.unit_id, BYTE_ENCODING)
        iostream.write(len(unit_id_bytes).to_bytes(1, byteorder=BYTE_ORDER, signed=True))
        iostream.write(unit_id_bytes)
        unit.coord.write(iostream)

    def __eq__(self, other):
        return self.unit_type == other.unit_type and self.unit_id == other.unit_id

    def __str__(self):
        return f'Unit[unit_type={self.unit_type}, unit_id={self.unit_id}, coord={self.coord}]'
