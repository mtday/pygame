
from mygame.common.msg.messageio import MessageIO
from mygame.common.msg.login import LoginRequest, LoginResponse


class LoginHandler:
    @staticmethod
    def accept(msg_type):
        return msg_type == LoginRequest.TYPE

    @staticmethod
    def handle(request, login_request):
        print(f'Login request from: {login_request.login}')
        MessageIO.send(request, LoginResponse(True))
