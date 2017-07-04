
import logging
import socketserver

from mygame.common.msg.loginrequest import LoginRequest
from mygame.common.msg.messagefactory import MessageFactory
from mygame.common.msg.unitrequest import UnitRequest
from mygame.server.db.db import Db
from mygame.server.handler.loginhandler import LoginHandler
from mygame.server.handler.unithandler import UnitHandler


class HandlerManager:
    def __init__(self):
        self.db = Db()
        self.handlers = {
            LoginRequest.TYPE: LoginHandler(self.db),
            UnitRequest.TYPE: UnitHandler(self.db)
        }

    def get_handler(self, msg_type):
        if msg_type in self.handlers:
            return self.handlers[msg_type]
        return None


class Handler(socketserver.BaseRequestHandler):
    MGR = HandlerManager()

    def __init__(self, request, client_address, server):
        super(Handler, self).__init__(request, client_address, server)

    def handle(self):
        log = logging.getLogger(__name__)
        (data, socket) = self.request
        msg = MessageFactory.read(data)

        if not msg:
            log.warning('Ignoring unrecognized message type')
        else:
            log.info(f'Received message: {msg.msg_type}')
            handler = Handler.MGR.get_handler(msg.msg_type)
            if handler:
                handler.handle(socket, self.client_address, msg)
