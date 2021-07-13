from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests 
import os
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db = SQLAlchemy(app)

class songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(20), nullable=False)
    song = db.Column(db.String(20), nullable=False)

@app.route('/')
def home():
    artist = requests.get('http://artist_api:5000/get_artist')
    random = requests.get('http://random_api:5000/get_random')
    song = requests.post('http://song_api:5000/get_song', json={'artist':artist.text, 'random':random.text})
    last_five_songs = songs.query.order_by(desc(songs.id)).limit(5).all()
    db.session.add(songs(artist=artist.text,song=song.text))
    db.session.commit()
    return render_template('index.html', artist=artist.text, song=song.text, last_five_songs=last_five_songs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)