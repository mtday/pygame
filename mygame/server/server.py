

class Server:
    def __init__(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            # TODO
            pass

    def stop(self):
        self.running = False


if __name__ == '__main__':
    Server().run()
