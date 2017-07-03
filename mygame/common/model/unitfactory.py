
from mygame.common.config.settings import BYTE_ENCODING
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.model.coord import Coord
from mygame.common.model.unit import Unit
from mygame.common.unit.planet import Planet
from mygame.common.unit.recon import ReconDrone
from mygame.common.unit.sun import Sun


class UnitFactory:
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
        (unit_type, unit_id, coord) = Unit.read(iostream, None, None, None)
        unit = UnitFactory.get_unit(unit_type)
        if unit:
            return unit.read(iostream, unit_type, unit_id, coord)
        else:
            raise Exception("Invalid unit received: '{unit_type}', '{unit_id}'")

    @staticmethod
    def write(iostream, unit):
        Unit.write(iostream, unit)
        unit.write(iostream, unit)
