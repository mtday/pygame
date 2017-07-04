class Message:
    def __init__(self, msg_type):
        self.msg_type = msg_type

    def accept(self, msg_type):
        return self.msg_type == msg_type
