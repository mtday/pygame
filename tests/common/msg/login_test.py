
import io
import unittest

from mygame.common.msg.login import LoginRequest, LoginResponse


class LoginTest(unittest.TestCase):
    def test_request_write_read(self):
        outstream = io.BytesIO()
        LoginRequest('user', 'pass').write(outstream)

        instream = io.BytesIO(outstream.getvalue())
        request = LoginRequest.read(instream, LoginRequest.VERSION)

        self.assertEqual(request.login, 'user')
        self.assertEqual(request.password, 'pass')

    def test_response_true_write_read(self):
        outstream = io.BytesIO()
        LoginResponse(True).write(outstream)

        instream = io.BytesIO(outstream.getvalue())
        response = LoginResponse.read(instream, LoginResponse.VERSION)

        self.assertEqual(response.success, True)

    def test_response_false_write_read(self):
        outstream = io.BytesIO()
        LoginResponse(False).write(outstream)

        instream = io.BytesIO(outstream.getvalue())
        response = LoginResponse.read(instream, LoginResponse.VERSION)

        self.assertEqual(response.success, False)
