import io

from mygame.common.config.settings import BYTE_ENCODING
from mygame.common.config.settings import BYTE_ORDER
from mygame.common.msg.loginrequest import LoginRequest
from mygame.common.msg.loginresponse import LoginResponse
from mygame.common.msg.unitrequest import UnitRequest
from mygame.common.msg.unitresponse import UnitResponse


class MessageFactory:
    VERSION = 1
    TYPES = {
        LoginRequest.TYPE: LoginRequest,
        LoginResponse.TYPE: LoginResponse,
        UnitRequest.TYPE: UnitRequest,
        UnitResponse.TYPE: UnitResponse
    }

    @staticmethod
    def get_message(msg_type):
        if msg_type in MessageFactory.TYPES:
            return MessageFactory.TYPES[msg_type]
        return None

    @staticmethod
    def read(data):
        iostream = io.BytesIO(data)
        version = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
        if version == 1:
            msg_type_len = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=False)
            msg_type = str(iostream.read(msg_type_len), BYTE_ENCODING)
            msg = MessageFactory.get_message(msg_type)
            if msg:
                return msg.read(iostream)
            else:
                raise Exception("Invalid message received: '{msg_type}', '{msg_version}'")
        else:
            raise Exception(f'Unsupported serialization version: {version}')

    @staticmethod
    def write(socket, message, client=None):
        iostream = io.BytesIO()
        iostream.write(int(MessageFactory.VERSION).to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        msg_type_bytes = message.msg_type.encode(BYTE_ENCODING)
        iostream.write(len(msg_type_bytes).to_bytes(1, byteorder=BYTE_ORDER, signed=False))
        iostream.write(msg_type_bytes)
        message.write(iostream)
        data = iostream.getvalue()
        if client:
            socket.sendto(data, client)
        else:
            socket.sendall(data)
        iostream.close()

