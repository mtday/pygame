
import unittest

from mygame.client.ui.unitmgr import UnitMgr
from mygame.common.model.coord import Coord
from mygame.common.model.unit import Unit


class UnitMgrTest(unittest.TestCase):
    def test_len(self):
        unitmgr = UnitMgr(None)
        self.assertEqual(len(unitmgr), 0)
        unitmgr.add(Unit('type1', 'id1', Coord()))
        unitmgr.add(Unit('type2', 'id2', Coord()))
        self.assertEqual(len(unitmgr), 2)

    def test_add(self):
        unitmgr = UnitMgr(None)
        unitmgr.add(Unit('type1', 'id1', Coord()))
        unitmgr.add(Unit('type2', 'id2', Coord()))
        self.assertEqual(len(unitmgr), 2)
        self.assertTrue('id1' in unitmgr)
        self.assertTrue('id2' in unitmgr)

    def test_remove(self):
        unitmgr = UnitMgr(None)
        unitmgr.add(Unit('type1', 'id1', Coord()))
        unitmgr.add(Unit('type2', 'id2', Coord()))
        self.assertEqual(len(unitmgr), 2)
        self.assertTrue('id1' in unitmgr)
        self.assertTrue('id2' in unitmgr)

        unitmgr.remove(Unit('type3', 'id3', Coord()))
        self.assertEqual(len(unitmgr), 2)
        self.assertTrue('id1' in unitmgr)
        self.assertTrue('id2' in unitmgr)

        unitmgr.remove(Unit('type1', 'id1', Coord()))
        self.assertEqual(len(unitmgr), 1)
        self.assertFalse('id1' in unitmgr)
        self.assertTrue('id2' in unitmgr)

    def test_remove_by_id(self):
        unitmgr = UnitMgr(None)
        unitmgr.add(Unit('type1', 'id1', Coord()))
        unitmgr.add(Unit('type2', 'id2', Coord()))
        self.assertEqual(len(unitmgr), 2)
        self.assertTrue('id1' in unitmgr)
        self.assertTrue('id2' in unitmgr)

        unitmgr.remove_by_id('id3')
        self.assertEqual(len(unitmgr), 2)
        self.assertTrue('id1' in unitmgr)
        self.assertTrue('id2' in unitmgr)

        unitmgr.remove_by_id('id1')
        self.assertEqual(len(unitmgr), 1)
        self.assertFalse('id1' in unitmgr)
        self.assertTrue('id2' in unitmgr)

    def test_get_by_id(self):
        unitmgr = UnitMgr(None)
        unitmgr.add(Unit('type1', 'id1', Coord()))
        unitmgr.add(Unit('type2', 'id2', Coord()))

        missing = unitmgr.get_by_id('missing')
        self.assertIsNone(missing)

        unit1 = unitmgr.get_by_id('id1')
        self.assertIsNotNone(unit1)
        self.assertEqual(unit1.unit_id, 'id1')
        self.assertEqual(unit1.unit_type, 'type1')

    def test_get_by_type(self):
        unitmgr = UnitMgr(None)
        unitmgr.add(Unit('type1', 'idA', Coord()))
        unitmgr.add(Unit('type2', 'idB', Coord()))
        unitmgr.add(Unit('type1', 'idC', Coord()))

        empty = unitmgr.get_by_type('missing')
        self.assertIsNotNone(empty)
        self.assertEqual(len(empty), 0)

        type1 = unitmgr.get_by_type('type1')
        self.assertIsNotNone(type1)
        self.assertEqual(len(type1), 2)
        self.assertEqual('idA', type1[0].unit_id)
        self.assertEqual('idC', type1[1].unit_id)

        type2 = unitmgr.get_by_type('type2')
        self.assertIsNotNone(type2)
        self.assertEqual(len(type2), 1)
        self.assertEqual('idB', type2[0].unit_id)

    def test_get_selected_default(self):
        unitmgr = UnitMgr(None)
        a = Unit('type1', 'id1', Coord())
        b = Unit('type2', 'id2', Coord())
        unitmgr.add(a)
        unitmgr.add(b)

        empty = unitmgr.get_selected()
        self.assertIsNotNone(empty)
        self.assertEqual(len(empty), 0)

        a.selected = True

        sel = unitmgr.get_selected()
        self.assertIsNotNone(sel)
        self.assertEqual(len(sel), 1)
        self.assertEqual(sel[0].unit_id, a.unit_id)

    def test_get_selected_true(self):
        unitmgr = UnitMgr(None)
        a = Unit('type1', 'id1', Coord())
        b = Unit('type2', 'id2', Coord())
        unitmgr.add(a)
        unitmgr.add(b)

        empty = unitmgr.get_selected(True)
        self.assertIsNotNone(empty)
        self.assertEqual(len(empty), 0)

        a.selected = True

        sel = unitmgr.get_selected(True)
        self.assertIsNotNone(sel)
        self.assertEqual(len(sel), 1)
        self.assertEqual(sel[0].unit_id, a.unit_id)

    def test_get_selected_false(self):
        unitmgr = UnitMgr(None)
        a = Unit('type1', 'id1', Coord())
        b = Unit('type2', 'id2', Coord())
        unitmgr.add(a)
        unitmgr.add(b)

        both = unitmgr.get_selected(False)
        self.assertIsNotNone(both)
        self.assertEqual(len(both), 2)
        self.assertEqual(both[0].unit_id, a.unit_id)
        self.assertEqual(both[1].unit_id, b.unit_id)

        a.selected = True

        unsel = unitmgr.get_selected(False)
        self.assertIsNotNone(unsel)
        self.assertEqual(len(unsel), 1)
        self.assertEqual(unsel[0].unit_id, b.unit_id)
