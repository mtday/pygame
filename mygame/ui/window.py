from mygame.config.colors import BLACK
from mygame.config.settings import WINDOW_SIZE
from mygame.config.settings import WINDOW_TITLE
from mygame.ui.hexgrid import HexGrid
import pygame


class Window:
    def __init__(self, main):
        self.main = main
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)
        self.hexgrid = HexGrid(self.screen)
        self.mouse_down_position = None

    def handle_events(self, events):
        for event in events:
            # print(f'Event: {event}')
            if event.type == pygame.QUIT:
                self.main.stop()
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

    def draw(self):
        self.screen.fill(BLACK)
        self.hexgrid.draw()
        pygame.display.flip()
