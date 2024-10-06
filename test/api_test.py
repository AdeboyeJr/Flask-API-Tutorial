import unittest
import requests
import src.main as rest_api

BASE = "http://127.0.0.1:5000/"

class APITest(unittest.TestCase):
    def setup(self):
        self.app = rest_api.app

        self.app.run(debug=True)

    def get_request(self):
        response = requests.get(BASE + "helloworld")
        print(response.json())

        assert response.status_code == 200


