import json

from database.parser import Parser


if __name__ == '__main__':
    req = None
    config = None
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    with open('create_table.json', 'r') as req_file:
        req = json.load(req_file)
    
    parser = Parser(config, req)
    pass