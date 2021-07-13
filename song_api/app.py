from flask import Flask, request

app = Flask(__name__)

def countvowels(string):
    vowels = 0
    for char in string:
        if char in "aeiou":
            vowels += 1
    return vowels

@app.route('/get_song', methods=['POST'])
def get_song():
    Fox_Stevenson = ["Bruises", "Go Like", "Dreamland", "Ether"]
    Sol = ["Too Much", "Chasing Stars", "I'll Never Change", "So Far Away"]
    Unlike_Pluto = ["Everything Black", "No Scrubs", "JOLT", "Worst in Me"]
    Leotrix = ["brief grip of creation", "TRIP333", "Emoboy303", "Sight"]
    Artist = [Fox_Stevenson, Sol, Unlike_Pluto, Leotrix]
    data_sent = request.get_json()
    song_id = data_sent['random']
    id_num = countvowels(song_id)
    if data_sent['artist'] == 'Fox Stevenson':
        return Artist[0][id_num]
    elif data_sent['artist'] == 'Sol':
        return Artist[1][id_num]
    elif data_sent['artist'] == 'Unlike Pluto':
        return Artist[2][id_num]
    else:
        return Artist[3][id_num]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)