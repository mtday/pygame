
import unittest

from mygame.client.ui.menu import Menu
from mygame.client.ui.unitmgr import UnitMgr
from mygame.common.model.coord import Coord
from mygame.common.model.unit import Unit
from mygame.common.model.unitinfo import UnitInfo


class UnitMgrTest(unittest.TestCase):
    def test_len(self):
        unitmgr = UnitMgr(None, Menu(None))
        self.assertEqual(len(unitmgr), 0)
        unitmgr.add(Unit('type1', UnitInfo(1, 1, 1, Coord())))
        unitmgr.add(Unit('type2', UnitInfo(2, 1, 1, Coord())))
        self.assertEqual(len(unitmgr), 2)

    def test_add(self):
        unitmgr = UnitMgr(None, Menu(None))
        unitmgr.add(Unit('type1', UnitInfo(1, 1, 1, Coord())))
        unitmgr.add(Unit('type2', UnitInfo(2, 1, 1, Coord())))
        self.assertEqual(len(unitmgr), 2)
        self.assertTrue(1 in unitmgr)
        self.assertTrue(2 in unitmgr)

    def test_remove(self):
        unitmgr = UnitMgr(None, Menu(None))
        unitmgr.add(Unit('type1', UnitInfo(1, 1, 1, Coord())))
        unitmgr.add(Unit('type2', UnitInfo(2, 1, 1, Coord())))
        self.assertEqual(len(unitmgr), 2)
        self.assertTrue(1 in unitmgr)
        self.assertTrue(2 in unitmgr)

        unitmgr.remove(Unit('type3', UnitInfo(3, 1, 1, Coord())))
        self.assertEqual(len(unitmgr), 2)
        self.assertTrue(1 in unitmgr)
        self.assertTrue(2 in unitmgr)

        unitmgr.remove(Unit('type1', UnitInfo(1, 1, 1, Coord())))
        self.assertEqual(len(unitmgr), 1)
        self.assertFalse(1 in unitmgr)
        self.assertTrue(2 in unitmgr)

    def test_remove_by_id(self):
        unitmgr = UnitMgr(None, Menu(None))
        unitmgr.add(Unit('type1', UnitInfo(1, 1, 1, Coord())))
        unitmgr.add(Unit('type2', UnitInfo(2, 1, 1, Coord())))
        self.assertEqual(len(unitmgr), 2)
        self.assertTrue(1 in unitmgr)
        self.assertTrue(2 in unitmgr)

        unitmgr.remove_by_id(3)
        self.assertEqual(len(unitmgr), 2)
        self.assertTrue(1 in unitmgr)
        self.assertTrue(2 in unitmgr)

        unitmgr.remove_by_id(1)
        self.assertEqual(len(unitmgr), 1)
        self.assertFalse(1 in unitmgr)
        self.assertTrue(2 in unitmgr)

    def test_get_by_id(self):
        unitmgr = UnitMgr(None, Menu(None))
        unitmgr.add(Unit('type1', UnitInfo(1, 1, 1, Coord())))
        unitmgr.add(Unit('type2', UnitInfo(2, 1, 1, Coord())))

        missing = unitmgr.get_by_id('missing')
        self.assertIsNone(missing)

        unit1 = unitmgr.get_by_id(1)
        self.assertIsNotNone(unit1)
        self.assertEqual(unit1.unit_type, 'type1')
        self.assertEqual(unit1.unit_info.unit_id, 1)

    def test_get_by_type(self):
        unitmgr = UnitMgr(None, Menu(None))
        unitmgr.add(Unit('type1', UnitInfo(1, 1, 1, Coord())))
        unitmgr.add(Unit('type2', UnitInfo(2, 1, 1, Coord())))
        unitmgr.add(Unit('type1', UnitInfo(3, 1, 1, Coord())))

        empty = unitmgr.get_by_type('missing')
        self.assertIsNotNone(empty)
        self.assertEqual(len(empty), 0)

        type1 = unitmgr.get_by_type('type1')
        self.assertIsNotNone(type1)
        self.assertEqual(len(type1), 2)
        self.assertEqual(1, type1[0].unit_info.unit_id)
        self.assertEqual(3, type1[1].unit_info.unit_id)

        type2 = unitmgr.get_by_type('type2')
        self.assertIsNotNone(type2)
        self.assertEqual(len(type2), 1)
        self.assertEqual(2, type2[0].unit_info.unit_id)

    def test_get_selected_default(self):
        unitmgr = UnitMgr(None, Menu(None))
        a = Unit('type1', UnitInfo(1, 1, 1, Coord()))
        b = Unit('type2', UnitInfo(2, 1, 1, Coord()))
        unitmgr.add(a)
        unitmgr.add(b)

        empty = unitmgr.get_selected()
        self.assertIsNotNone(empty)
        self.assertEqual(len(empty), 0)

        a.selected = True

        sel = unitmgr.get_selected()
        self.assertIsNotNone(sel)
        self.assertEqual(len(sel), 1)
        self.assertEqual(sel[0].unit_info.unit_id, a.unit_info.unit_id)

    def test_get_selected_true(self):
        unitmgr = UnitMgr(None, Menu(None))
        a = Unit('type1', UnitInfo(1, 1, 1, Coord()))
        b = Unit('type2', UnitInfo(2, 1, 1, Coord()))
        unitmgr.add(a)
        unitmgr.add(b)

        empty = unitmgr.get_selected(True)
        self.assertIsNotNone(empty)
        self.assertEqual(len(empty), 0)

        a.selected = True

        sel = unitmgr.get_selected(True)
        self.assertIsNotNone(sel)
        self.assertEqual(len(sel), 1)
        self.assertEqual(sel[0].unit_info.unit_id, a.unit_info.unit_id)

    def test_get_selected_false(self):
        unitmgr = UnitMgr(None, Menu(None))
        a = Unit('type1', UnitInfo(1, 1, 1, Coord()))
        b = Unit('type2', UnitInfo(2, 1, 1, Coord()))
        unitmgr.add(a)
        unitmgr.add(b)

        both = unitmgr.get_selected(False)
        self.assertIsNotNone(both)
        self.assertEqual(len(both), 2)
        self.assertEqual(both[0].unit_info.unit_id, a.unit_info.unit_id)
        self.assertEqual(both[1].unit_info.unit_id, b.unit_info.unit_id)

        a.selected = True

        unsel = unitmgr.get_selected(False)
        self.assertIsNotNone(unsel)
        self.assertEqual(len(unsel), 1)
        self.assertEqual(unsel[0].unit_info.unit_id, b.unit_info.unit_id)
