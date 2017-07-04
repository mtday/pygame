
from mygame.common.config.settings import BYTE_ENCODING
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.msg.message import Message


class LoginRequest(Message):
    TYPE = 'LoginRequest'
    VERSION = 1

    def __init__(self, login, password):
        super(LoginRequest, self).__init__(LoginRequest.TYPE)
        self.login = login
        self.password = password

    @staticmethod
    def read(iostream):
        version = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        if version == 1:
            login_len = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
            login = str(iostream.read(login_len), BYTE_ENCODING)
            password_len = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
            password = str(iostream.read(password_len), BYTE_ENCODING)
            return LoginRequest(login, password)
        else:
            raise Exception(f'Unsupported version number: {version}')

    def write(self, iostream):
        iostream.write(LoginRequest.VERSION.to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        login_bytes = self.login.encode(BYTE_ENCODING)
        iostream.write(len(login_bytes).to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        iostream.write(login_bytes)
        password_bytes = self.password.encode(BYTE_ENCODING)
        iostream.write(len(password_bytes).to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        iostream.write(password_bytes)


class LoginResponse(Message):
    TYPE = 'LoginResponse'
    VERSION = 1

    def __init__(self, success):
        super(LoginResponse, self).__init__(LoginResponse.TYPE)
        self.success = success

    @staticmethod
    def read(iostream):
        version = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        if version == 1:
            success = bool.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
            return LoginResponse(success)
        else:
            raise Exception(f'Unsupported version number: {version}')

    def write(self, iostream):
        iostream.write(LoginResponse.VERSION.to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        iostream.write(bool(self.success).to_bytes(1, byteorder=BYTE_ORDER, signed=False))
