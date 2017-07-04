import logging
import sqlalchemy

from mygame.common.model.unit import Unit
from mygame.server.db.dbusers import DbUsers


class DbGames:
    TABLE = sqlalchemy.Table('games', sqlalchemy.MetaData(),
                             sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column('user_id', None, sqlalchemy.ForeignKey('users.id')))

    def __init__(self, engine):
        self.log = logging.getLogger(__name__)
        self.engine = engine

    def create_game(self, game):
        self.log.info('Creating game: {game}')

    def get_for_user(self, user_id):
        self.log.info('Fetching games for game: {game_id}')
        units = []
        with self.engine.connect() as conn:
            select = sqlalchemy.select([DbUnits.TABLE, DbUsers.TABLE]).select_from(
                DbUnits.TABLE.join(DbUsers.TABLE)).where(DbUnits.TABLE.c.id == unit_id)
            result = conn.execute(select)
            fetched = result.fetchone()
            if fetched:
                self.log.info(f'Unit retrieved: {fetched}')
                unit = None  # Unit(fetched['id'], fetched['login'])
            result.close()
        return unit
