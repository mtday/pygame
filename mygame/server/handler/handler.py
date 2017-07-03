
import socketserver

from mygame.common.io.messageio import MessageIO
from mygame.common.msg.login import LoginRequest
from mygame.common.msg.unit import UnitRequest
from mygame.server.handler.login import LoginHandler
from mygame.server.handler.unit import UnitHandler


class Handler(socketserver.BaseRequestHandler):
    HANDLERS = {
        LoginRequest.TYPE: LoginHandler,
        UnitRequest.TYPE: UnitHandler
    }

    def handle(self):
        (data, socket) = self.request
        msg = MessageIO.read(data)

        if not msg:
            raise Exception(f'Unrecognized message type: {msg.msg_type}')

        if msg.msg_type in Handler.HANDLERS:
            Handler.HANDLERS[msg.msg_type].handle(socket, self.client_address, msg)
