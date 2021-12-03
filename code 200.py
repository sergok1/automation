import requests
import json
from unittest import TestCase, main

 
class TestSomeEndpoint(TestCase):
 
    def test_get_returns_200(self):
        req = requests.get('https://reqres.in/api/single_user')
        self.assertEqual(200, req.status_code, "Code is not 200!")
 
        response_name = req.json()
        self.assertIn("first_name", response_name, "Key not found!")
        self.assertEqual(response_name["first_name"], "Janet", "Key first_name not equal Janet"
        )

 
        print(req.text)
 
 
if __name__ == '__main__':
            main()