from sqlalchemy import Table, Column, Integer, String, Boolean, Sequence
import sqlalchemy as db
from sqlalchemy.sql import text
from .manager import ManagerFactory

Type = {
    'int': Integer,
    'string': String,
    'boolean': Boolean
}

class Parser():
    def __init__(self, config, req = dict()):
        self.req = req
        self.manager = ManagerFactory.get_manager(self.req['database'], config)

    def _get(self):
        res = []
        table = db.Table(self.req["model"]["name"], self.manager.metadata, autoload=True, autoload_with=self.manager.engine)
        query = ''
        for key in self.req["model"]["where"].keys():
            query += '{0}.{1} == "{2}"'.format(self.req["model"]["name"], key, self.req["model"]["where"][key])
        
        cursor = None
        if query != '':
            cursor = self.manager.engine.execute(db.select([table]).where(text(query)))
        else:
            cursor = self.manager.engine.execute(db.select([table]))
        
        for row in cursor:
            obj = dict()
            fields = table.columns.keys()
            i = 0
            for field in fields:
                obj[field] = row[i]
                i += 1
            res.append(obj)
        return res

    def _update(self):
        res = []
        table = db.Table(self.req["model"]["name"], self.manager.metadata, autoload=True, autoload_with=self.manager.engine)
        query = ''
        for key in self.req["model"]["where"].keys():
            query += '{0}.{1} == "{2}"'.format(self.req["model"]["name"], key, self.req["model"]["where"][key])
        
        cursor = None
        if query != '':
            cursor = self.manager.engine.execute(db.select([table]).where(text(query)))
        else:
            cursor = self.manager.engine.execute(db.select([table]))
        
        for row in cursor:
            obj = dict()
            fields = table.columns.keys()
            i = 0
            for field in fields:
                obj[field] = row[i]
                i += 1
            res.append(obj)
        return res

    def _delete(self):
        pass
    
    def _add(self):
        table = db.Table(self.req["model"]["name"], self.manager.metadata, autoload=True, autoload_with=self.manager.engine)
        self.manager.engine.execute(db.insert(table).values(self.req["model"]["data"]))
        
    def _create_table(self):
        fields = []
        for key in self.req["model"]["schema"].keys():
            print('{} {}'.format(key, self.req["model"]["schema"][key]))
            fields.append(Column(key, Type[self.req["model"]["schema"][key]]))
        print(fields)
        table = Table(
            self.req['model']['name'], 
            self.manager.metadata,
            Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
            *fields)
        table.create(self.manager.engine)
        return table

    def execute(self):
        if self.req['type'] == 'get':
            return self._get()
        elif self.req['type'] == 'update':
            return self._update()
        elif self.req['type'] == 'delete':
            return self._delete()
        elif self.req['type'] == 'add':
            return self._add()
        elif self.req['type'] == 'create':
            return self._create_table()
        else:
            raise Exception("Method not allowed")

