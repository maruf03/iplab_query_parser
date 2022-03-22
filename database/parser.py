from sqlalchemy import Table, Column, MetaData, Integer, String, Boolean
import sqlalchemy as db
from manager import ManagerFactory

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
        table = db.Table(self.req["model"]["name"], self.manager.metadata, autoload=True, autoload_with=self.manager.engine)
        db.select([table]).where(table.columns.id == self.req["model"]["where"]["id"]).execute()

    def _update(self):
        pass

    def _delete(self):
        pass
    
    def _add(self):
        pass

    def _create_table(self):
        fields = []
        for key in self.req["model"]["schema"].keys():
            fields.append(Column(key, Type[self.req["model"]["schema"][key]]))
        table = Table(
            self.req['model']['name'], 
            self.manager.metadata(),
            Column('id', Integer, primary_key=True),
            *fields)
        return table

    def execute(self):
        if self.req['type'] == 'get':
            self._get()
        elif self.req['type'] == 'update':
            self._update()
        elif self.req['type'] == 'delete':
            self._delete()
        elif self.req['type'] == 'add':
            self._add()
        elif self.req['type'] == 'create':
            self._create_table()
        else:
            raise Exception("Method not allowed")

