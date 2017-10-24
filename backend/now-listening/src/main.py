from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

api_key = "ed858d2eca17c6396d503419915e66f6"
endpoint_url = "http://ws.audioscrobbler.com/2.0/"

usernames = ["ireneito", "halliz", "petriairio", "bflorry"]

def getLatestSong(username):
    params = {"user":username, "api_key":api_key, "method":"user.getrecenttracks", "limit":1, "format":"json"}
    res = requests.get(endpoint_url, params=params)
    data = res.json()
    track = data["recenttracks"]["track"][0]
    dateStr = ""
    # date is not available for curretly playing track
    if "@attr" in track.keys():
        dateStr = "now playing"
    elif "date" in track.keys():
        dateStr = track["date"]["#text"]
    return "{user}: {artist} - {track}, {date}".format(user=username, artist=track["artist"]["#text"], track=track["name"], date=dateStr)

@app.route("/")
def index():
    result = ""
    for username in usernames:
        result += getLatestSong(username) + "<br/>"
    return json.dumps({"title": "Recenlty listened tracks", "content":result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
