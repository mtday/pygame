
import socket

from mygame.common.msg.login import LoginRequest
from mygame.common.msg.messageio import MessageIO


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 34455))
try:
    MessageIO.send(sock, LoginRequest('user', 'pass'))
    response = MessageIO.recv(sock)
    print(f'Received: {response}')
finally:
    sock.close()
