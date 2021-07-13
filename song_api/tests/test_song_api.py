from flask import url_for
from flask_testing import TestCase
from app import app 

class TestBase(TestCase):
    def create_app(self):
        return app 

class TestHome(TestBase):
    def test_get_song(self):
        test_cases = [("Fox Stevenson","ctin", "Bruises"),("Leotrix","uooi", "Sight"),("Sol","baan", "Chasing Stars")]
        for case in test_cases:
            response = self.client.post(url_for('get_song'), json={'artist':case[0], 'random':case[1]})
            self.assertEqual(response.data.decode("utf-8"),case[2])