
from mygame.model.coord import Coord
import unittest


class CoordTest(unittest.TestCase):
    def test_init_defaults(self):
        coord = Coord()
        self.assertEqual(coord.x, 0)
        self.assertEqual(coord.y, 0)
        self.assertEqual(coord.z, 0)

    def test_init_int_params(self):
        coord = Coord(1, 2, -3)
        self.assertEqual(coord.x, 1)
        self.assertEqual(coord.y, 2)
        self.assertEqual(coord.z, -3)

    @staticmethod
    @unittest.expectedFailure
    def test_init_int_invalid():
        Coord(1, 2, 3)

    def test_init_float_params(self):
        coord = Coord(1.1, 2.9, -4.0)
        self.assertEqual(coord.x, 1)
        self.assertEqual(coord.y, 3)
        self.assertEqual(coord.z, -4)

    def test_init_float_invalid(self):
        # The z value is calculated based on rounded x and y
        coord = Coord(1.1, 3.9, 2.5)
        self.assertEqual(coord.x, 1)
        self.assertEqual(coord.y, 4)
        self.assertEqual(coord.z, -5)

    def test_distance(self):
        a = Coord()
        b = Coord(0, 1, -1)
        c = Coord(1, -1, 0)
        d = Coord(2, -3, 1)
        self.assertEqual(a.distance_to(a), 0)
        self.assertEqual(a.distance_to(b), 1)
        self.assertEqual(a.distance_to(c), 1)
        self.assertEqual(a.distance_to(d), 3)
        self.assertEqual(b.distance_to(a), 1)
        self.assertEqual(b.distance_to(b), 0)
        self.assertEqual(b.distance_to(c), 2)
        self.assertEqual(b.distance_to(d), 4)
        self.assertEqual(c.distance_to(a), 1)
        self.assertEqual(c.distance_to(b), 2)
        self.assertEqual(c.distance_to(c), 0)
        self.assertEqual(c.distance_to(d), 2)
        self.assertEqual(d.distance_to(a), 3)
        self.assertEqual(d.distance_to(b), 4)
        self.assertEqual(d.distance_to(c), 2)
        self.assertEqual(d.distance_to(d), 0)

    def test_add_int_to_origin(self):
        coord = Coord().add(1, 2, -3)
        self.assertEqual(coord.x, 1)
        self.assertEqual(coord.y, 2)
        self.assertEqual(coord.z, -3)

    @staticmethod
    @unittest.expectedFailure
    def test_add_int_to_origin_invalid():
        Coord().add(1, 2, -4)

    def test_add_int_to_non_origin(self):
        coord = Coord(1, 1, -2).add(1, 2, -3)
        self.assertEqual(coord.x, 2)
        self.assertEqual(coord.y, 3)
        self.assertEqual(coord.z, -5)

    @staticmethod
    @unittest.expectedFailure
    def test_add_int_to_non_origin_invalid():
        Coord(1, 1, -2).add(1, 2, -4)

    def test_add_float_to_origin(self):
        coord = Coord().add(1.1, 2.9, -4.0)
        self.assertEqual(coord.x, 1)
        self.assertEqual(coord.y, 3)
        self.assertEqual(coord.z, -4)

    def test_add_float_to_origin_invalid(self):
        # The z value is calculated based on rounded x and y
        coord = Coord().add(1.1, 1.9, -3.0)
        self.assertEqual(coord.x, 1)
        self.assertEqual(coord.y, 2)
        self.assertEqual(coord.z, -3)

    def test_add_float_to_non_origin(self):
        coord = Coord(1.1, 2.9, -4.0).add(1.1, 2.9, -4.0)
        self.assertEqual(coord.x, 2)
        self.assertEqual(coord.y, 6)
        self.assertEqual(coord.z, -8)

    def test_add_float_to_non_origin_invalid(self):
        # The z value is calculated based on rounded x and y
        coord = Coord(1.1, 1.9, -3.0).add(1.1, 1.9, -3.0)
        self.assertEqual(coord.x, 2)
        self.assertEqual(coord.y, 4)
        self.assertEqual(coord.z, -6)

    def test_add_coord_to_origin(self):
        coord = Coord().add_coord(Coord(1, 2, -3))
        self.assertEqual(coord.x, 1)
        self.assertEqual(coord.y, 2)
        self.assertEqual(coord.z, -3)

    def test_add_coord_to_non_origin(self):
        coord = Coord(3, 2, -5).add_coord(Coord(1, 2, -3))
        self.assertEqual(coord.x, 4)
        self.assertEqual(coord.y, 4)
        self.assertEqual(coord.z, -8)

    def test_subtract_int_from_origin(self):
        coord = Coord().subtract(1, 2, -3)
        self.assertEqual(coord.x, -1)
        self.assertEqual(coord.y, -2)
        self.assertEqual(coord.z, 3)

    @staticmethod
    @unittest.expectedFailure
    def test_subtract_int_from_origin_invalid():
        Coord().subtract(1, 2, -4)

    def test_subtract_int_from_non_origin(self):
        coord = Coord(1, 1, -2).subtract(1, 2, -3)
        self.assertEqual(coord.x, 0)
        self.assertEqual(coord.y, -1)
        self.assertEqual(coord.z, 1)

    @staticmethod
    @unittest.expectedFailure
    def test_subtract_int_from_non_origin_invalid():
        Coord(1, 1, -2).subtract(1, 2, -4)

    def test_subtract_float_from_origin(self):
        coord = Coord().subtract(1.1, 2.9, -4.0)
        self.assertEqual(coord.x, -1)
        self.assertEqual(coord.y, -3)
        self.assertEqual(coord.z, 4)

    def test_subtract_float_from_origin_invalid(self):
        # The z value is calculated based on rounded x and y
        coord = Coord().subtract(1.1, 1.9, -3.0)
        self.assertEqual(coord.x, -1)
        self.assertEqual(coord.y, -2)
        self.assertEqual(coord.z, 3)

    def test_subtract_float_from_non_origin(self):
        coord = Coord(1.1, 2.9, -4.0).subtract(2.1, 1.9, -4.0)
        self.assertEqual(coord.x, -1)
        self.assertEqual(coord.y, 1)
        self.assertEqual(coord.z, 0)

    def test_subtract_float_from_non_origin_invalid(self):
        # The z value is calculated based on rounded x and y
        coord = Coord(1.1, 1.9, -3.0).subtract(2.1, 0.9, -3.0)
        self.assertEqual(coord.x, -1)
        self.assertEqual(coord.y, 1)
        self.assertEqual(coord.z, 0)

    def test_subtract_coord_from_origin(self):
        coord = Coord().subtract_coord(Coord(1, 2, -3))
        self.assertEqual(coord.x, -1)
        self.assertEqual(coord.y, -2)
        self.assertEqual(coord.z, 3)

    def test_subtract_coord_from_non_origin(self):
        coord = Coord(3, 2, -5).subtract_coord(Coord(1, 2, -3))
        self.assertEqual(coord.x, 2)
        self.assertEqual(coord.y, 0)
        self.assertEqual(coord.z, -2)

    def test_get_neighbor_from_origin(self):
        coord = Coord()
        neighbors = [coord.get_neighbor(i) for i in range(6)]
        self.assertEqual(len(neighbors), 6)
        self.assertEqual((neighbors[0].x, neighbors[0].y, neighbors[0].z), (1, -1, 0))
        self.assertEqual((neighbors[1].x, neighbors[1].y, neighbors[1].z), (1, 0, -1))
        self.assertEqual((neighbors[2].x, neighbors[2].y, neighbors[2].z), (0, 1, -1))
        self.assertEqual((neighbors[3].x, neighbors[3].y, neighbors[3].z), (-1, 1, 0))
        self.assertEqual((neighbors[4].x, neighbors[4].y, neighbors[4].z), (-1, 0, 1))
        self.assertEqual((neighbors[5].x, neighbors[5].y, neighbors[5].z), (0, -1, 1))

    def test_get_neighbor_from_non_origin(self):
        coord = Coord(2, -3, 1)
        neighbors = [coord.get_neighbor(i) for i in range(6)]
        self.assertEqual(len(neighbors), 6)
        self.assertEqual((neighbors[0].x, neighbors[0].y, neighbors[0].z), (3, -4, 1))
        self.assertEqual((neighbors[1].x, neighbors[1].y, neighbors[1].z), (3, -3, 0))
        self.assertEqual((neighbors[2].x, neighbors[2].y, neighbors[2].z), (2, -2, 0))
        self.assertEqual((neighbors[3].x, neighbors[3].y, neighbors[3].z), (1, -2, 1))
        self.assertEqual((neighbors[4].x, neighbors[4].y, neighbors[4].z), (1, -3, 2))
        self.assertEqual((neighbors[5].x, neighbors[5].y, neighbors[5].z), (2, -4, 2))

    def test_get_neighbors_from_origin(self):
        neighbors = Coord().get_neighbors()
        self.assertEqual(len(neighbors), 6)
        self.assertEqual((neighbors[0].x, neighbors[0].y, neighbors[0].z), (1, -1, 0))
        self.assertEqual((neighbors[1].x, neighbors[1].y, neighbors[1].z), (1, 0, -1))
        self.assertEqual((neighbors[2].x, neighbors[2].y, neighbors[2].z), (0, 1, -1))
        self.assertEqual((neighbors[3].x, neighbors[3].y, neighbors[3].z), (-1, 1, 0))
        self.assertEqual((neighbors[4].x, neighbors[4].y, neighbors[4].z), (-1, 0, 1))
        self.assertEqual((neighbors[5].x, neighbors[5].y, neighbors[5].z), (0, -1, 1))

    def test_get_neighbors_from_non_origin(self):
        neighbors = Coord(2, -3, 1).get_neighbors()
        self.assertEqual(len(neighbors), 6)
        self.assertEqual((neighbors[0].x, neighbors[0].y, neighbors[0].z), (3, -4, 1))
        self.assertEqual((neighbors[1].x, neighbors[1].y, neighbors[1].z), (3, -3, 0))
        self.assertEqual((neighbors[2].x, neighbors[2].y, neighbors[2].z), (2, -2, 0))
        self.assertEqual((neighbors[3].x, neighbors[3].y, neighbors[3].z), (1, -2, 1))
        self.assertEqual((neighbors[4].x, neighbors[4].y, neighbors[4].z), (1, -3, 2))
        self.assertEqual((neighbors[5].x, neighbors[5].y, neighbors[5].z), (2, -4, 2))
