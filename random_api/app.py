from flask import Flask
import random
import string
import os

app = Flask(__name__)

@app.route('/get_random', methods=['GET'])
def get_random():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(int(os.getenv('str_len'))))
    return result_str

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)