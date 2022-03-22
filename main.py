import json

from database.parser import Parser


if __name__ == '__main__':
    config = None

    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    with open('tests/create_table.json', 'r') as req_file:
        parser = Parser(config, json.load(req_file))
        parser.execute()
    
    with open('tests/add_student.json', 'r') as req_file:
        parser = Parser(config, json.load(req_file))
        parser.execute()

    with open('tests/get_student.json', 'r') as req_file:
        parser = Parser(config, json.load(req_file))
        parser.execute()

    with open('tests/update_student.json', 'r') as req_file:
        parser = Parser(config, json.load(req_file))
        parser.execute()

    with open('tests/delete_student.json', 'r') as req_file:
        parser = Parser(config, json.load(req_file))
        parser.execute()