
import pygame

from mygame.client.config.settings import FPS_TARGET
from mygame.client.config.settings import SERVER_HOST
from mygame.client.config.settings import SERVER_PORT
from mygame.client.io.serverio import ServerIO
from mygame.client.ui.window import Window
from mygame.common.msg.login import LoginRequest


class Client:
    def __init__(self):
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
        self.running = True
        self.serverio.listen()
        self.serverio.send(LoginRequest('user', 'pass'))
        while self.running:
            self.clock.tick(FPS_TARGET)
            self.handle_events()
            self.draw()
        self.serverio.stop()
        pygame.quit()

    def stop(self):
        self.running = False

    def draw(self):
        self.window.draw()


if __name__ == '__main__':
    Client().run()
