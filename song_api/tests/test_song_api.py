from flask import url_for
from flask_testing import TestCase
from app import app 

class TestBase(TestCase):
    def create_app(self):
        return app 

class TestHome(TestBase):
    def test_get_song(self):
        test_cases = [("Rogue","ctin", "Fortress"),("Conro","uooi", "All Eyes On Me"),("Grant","baan", "Move On")]
        for case in test_cases:
            response = self.client.post(url_for('get_song'), json={'artist':case[0], 'random':case[1]})
            self.assertEqual(response.data.decode("utf-8"),case[2])