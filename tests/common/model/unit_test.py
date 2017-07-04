
import unittest

from mygame.common.model.coord import Coord
from mygame.common.model.unit import Unit
from mygame.common.model.unitinfo import UnitInfo


class UnitTest(unittest.TestCase):
    def test_init(self):
        unit = Unit('type', UnitInfo(10, 11, 12, Coord(1, 2, -3)))
        self.assertEqual(unit.unit_type, 'type')
        self.assertEqual(unit.unit_info.unit_id, 10)
        self.assertEqual(unit.unit_info.user_id, 11)
        self.assertEqual(unit.unit_info.game_id, 12)
        self.assertEqual(unit.unit_info.coord, Coord(1, 2, -3))

    def test_eq(self):
        # Only the unit id is checked
        a = Unit('type1', UnitInfo(1, 2, 3, Coord(1, 2, -3)))
        b = Unit('type1', UnitInfo(2, 2, 3, Coord(1, 2, -3)))
        self.assertTrue(a == a)
        self.assertFalse(a == b)
        self.assertFalse(b == a)
        self.assertTrue(b == b)

    def test_str(self):
        unit = Unit('type', UnitInfo(10, 11, 12, Coord(1, 2, -3)))
        self.assertEqual(str(unit), 'Unit[unit_type=type, unit_info=UnitInfo[unit_id=10, user_id=11, game_id=12,' +
                         ' coord=Coord[x=1, y=2, z=-3]]]')
