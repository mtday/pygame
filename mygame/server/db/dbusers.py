import logging
import sqlalchemy

from mygame.common.model.user import User


class DbUsers:
    TABLE = sqlalchemy.Table('users', sqlalchemy.MetaData(),
                             sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column('login', sqlalchemy.String(100)))

    def __init__(self, engine):
        self.log = logging.getLogger(__name__)
        self.engine = engine

    def get_by_login(self, login):
        self.log.info('Fetching user with login: {login}')
        user = None
        with self.engine.connect() as conn:
            select = sqlalchemy.select([DbUsers.TABLE]).where(DbUsers.TABLE.c.login == login)
            result = conn.execute(select)
            fetched = result.fetchone()
            if fetched:
                user = User(fetched['id'], fetched['login'])
            result.close()
        return user
