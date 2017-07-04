from mygame.common.config.settings import BYTE_ORDER
from mygame.common.model.coord import Coord
from mygame.common.msg.message import Message


class UnitRequest(Message):
    TYPE = 'UnitRequest'
    VERSION = 1

    def __init__(self, coord, distance):
        super(UnitRequest, self).__init__(UnitRequest.TYPE)
        self.coord = coord
        self.distance = distance

    @staticmethod
    def read(iostream):
        version = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        if version == 1:
            coord = Coord.read(iostream)
            distance = int.from_bytes(iostream.read(4), byteorder=BYTE_ORDER, signed=False)
            return UnitRequest(coord, distance)
        else:
            raise Exception(f'Unsupported version number: {version}')

    def write(self, iostream):
        iostream.write(UnitRequest.VERSION.to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        self.coord.write(iostream)
        iostream.write(int(self.distance).to_bytes(4, byteorder=BYTE_ORDER, signed=False))
