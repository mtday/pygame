import logging
import sqlalchemy

from mygame.common.model.coord import Coord
from mygame.common.model.unitfactory import UnitFactory
from mygame.common.model.unitinfo import UnitInfo


class DbUnits:
    TABLE = sqlalchemy.Table('units', sqlalchemy.MetaData(),
                             sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column('user_id', None, sqlalchemy.ForeignKey('users.id')),
                             sqlalchemy.Column('game_id', None, sqlalchemy.ForeignKey('games.id')),
                             sqlalchemy.Column('type', sqlalchemy.String(30)),
                             sqlalchemy.Column('coord_x', sqlalchemy.Integer),
                             sqlalchemy.Column('coord_z', sqlalchemy.Integer))

    def __init__(self, engine):
        self.engine = engine

    def get_for_game(self, game_id):
        log = logging.getLogger(__name__)
        log.info(f'Fetching units for game: {game_id}')

        units = []
        with self.engine.connect() as conn:
            select = sqlalchemy.select([DbUnits.TABLE]).where(DbUnits.TABLE.c.game_id == game_id)
            result = conn.execute(select)
            for row in result:
                coord = Coord(row['coord_x'], -row['coord_x'] - row['coord_z'], row['coord_z'])
                unit_info = UnitInfo(row['id'], row['user_id'], row['game_id'], coord)
                unit = UnitFactory.get_unit(row['type'])
                units.append(unit(unit_info))
            result.close()
        return units
