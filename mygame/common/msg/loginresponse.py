
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.msg.message import Message


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
