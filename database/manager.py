from abc import ABC, abstractmethod
import sqlalchemy as db

class Manager(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add(self, *args, **kwargs):
        pass

    @abstractmethod
    def remove(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def get(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_all(self, *args, **kwargs):
        pass


class SQLiteManager(Manager):
    def __init__(self, config = dict()):
        super().__init__()
        self.config = config
        self.engine = db.create_engine('sqlite:///' + self.config['sqlite']['url'])
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

    def add(self, *args, **kwargs):
        pass

    def remove(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass

    def get_all(self, *args, **kwargs):
        pass


class MySQLManager(Manager):
    def __init__(self, config=dict()):
        super().__init__()
        self.config = config
        self.engine = db.create_engine('mysql+pymysql://' + self.config['mysql']['user'] + ':' + self.config['mysql']['password'] + '@' + self.config['mysql']['host'] + '/' + self.config['mysql']['database'])
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

    def add(self, *args, **kwargs):
        pass

    def remove(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass

    def get_all(self, *args, **kwargs):
        pass


class PostgreSQLManager(Manager):
    def __init__(self, config):
        super().__init__()

    def add(self, *args, **kwargs):
        pass

    def remove(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass

    def get_all(self, *args, **kwargs):
        pass


class ManagerFactory:
    @staticmethod
    def get_manager(manager_type, config):
        if manager_type == 'sqlite3':
            return SQLiteManager(config)
        elif manager_type == 'mysql':
            return MySQLManager(config)
        elif manager_type == 'postgres':
            return PostgreSQLManager(config)
        else:
            raise Exception('Unknown manager type: {}'.format(manager_type))


