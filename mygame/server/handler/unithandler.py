
import logging

from mygame.common.msg.messagefactory import MessageFactory
from mygame.common.msg.unitrequest import UnitRequest
from mygame.common.msg.unitresponse import UnitResponse


class UnitHandler:
    def __init__(self, db):
        self.db = db

    @staticmethod
    def accept(msg_type):
        return msg_type == UnitRequest.TYPE

    def handle(self, socket, client, unit_request):
        # Have to get logger here since HandlerManager is created statically.
        log = logging.getLogger(__name__)
        log.info('Handling unit request from coord %s with distance %d',
                 str(unit_request.coord), unit_request.distance)

        units = self.db.units.get_for_game(1)
        MessageFactory.write(socket, UnitResponse(units), client)
