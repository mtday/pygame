
import logging
import select
import socket
import threading

import pygame

from mygame.common.msg.messagefactory import MessageFactory


class ServerIO:
    def __init__(self, host, port):
        self.log = logging.getLogger(__name__)
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(True)
        self.listener_thread = threading.Thread(target=self.receive, daemon=True)
        self.receiving = False

    def listen(self):
        self.sock.connect((self.host, self.port))
        self.listener_thread.start()

    def send(self, message):
        MessageFactory.write(self.sock, message)

    def receive(self):
        self.receiving = True
        try:
            while self.receiving:
                input_ready, _, except_ready = select.select([self.sock], [], [self.sock])
                for s in input_ready:
                    (data, server) = s.recvfrom(4096)
                    if data:
                        message = MessageFactory.read(data)
                        if message:
                            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'msg': message}))
                for s in except_ready:
                    self.log.warning('Exception with connection to server, reconnecting')
                    s.close()
                    s.connect((self.host, self.port))
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.receiving = False
        self.sock.close()
