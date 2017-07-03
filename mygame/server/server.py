
import logging
import logging.config
import os
import socketserver
import threading

from mygame.server.handler.handler import Handler


class Listener(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass


class Server:
    HOST = "localhost"
    PORT = 34455

    def __init__(self):
        logging.config.fileConfig(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.ini'))
        self.log = logging.getLogger(__name__)
        self.running = False
        self.server = Listener((Server.HOST, Server.PORT), Handler)
        self.server_thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    def run(self):
        self.log.info(f'Server starting on host %s:%d', Server.HOST, Server.PORT)
        self.running = True
        self.server_thread.start()
        try:
            while self.running:
                pass
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.log.info(f'Server stopping')
        self.running = False
        self.server.shutdown()
        self.server.server_close()


if __name__ == '__main__':
    Server().run()
