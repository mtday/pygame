
import logging

from mygame.common.io.messageio import MessageIO
from mygame.common.msg.login import LoginRequest, LoginResponse


class LoginHandler:
    LOG = logging.getLogger(__name__)

    @staticmethod
    def accept(msg_type):
        return msg_type == LoginRequest.TYPE

    @staticmethod
    def handle(socket, client, login_request):
        LoginHandler.LOG.debug('Handling login request from: %s', login_request.login)
        # TODO verify the login request information
        MessageIO.write(socket, LoginResponse(True), client)
