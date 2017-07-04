
import io
import unittest

from mygame.common.model.coord import Coord
from mygame.common.msg.unitrequest import UnitRequest


class UnitRequestTest(unittest.TestCase):
    def test_request_write_read(self):
        outstream = io.BytesIO()
        UnitRequest(Coord(1, 2, -3), 10).write(outstream)

        instream = io.BytesIO(outstream.getvalue())
        request = UnitRequest.read(instream)

        self.assertEqual(request.coord, Coord(1, 2, -3))
        self.assertEqual(request.distance, 10)
