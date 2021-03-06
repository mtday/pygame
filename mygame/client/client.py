
import logging
import logging.config
import os
import pygame

from mygame.client.config.settings import FPS_TARGET
from mygame.client.config.settings import SERVER_HOST
from mygame.client.config.settings import SERVER_PORT
from mygame.client.io.serverio import ServerIO
from mygame.client.ui.window import Window
from mygame.common.model.coord import Coord
from mygame.common.msg.loginrequest import LoginRequest
from mygame.common.msg.unitrequest import UnitRequest


class Client:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        pygame.init()
        pygame.mixer.init()
        self.window = Window(self)
        self.clock = pygame.time.Clock()
        self.serverio = ServerIO(SERVER_HOST, SERVER_PORT)
        self.running = False

    def handle_events(self):
        events = pygame.event.get()
        self.window.handle_events(events)

    def run(self):
        self.log.info('Client running')
        self.running = True
        self.serverio.listen()
        # TODO: When do these happen?
        self.serverio.send(LoginRequest('user', 'pass'))
        self.serverio.send(UnitRequest(Coord(), 100))
        while self.running:
            self.clock.tick(FPS_TARGET)
            self.handle_events()
            self.draw()
        self.serverio.stop()
        pygame.quit()

    def stop(self):
        self.log.info('Client stopping')
        self.running = False

    def draw(self):
        self.window.draw()


if __name__ == '__main__':
    logging.config.fileConfig(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.ini'))
    Client().run()
