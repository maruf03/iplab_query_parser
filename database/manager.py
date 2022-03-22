from abc import ABC, abstractmethod
import sqlalchemy as db

class Manager(ABC):
    @abstractmethod
    def __init__(self):
        pass


class SQLiteManager(Manager):
    def __init__(self, config = dict()):
        super().__init__()
        self.config = config
        self.engine = db.create_engine('sqlite:///' + self.config['sqlite']['url'])
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()


class MySQLManager(Manager):
    def __init__(self, config=dict()):
        super().__init__()
        self.config = config
        self.engine = db.create_engine('mysql+pymysql://' + self.config['mysql']['user'] + ':' + self.config['mysql']['password'] + '@' + self.config['mysql']['host'] + '/' + self.config['mysql']['database'])
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()


class PostgreSQLManager(Manager):
    def __init__(self, config):
        super().__init__()
        pass


class ManagerFactory:
    @staticmethod
    def get_manager(manager_type, config):
        if manager_type == 'sqlite':
            return SQLiteManager(config)
        elif manager_type == 'mysql':
            return MySQLManager(config)
        elif manager_type == 'postgres':
            return PostgreSQLManager(config)
        else:
            raise Exception('Unknown manager type: {}'.format(manager_type))


