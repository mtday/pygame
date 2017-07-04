import io
import unittest

from mygame.common.msg.loginresponse import LoginResponse


class LoginResponseTest(unittest.TestCase):
    def test_response_true_write_read(self):
        outstream = io.BytesIO()
        LoginResponse(True).write(outstream)

        instream = io.BytesIO(outstream.getvalue())
        response = LoginResponse.read(instream)

        self.assertEqual(response.success, True)

    def test_response_false_write_read(self):
        outstream = io.BytesIO()
        LoginResponse(False).write(outstream)

        instream = io.BytesIO(outstream.getvalue())
        response = LoginResponse.read(instream)

        self.assertEqual(response.success, False)
