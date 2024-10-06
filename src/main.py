from flask import Flask
from flask_restful import Api, Resource
import time

app = Flask(__name__)
api = Api(app)

names = {
        "Adeboye": {"age": 24, "gender": "male"},
        "Bill": {"age": 70, "gender": "male"}
        }

class HelloWorld(Resource):
    def get(self, name):
        return names[name]
    

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)