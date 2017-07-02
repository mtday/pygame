
from mygame.common.config.settings import BYTE_ENCODING
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.msg.login import LoginRequest, LoginResponse


class MessageIO:
    TYPES = [
        LoginRequest(), LoginResponse()
    ]

    @staticmethod
    def get_message(msg_type):
        for msg in MessageIO.TYPES:
            if msg.accept(msg_type):
                return msg
        return None

    @staticmethod
    def send(socket, message):
        MessageIO.send_msg_type(socket, message.msg_type)
        MessageIO.send_msg_version(socket, message.msg_version)
        message.send(socket)

    @staticmethod
    def recv(socket):
        msg_type = MessageIO.recv_msg_type(socket)
        msg_version = MessageIO.recv_msg_version(socket)
        msg = MessageIO.get_message(msg_type)
        if msg:
            return msg.recv(socket, msg_version)
        else:
            return None

    @staticmethod
    def send_msg_type(socket, msg_type):
        socket.sendall(bytes(msg_type, BYTE_ENCODING))

    @staticmethod
    def recv_msg_type(socket):
        return str(socket.recv(4), BYTE_ENCODING)

    @staticmethod
    def send_msg_version(socket, msg_version):
        socket.sendall(int(msg_version).to_bytes(1, byteorder=BYTE_ORDER, signed=False))

    @staticmethod
    def recv_msg_version(socket):
        return int.from_bytes(socket.recv(1), byteorder=BYTE_ORDER, signed=False)
