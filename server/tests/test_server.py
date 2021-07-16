from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///", SECRET_KEY='TEST_KEY', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://artist_api:5000/get_artist', text='Fox Stevenson')
            mocker.get('http://random_api:5000/get_random', text='ctin')
            mocker.post('http://song_api:5000/get_song', text='Bruises')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Listen to Bruises from Fox Stevenson', response.data)