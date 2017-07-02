
from mygame.common.msg.messageio import MessageIO
from mygame.common.msg.login import LoginRequest, LoginResponse


class LoginHandler:
    @staticmethod
    def accept(msg_type):
        return msg_type == LoginRequest.TYPE

    @staticmethod
    def handle(socket, client, login_request):
        print(f'Login request from: {login_request.login}')
        MessageIO.write(socket, LoginResponse(True), client)
