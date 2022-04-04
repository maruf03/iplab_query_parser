import flask
import json
from database.parser import Parser

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/query', methods=['POST'])
def run_query():
    with open('config.json', 'r') as config_file:
        try:
            config = json.load(config_file)
            req = flask.request.get_json()
            parser = Parser(config, req)
            obj = parser.execute()
            
            if obj == True:
                return flask.make_response(flask.jsonify({"status": "success"}), 200)
            elif obj == False:
                return flask.make_response(flask.jsonify({"status": "failure"}), 400)
            else:
                return flask.make_response(flask.jsonify(obj), 200)
        except Exception as e:
            return flask.make_response(flask.jsonify(str(e)), 500)


if __name__ == '__main__':
    app.run()