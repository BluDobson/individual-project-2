from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app 

class TestBase(TestCase):
    def create_app(self):
        return app 

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://artist_api:5000/get_artist', text='Fox Stevenson')
            mocker.get('http://random_api:5000/get_random', text='ctin')
            mocker.post('http://song_api:5000/get_song', text='Bruises')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Listen to Bruises from Fox Stevenson', response.data)