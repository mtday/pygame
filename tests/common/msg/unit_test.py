
import io
import unittest

from mygame.common.model.coord import Coord
from mygame.common.msg.unit import UnitRequest, UnitResponse
from mygame.common.unit.planet import Planet
from mygame.common.unit.recon import ReconDrone
from mygame.common.unit.sun import Sun


class UnitTest(unittest.TestCase):
    def test_request_write_read(self):
        outstream = io.BytesIO()
        UnitRequest(Coord(1, 2, -3), 10).write(outstream)

        instream = io.BytesIO(outstream.getvalue())
        request = UnitRequest.read(instream, UnitRequest.VERSION)

        self.assertEqual(request.coord, Coord(1, 2, -3))
        self.assertEqual(request.distance, 10)

    def test_response_empty_write_read(self):
        outstream = io.BytesIO()
        UnitResponse([]).write(outstream)

        instream = io.BytesIO(outstream.getvalue())
        response = UnitResponse.read(instream, UnitResponse.VERSION)

        self.assertIsNotNone(response.units)
        self.assertEqual(len(response.units), 0)

    def test_response_nonempty_write_read(self):
        outstream = io.BytesIO()
        a = Sun('a', Coord(1, 2, -3))
        b = Planet('b', Coord(1, -2, 1))
        c = ReconDrone('c', Coord(2, -3, 1))
        UnitResponse([a, b, c]).write(outstream)

        instream = io.BytesIO(outstream.getvalue())
        response = UnitResponse.read(instream, UnitResponse.VERSION)

        self.assertIsNotNone(response.units)
        self.assertEqual(len(response.units), 3)
        self.assertEqual(response.units[0], a)
        self.assertEqual(response.units[1], b)
        self.assertEqual(response.units[2], c)
