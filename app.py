from flask import Flask,send_from_directory,render_template
from flask_restful import Resource, Api
from package.person import People, Person
import json


with open('config.json') as data_file:
    config = json.load(data_file)

app = Flask(__name__)
api = Api(app)

api.add_resource(People, '/people')
api.add_resource(Person, '/person/<string:email>')
api.add_resource(Person, '/person/<string:name>')

@app.route('/')
def index():
    return "Hello, This is a Phone dir!"


if __name__ == '__main__':
    app.run(debug=True,host=config['host'],port=config['port'])
