from flask import Flask
from flask_restful import Resource, Api
import datetime

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Now(Resource):
    def get(self):
        now = str(datetime.datetime.now())
        return {'current_datetime': now}


api.add_resource(HelloWorld, '/')
api.add_resource(Now, '/now')

if __name__ == '__main__':
    app.run(debug=True)
