from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast

app = Flask(__name__)
api = Api(app)

class Weather(Resource):
    def get(self):
        return
    pass



api.add_resource(Weather, '/weather')
if __name__ == '__main__':
    app.run() 

"""REDO WITH FAST API"""