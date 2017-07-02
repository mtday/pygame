
from mygame.common.config.settings import BYTE_ENCODING
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.msg.message import Message


class LoginRequest(Message):
    TYPE = 'LoginRequest'
    VERSION = 1

    def __init__(self, login=None, password=None):
        super(LoginRequest, self).__init__(LoginRequest.TYPE, LoginRequest.VERSION)
        self.login = login
        self.password = password

    def write(self, iostream):
        login_bytes = self.login.encode(BYTE_ENCODING)
        iostream.write(len(login_bytes).to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        iostream.write(login_bytes)
        password_bytes = self.password.encode(BYTE_ENCODING)
        iostream.write(len(password_bytes).to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        iostream.write(password_bytes)

    @staticmethod
    def read(iostream):
        login_len = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        login = str(iostream.read(login_len), BYTE_ENCODING)
        password_len = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        password = str(iostream.read(password_len), BYTE_ENCODING)
        return LoginRequest(login, password)


class LoginResponse(Message):
    TYPE = 'LoginResponse'
    VERSION = 1

    def __init__(self, success=None):
        super(LoginResponse, self).__init__(LoginResponse.TYPE, LoginResponse.VERSION)
        self.success = success

    def write(self, iostream):
        iostream.write(bool(self.success).to_bytes(1, byteorder=BYTE_ORDER, signed=False))

    @staticmethod
    def read(iostream):
        success = bool.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        return LoginResponse(success)
