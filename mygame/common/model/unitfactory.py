from mygame.common.config.settings import BYTE_ENCODING
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.unit.planet import Planet
from mygame.common.unit.recon import ReconDrone
from mygame.common.unit.sun import Sun


class UnitFactory:
    VERSION = 1
    TYPES = {
        Planet.TYPE: Planet,
        ReconDrone.TYPE: ReconDrone,
        Sun.TYPE: Sun,
    }

    @staticmethod
    def get_unit(unit_type):
        if unit_type in UnitFactory.TYPES:
            return UnitFactory.TYPES[unit_type]
        return None

    @staticmethod
    def read(iostream):
        version = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        if version == 1:
            unit_type_len = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
            unit_type = str(iostream.read(unit_type_len), BYTE_ENCODING)
            unit = UnitFactory.get_unit(unit_type)
            if unit:
                return unit.read(iostream)
            else:
                raise Exception('Invalid unit received: {unit_type}')
        else:
            raise Exception(f'Unsupported serialization version: {version}')

    @staticmethod
    def write(iostream, unit):
        iostream.write(UnitFactory.VERSION.to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        iostream.write(len(unit.unit_type).to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        iostream.write(bytes(unit.unit_type, BYTE_ENCODING))
        unit.write(iostream)
