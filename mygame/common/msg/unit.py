
import logging

from mygame.common.config.settings import BYTE_ORDER
from mygame.common.model.coord import Coord
from mygame.common.model.unitfactory import UnitFactory
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


class UnitResponse(Message):
    TYPE = 'UnitResponse'
    VERSION = 1

    def __init__(self, units):
        super(UnitResponse, self).__init__(UnitResponse.TYPE)
        self.units = units
        if len(units) > 255:
            raise Exception(f'Too many units for response: {len(units)}')

    @staticmethod
    def read(iostream):
        version = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        if version == 1:
            unit_count = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
            units = []
            for i in range(unit_count):
                units.append(UnitFactory.read(iostream))
            return UnitResponse(units)
        else:
            raise Exception(f'Unsupported version number: {version}')

    def write(self, iostream):
        iostream.write(UnitResponse.VERSION.to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        iostream.write(len(self.units).to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        for unit in self.units:
            UnitFactory.write(iostream, unit)
