
import socketserver

from mygame.common.msg.messageio import MessageIO
from mygame.server.handler.login import LoginHandler


class Handler(socketserver.BaseRequestHandler):
    HANDLERS = [
        LoginHandler()
    ]

    def handle(self):
        msg = MessageIO.recv(self.request)

        if not msg:
            raise Exception(f'Unrecognized message type: {msg.msg_type}')

        for handler in Handler.HANDLERS:
            if handler.accept(msg.msg_type):
                handler.handle(self.request, msg)
