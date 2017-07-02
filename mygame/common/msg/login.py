
from mygame.common.msg.message import Message


class LoginRequest(Message):
    TYPE = 'LogQ'
    VERSION = 1

    def __init__(self, login=None, password=None):
        super(LoginRequest, self).__init__(LoginRequest.TYPE, LoginRequest.VERSION)
        self.login = login
        self.password = password

    def send(self, socket):
        Message.send_text(socket, self.login)
        Message.send_text(socket, self.password)

    def recv(self, socket, msg_version):
        if LoginRequest.VERSION == msg_version:
            login = Message.recv_text(socket)
            password = Message.recv_text(socket)
            return LoginRequest(login, password)
        else:
            raise Exception(f'Unsupported message version: {msg_version}')


class LoginResponse(Message):
    TYPE = 'LogS'
    VERSION = 1

    def __init__(self, success=None):
        super(LoginResponse, self).__init__(LoginResponse.TYPE, LoginResponse.VERSION)
        self.success = success

    def send(self, socket):
        Message.send_bool(socket, self.success)

    def recv(self, socket, msg_version):
        if LoginResponse.VERSION == msg_version:
            success = Message.recv_bool(socket)
            return LoginResponse(success)
        else:
            raise Exception(f'Unsupported message version: {msg_version}')
