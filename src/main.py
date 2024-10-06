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

    def post(self, name, age, gender):
        if name not in names:
            names[name] = {"age": age, "gender": gender}

        return names[name]
    

api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:age>/<string:gender>")

if __name__ == "__main__":
    app.run(debug=True)