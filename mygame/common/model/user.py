

class User:
    def __init__(self, user_id, login):
        self.user_id = user_id
        self.login = login

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __str__(self):
        return f'User[user_id={self.user_id}, login={self.login}]'
