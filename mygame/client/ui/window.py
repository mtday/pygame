import pygame
import random

from mygame.client.config.colors import BLACK
from mygame.client.config.settings import WINDOW_SIZE_DEFAULT
from mygame.client.config.settings import WINDOW_TITLE
from mygame.client.ui.hexgrid import HexGrid
from mygame.client.ui.unitmgr import UnitMgr
from mygame.common.model.coord import Coord
from mygame.common.unit.planet import Planet
from mygame.common.unit.recon import ReconDrone
from mygame.common.unit.sun import Sun


class Window:
    def __init__(self, client):
        self.client = client
        # self.window_settings = pygame.HWSURFACE | pygame.DOUBLEBUF
        # self.screen = pygame.display.set_mode((800, 600), self.window_settings)
        self.window_settings = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN
        self.screen = pygame.display.set_mode(Window.get_display_mode(), self.window_settings)
        pygame.display.set_caption(WINDOW_TITLE)
        self.hexgrid = HexGrid(self.screen)
        self.unitmgr = UnitMgr(self.hexgrid)
        # if self.window_settings & pygame.FULLSCREEN:
        #     pygame.mouse.set_visible(False)

        # Add some initial units for testing
        # TODO: These should come from the server
        self.unitmgr.add(Sun('id1', Coord()))
        self.unitmgr.add(Planet('id2', Window.get_random_coord(20)))
        self.unitmgr.add(ReconDrone('id3', Window.get_random_coord(30)))

    @staticmethod
    def get_random_coord(max_distance):
        x = random.randint(-max_distance, max_distance)
        if abs(x) < 3:
            x *= 3
        y = random.randint(-max_distance, max_distance)
        if abs(y) < 3:
            y *= 3
        z = -x - y
        return Coord(x, y, z)

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
            # print(f'Event: {event}')
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
        pygame.display.flip()
