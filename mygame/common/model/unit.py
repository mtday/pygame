
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

    def write(self, iostream):
        unit_type_bytes = bytes(self.unit_type, BYTE_ENCODING)
        iostream.write(len(unit_type_bytes).to_bytes(1, byteorder=BYTE_ORDER, signed=True))
        iostream.write(unit_type_bytes)
        unit_id_bytes = bytes(self.unit_id, BYTE_ENCODING)
        iostream.write(len(unit_id_bytes).to_bytes(1, byteorder=BYTE_ORDER, signed=True))
        iostream.write(unit_id_bytes)
        iostream.write(self.coord)

    @staticmethod
    def read(iostream):
        unit_type_len = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=True)
        unit_type = str(iostream.read(unit_type_len), BYTE_ENCODING)
        unit_id_len = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=True)
        unit_id = str(iostream.read(unit_id_len), BYTE_ENCODING)
        coord = Coord.read(iostream)
        return unit_type, unit_id, coord
