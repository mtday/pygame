
import random

from mygame.common.io.messageio import MessageIO
from mygame.common.model.coord import Coord
from mygame.common.msg.unit import UnitRequest, UnitResponse
from mygame.common.unit.planet import Planet
from mygame.common.unit.recon import ReconDrone
from mygame.common.unit.sun import Sun


class UnitHandler:
    @staticmethod
    def accept(msg_type):
        return msg_type == UnitRequest.TYPE

    @staticmethod
    def handle(socket, client, unit_request):
        print(f'Unit request for location: {unit_request.coord} and distance {unit_request.distance}')
        sun = Sun('sun', Coord(0, 0, 0))
        planet = Planet('planet', UnitHandler.get_random_coord(20))
        recon = ReconDrone('recon', UnitHandler.get_random_coord(30))
        MessageIO.write(socket, UnitResponse([sun, planet, recon]), client)

    @staticmethod
    def get_random_coord(max_distance):
        x = random.randint(-max_distance, max_distance)
        if abs(x) < 3:
            x *= 3
        z = random.randint(-max_distance, max_distance)
        if abs(z) < 3:
            z *= 3
        y = -x - z
        return Coord(x, y, z)
