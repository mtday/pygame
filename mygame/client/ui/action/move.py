
from mygame.client.ui.action.action import Action


class Move(Action):
    NAME = 'Move'

    def __init__(self):
        super(Move, self).__init__(Move.NAME)

    def perform(self):
        pass
