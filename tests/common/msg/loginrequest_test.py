import io
import unittest

from mygame.common.msg.loginrequest import LoginRequest


class LoginRequestTest(unittest.TestCase):
    def test_request_write_read(self):
        outstream = io.BytesIO()
        LoginRequest('user', 'pass').write(outstream)

        instream = io.BytesIO(outstream.getvalue())
        request = LoginRequest.read(instream)

        self.assertEqual(request.login, 'user')
        self.assertEqual(request.password, 'pass')
