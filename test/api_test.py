import unittest
import requests
import threading
import src.main as rest_api

BASE = "http://127.0.0.1:5000/"

class APITest(unittest.TestCase):

    def test_get_request(self):
        response = requests.get(BASE + "helloworld/Adeboye")
        print(response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["age"], 24)
        self.assertEqual(response.json()["gender"], "male")

    def test_post_request(self):
        response = requests.post(BASE + "helloworld/Jonathan/37/male")
        print(response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["age"], 37)
        self.assertEqual(response.json()["gender"], "male")

if __name__ == '__main__':
    unittest.main()
