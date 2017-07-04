
import io
import unittest

from mygame.common.model.coord import Coord
from mygame.common.model.unitfactory import UnitFactory
from mygame.common.model.unitinfo import UnitInfo
from mygame.common.unit.planet import Planet
from mygame.common.unit.recon import ReconDrone
from mygame.common.unit.sun import Sun


class UnitFactoryTest(unittest.TestCase):
    def test_write_read(self):
        a = Sun(UnitInfo(1, 1, 1, Coord(1, 2, -3)))
        b = Planet(UnitInfo(2, 2, 2, Coord(1, 2, -3)))
        c = ReconDrone(UnitInfo(3, 3, 3, Coord(1, 2, -3)))

        for unit in [a, b, c]:
            outstream = io.BytesIO()
            UnitFactory.write(outstream, unit)

            instream = io.BytesIO(outstream.getvalue())
            read = UnitFactory.read(instream)

            self.assertEqual(read.unit_type, unit.unit_type)
            self.assertEqual(read.unit_info.unit_id, unit.unit_info.unit_id)
            self.assertEqual(read.unit_info.user_id, unit.unit_info.user_id)
            self.assertEqual(read.unit_info.game_id, unit.unit_info.game_id)
            self.assertEqual(read.unit_info.coord, unit.unit_info.coord)
