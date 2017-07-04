from mygame.common.config.settings import BYTE_ORDER
from mygame.common.model.coord import Coord


class UnitInfo:
    VERSION = 1

    def __init__(self, unit_id, user_id, game_id, coord):
        self.unit_id = unit_id
        self.user_id = user_id
        self.game_id = game_id
        self.coord = coord

    @staticmethod
    def read(iostream):
        version = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        if version == 1:
            unit_id = int.from_bytes(iostream.read(4), byteorder=BYTE_ORDER, signed=False)
            user_id = int.from_bytes(iostream.read(4), byteorder=BYTE_ORDER, signed=False)
            game_id = int.from_bytes(iostream.read(4), byteorder=BYTE_ORDER, signed=False)
            coord = Coord.read(iostream)
            return UnitInfo(unit_id, user_id, game_id, coord)
        else:
            raise Exception(f'Unsupported serialization version: {version}')

    def write(self, iostream):
        iostream.write(UnitInfo.VERSION.to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        iostream.write(int(self.unit_id).to_bytes(4, byteorder=BYTE_ORDER, signed=False))
        iostream.write(int(self.user_id).to_bytes(4, byteorder=BYTE_ORDER, signed=False))
        iostream.write(int(self.game_id).to_bytes(4, byteorder=BYTE_ORDER, signed=False))
        self.coord.write(iostream)

    def __str__(self):
        return f'UnitInfo[unit_id={self.unit_id}, user_id={self.user_id}, game_id={self.game_id}, coord={self.coord}]'
