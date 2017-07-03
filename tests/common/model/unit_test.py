
import io
import unittest

from mygame.common.model.coord import Coord
from mygame.common.model.unit import Unit


class UnitTest(unittest.TestCase):
    def test_init(self):
        unit = Unit('type', 'id', Coord(1, 2, -3))
        self.assertEqual(unit.unit_type, 'type')
        self.assertEqual(unit.unit_id, 'id')
        self.assertEqual(unit.coord, Coord(1, 2, -3))

    def test_write_read(self):
        unit = Unit('type', 'id', Coord(1, 2, -3))
        outstream = io.BytesIO()
        Unit.write(outstream, unit)

        instream = io.BytesIO(outstream.getvalue())
        (unit_type, unit_id, coord) = Unit.read(instream, None, None, None)

        self.assertEqual(unit_type, unit.unit_type)
        self.assertEqual(unit_id, unit.unit_id)
        self.assertEqual(coord, unit.coord)

    def test_eq(self):
        a = Unit('type1', 'id1', Coord(1, 2, -3))
        b = Unit('type1', 'id1', Coord(1, -2, 1))
        c = Unit('type1', 'id2', Coord(1, 2, -3))
        d = Unit('type2', 'id1', Coord(1, 2, -3))
        self.assertTrue(a == a)
        self.assertTrue(a == b)   # only type and id are compared
        self.assertFalse(a == c)
        self.assertFalse(a == d)
        self.assertTrue(b == a)   # only type and id are compared
        self.assertTrue(b == b)
        self.assertFalse(b == c)
        self.assertFalse(b == d)
        self.assertFalse(c == a)
        self.assertFalse(c == b)
        self.assertTrue(c == c)
        self.assertFalse(c == d)
        self.assertFalse(d == a)
        self.assertFalse(d == b)
        self.assertFalse(d == c)
        self.assertTrue(d == d)

    def test_str(self):
        unit = Unit('type', 'id', Coord(1, 2, -3))
        self.assertEqual(str(unit), 'Unit[unit_type=type, unit_id=id, coord=Coord[x=1, y=2, z=-3]]')