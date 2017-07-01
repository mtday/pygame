
from mygame.config.settings import FPS_TARGET
from mygame.ui.window import Window
import pygame


class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = Window(self)
        self.clock = pygame.time.Clock()
        self.running = False

    def handle_events(self):
        events = pygame.event.get()
        self.window.handle_events(events)

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS_TARGET)
            self.handle_events()
            self.draw()
        pygame.quit()

    def stop(self):
        self.running = False

    def draw(self):
        self.window.draw()


if __name__ == '__main__':
    Main().run()
