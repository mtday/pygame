
import io

from mygame.common.msg.login import LoginRequest, LoginResponse
from mygame.common.msg.unit import UnitRequest, UnitResponse
from mygame.common.msg.message import Message


class MessageIO:
    TYPES = {
        LoginRequest.TYPE: LoginRequest,
        LoginResponse.TYPE: LoginResponse,
        UnitRequest.TYPE: UnitRequest,
        UnitResponse.TYPE: UnitResponse
    }

    @staticmethod
    def get_message(msg_type):
        if msg_type in MessageIO.TYPES:
            return MessageIO.TYPES[msg_type]
        return None

    @staticmethod
    def read(data):
        iostream = io.BytesIO(data)
        (msg_type, msg_version) = Message.read(iostream, 0)
        msg = MessageIO.get_message(msg_type)
        if msg:
            msg = msg.read(iostream, msg_version)
        else:
            raise Exception("Invalid message received: '{msg_type}', '{msg_version}'")
        iostream.close()
        return msg

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
