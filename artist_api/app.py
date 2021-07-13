from flask import Flask 
import random
app = Flask(__name__)

@app.route('/get_artist', methods=['GET'])
def get_animal():
    return random.choice(['Fox Stevenson', 'Sol', 'Unlike Pluto', 'Leotrix'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)