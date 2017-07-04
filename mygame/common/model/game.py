

class Game:
    def __init__(self, game_id, user_id):
        self.game_id = game_id
        self.user_id = user_id

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __str__(self):
        return f'Game[game_id={self.game_id}, user_id={self.user_id}]'
