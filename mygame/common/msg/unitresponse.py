from mygame.common.config.settings import BYTE_ORDER
from mygame.common.model.unitfactory import UnitFactory
from mygame.common.msg.message import Message


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
