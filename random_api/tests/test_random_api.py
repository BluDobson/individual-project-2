from flask import url_for
from flask_testing import TestCase
from app import app 
import os

class TestBase(TestCase):
    def create_app(self):
        return app 

class TestHome(TestBase):
    def test_get_random(self):
            response = self.client.get(url_for('get_random'))
            length = len(response.data.decode("utf-8"))
            self.assertEqual(length,int(os.getenv('str_len')))
            