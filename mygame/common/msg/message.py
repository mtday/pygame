from mygame.common.config.settings import BYTE_ENCODING
from mygame.common.config.settings import BYTE_ORDER


class Message:
    def __init__(self, msg_type, msg_version):
        self.msg_type = msg_type
        self.msg_version = msg_version

    def accept(self, msg_type):
        return self.msg_type == msg_type

    @staticmethod
    def write(iostream, msg):
        msg_type_bytes = msg.msg_type.encode(BYTE_ENCODING)
        iostream.write(len(msg_type_bytes).to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        iostream.write(msg_type_bytes)
        iostream.write(int(msg.msg_version).to_bytes(1, byteorder=BYTE_ORDER, signed=False))

    @staticmethod
    def read(iostream):
        msg_type_len = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        msg_type = str(iostream.read(msg_type_len), BYTE_ENCODING)
        msg_version = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        return msg_type, msg_version
