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
    if countvowels(data_sent['random']) == 0:
        song_id = 0
    elif countvowels(data_sent['random']) == 1:
        song_id = 1
    elif countvowels(data_sent['random']) == 2:
        song_id = 2
    else:
        song_id = 3
        
    if data_sent['artist'] == 'Fox Stevenson':
        return Artist[0][song_id]
    elif data_sent['artist'] == 'Sol':
        return Artist[1][song_id]
    elif data_sent['artist'] == 'Unlike Pluto':
        return Artist[2][song_id]
    else:
        return Artist[3][song_id]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)