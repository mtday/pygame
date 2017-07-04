
import sqlalchemy

from mygame.server.config.settings import DB_DRIVER
from mygame.server.config.settings import DB_HOST
from mygame.server.config.settings import DB_PORT
from mygame.server.config.settings import DB_USER
from mygame.server.config.settings import DB_PASS
from mygame.server.config.settings import DB_NAME
from mygame.server.db.dbgames import DbGames
from mygame.server.db.dbunits import DbUnits
from mygame.server.db.dbusers import DbUsers


class Db:
    def __init__(self):
        self.engine = sqlalchemy.create_engine(f'{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        self.games = DbGames(self.engine)
        self.units = DbUnits(self.engine)
        self.users = DbUsers(self.engine)
