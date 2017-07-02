
import socketserver
import threading

from mygame.server.handler.handler import Handler


class Listener(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass


class Server:
    HOST = "localhost"
    PORT = 34455

    def __init__(self):
        self.running = False
        self.server = Listener((Server.HOST, Server.PORT), Handler)
        self.server_thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    def run(self):
        self.running = True
        self.server_thread.start()
        try:
            while self.running:
                pass
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.running = False
        self.server.shutdown()
        self.server.server_close()


if __name__ == '__main__':
    Server().run()
