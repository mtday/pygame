import pygame

from mygame.config.colors import BLACK
from mygame.config.settings import WINDOW_SIZE_DEFAULT
from mygame.config.settings import WINDOW_TITLE
from mygame.ui.hexgrid import HexGrid


class Window:
    def __init__(self, main):
        self.main = main
        self.window_settings = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN
        self.screen = pygame.display.set_mode(Window.get_display_mode(), self.window_settings)
        pygame.display.set_caption(WINDOW_TITLE)
        self.hexgrid = HexGrid(self.screen)
        self.mouse_down_position = None

    @staticmethod
    def get_display_mode():
        available = pygame.display.list_modes()
        if len(available) > 0:
            return available[int(len(available) / 2)]
        return WINDOW_SIZE_DEFAULT

    def handle_events(self, events):
        for event in events:
            # print(f'Event: {event}')
            if event.type == pygame.QUIT:
                self.main.stop()
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.size, self.window_settings)
            elif event.type == pygame.MOUSEMOTION:
                self.hexgrid.set_mouse_position(event.pos)
                if self.mouse_down_position:
                    # The user is dragging the window rectangle.
                    offset = (self.mouse_down_position[0] - event.pos[0], self.mouse_down_position[1] - event.pos[1])
                    self.mouse_down_position = event.pos
                    self.hexgrid.drag_grid(offset)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down_position = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down_position = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    self.main.stop()
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    self.hexgrid.zoom_in()
                if event.key == pygame.K_MINUS or event.key == pygame.K_UNDERSCORE:
                    self.hexgrid.zoom_out()

    def draw(self):
        self.screen.fill(BLACK)
        self.hexgrid.draw()
        pygame.display.flip()
