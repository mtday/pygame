from mygame.common.config.settings import BYTE_ENCODING
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.config.settings import MESSAGE_SIZE_MAX


class Message:
    def __init__(self, msg_type, msg_version):
        self.msg_type = msg_type
        self.msg_version = msg_version

    def accept(self, the_type):
        return self.msg_type == the_type

    def send(self, socket):
        pass

    def recv(self, socket, msg_version):
        pass

    @staticmethod
    def send_text(socket, text):
        socket.sendall(len(text).to_bytes(2, byteorder=BYTE_ORDER, signed=False))
        socket.sendall(bytes(text, BYTE_ENCODING))

    @staticmethod
    def recv_text(socket):
        size = int.from_bytes(socket.recv(2), byteorder=BYTE_ORDER, signed=False)
        if size < MESSAGE_SIZE_MAX:
            return str(socket.recv(size), BYTE_ENCODING)
        else:
            # TODO: What do do when message size is too big?
            raise Exception(f'Invalid message size {size} is bigger than max {MESSAGE_SIZE_MAX}.')

    @staticmethod
    def send_int(socket, val):
        socket.sendall(int(val).to_bytes(4, byteorder=BYTE_ORDER, signed=True))

    @staticmethod
    def recv_int(socket):
        return int.from_bytes(socket.recv(4), byteorder=BYTE_ORDER, signed=True)

    @staticmethod
    def send_bool(socket, val):
        socket.sendall(bool(val).to_bytes(1, byteorder=BYTE_ORDER, signed=False))

    @staticmethod
    def recv_bool(socket):
        return bool.from_bytes(socket.recv(1), byteorder=BYTE_ORDER, signed=False)
