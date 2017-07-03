
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.model.coord import Coord
from mygame.common.model.unit import Unit
from mygame.common.model.unitfactory import UnitFactory
from mygame.common.msg.message import Message


class UnitRequest(Message):
    TYPE = 'UnitRequest'
    VERSION = 1

    def __init__(self, coord, distance):
        super(UnitRequest, self).__init__(UnitRequest.TYPE, UnitRequest.VERSION)
        self.coord = coord
        self.distance = distance

    @staticmethod
    def read(iostream, msg_version):
        if msg_version == UnitRequest.VERSION:
            coord = Coord.read(iostream)
            distance = int.from_bytes(iostream.read(4), byteorder=BYTE_ORDER, signed=False)
            return UnitRequest(coord, distance)
        else:
            raise Exception(f'Unsupported version number: {msg_version}')

    def write(self, iostream):
        self.coord.write(iostream)
        iostream.write(int(self.distance).to_bytes(4, byteorder=BYTE_ORDER, signed=False))


class UnitResponse(Message):
    TYPE = 'UnitResponse'
    VERSION = 1

    def __init__(self, units):
        super(UnitResponse, self).__init__(UnitResponse.TYPE, UnitResponse.VERSION)
        self.units = units

    @staticmethod
    def read(iostream, msg_version):
        if msg_version == UnitResponse.VERSION:
            unit_count = int.from_bytes(iostream.read(4), byteorder=BYTE_ORDER, signed=False)
            units = []
            for i in range(unit_count):
                units.append(UnitFactory.read(iostream))
            return UnitResponse(units)
        else:
            raise Exception(f'Unsupported version number: {msg_version}')

    def write(self, iostream):
        iostream.write(len(self.units).to_bytes(4, byteorder=BYTE_ORDER, signed=False))
        for unit in self.units:
            UnitFactory.write(iostream, unit)
