from flask import Flask 
import random
app = Flask(__name__)

@app.route('/get_artist', methods=['GET'])
def get_artist():
    return random.choice(['Rogue', 'Conro', 'PYLOT', 'Grant'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)