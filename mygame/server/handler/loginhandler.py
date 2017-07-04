
import logging

from mygame.common.msg.loginrequest import LoginRequest
from mygame.common.msg.loginresponse import LoginResponse
from mygame.common.msg.messagefactory import MessageFactory


class LoginHandler:
    def __init__(self, db):
        self.db = db

    @staticmethod
    def accept(msg_type):
        return msg_type == LoginRequest.TYPE

    def handle(self, socket, client, login_request):
        # Have to get logger here since HandlerManager is created statically.
        log = logging.getLogger(__name__)
        log.info('Handling login request from: %s', login_request.login)

        user = self.db.users.get_by_login(login_request.login)
        MessageFactory.write(socket, LoginResponse(user is not None), client)
