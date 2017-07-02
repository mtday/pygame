
import io

from mygame.common.msg.login import LoginRequest, LoginResponse
from mygame.common.msg.message import Message


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
    def write(socket, message, client=None):
        iostream = io.BytesIO()
        Message.write(iostream, message)
        message.write(iostream)
        if client:
            socket.sendto(iostream.getvalue(), client)
        else:
            socket.sendall(iostream.getvalue())
        iostream.close()

    @staticmethod
    def read(data):
        iostream = io.BytesIO(data)
        (msg_type, msg_version) = Message.read(iostream)
        msg = MessageIO.get_message(msg_type)
        if msg:
            msg = msg.read(iostream)
        else:
            raise Exception("Invalid message received: '{msg_type}', '{msg_version}'")
        iostream.close()
        return msg
