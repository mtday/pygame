import pygame

from mygame.client.config.colors import BLACK
from mygame.client.config.settings import WINDOW_SIZE_DEFAULT
from mygame.client.config.settings import WINDOW_TITLE
from mygame.client.ui.hexgrid import HexGrid
from mygame.client.ui.menu import Menu
from mygame.client.ui.unitmgr import UnitMgr


class Window:
    def __init__(self, client):
        self.client = client
        self.window_settings = pygame.HWSURFACE | pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode((800, 600), self.window_settings)
        # self.window_settings = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN
        # self.screen = pygame.display.set_mode(Window.get_display_mode(), self.window_settings)
        pygame.display.set_caption(WINDOW_TITLE)
        self.hexgrid = HexGrid(self.screen)
        self.menu = Menu(self.hexgrid)
        self.unitmgr = UnitMgr(self.hexgrid, self.menu)
        # if self.window_settings & pygame.FULLSCREEN:
        #     pygame.mouse.set_visible(False)

    @staticmethod
    def get_display_mode():
        available = pygame.display.list_modes()
        if len(available) > 0:
            return available[int(len(available) / 2)]
        return WINDOW_SIZE_DEFAULT

    def handle_events(self, events):
        self.hexgrid.handle_events(events)
        self.unitmgr.handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                self.client.stop()
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.size, self.window_settings)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    self.client.stop()

    def draw(self):
        self.screen.fill(BLACK)
        self.hexgrid.draw()
        self.unitmgr.draw()
        self.menu.draw()
        pygame.display.flip()
