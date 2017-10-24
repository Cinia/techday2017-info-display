from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

api_key = "ed858d2eca17c6396d503419915e66f6"
endpoint_url = "http://ws.audioscrobbler.com/2.0/"

usernames = ["ireneito", "halliz", "petriairio", "bflorry"]

class User:
    username = ""
    userpic = ""
    latestTrack = None

    def __init__(self, username):
        self.username = username
        self.getUserPic()
        self.getLatestSong()

    def getUserPic(self):
        params = {"user":self.username, "api_key":api_key, "method":"user.getInfo", "format":"json"}
        res = requests.get(endpoint_url, params=params)
        data = res.json()
        self.userpic = data["user"]["image"][0]["#text"]
        if (self.userpic is None or len(self.userpic) == 0):
            self.userpic = "http://via.placeholder.com/50x50"


    def getLatestSong(self):
        params = {"user":self.username, "api_key":api_key, "method":"user.getrecenttracks", "limit":1, "format":"json"}
        res = requests.get(endpoint_url, params=params)
        data = res.json()
        self.latestTrack = data["recenttracks"]["track"][0]

    def render(self):
        dateStr = ""
        # date is not available for curretly playing track
        if "@attr" in self.latestTrack.keys():
            dateStr = "now playing"
        elif "date" in self.latestTrack.keys():
            dateStr = self.latestTrack["date"]["#text"]
        return render_template("user.html", username=self.username, artist=self.latestTrack["artist"]["#text"], \
                     track=self.latestTrack["name"], date=dateStr, imgurl=self.userpic)

@app.route("/")
def index():
    result = ""
    for username in usernames:
        user = User(username)
        result += user.render() + "<br/>"
    content = render_template("list.html", listing=result)
    return json.dumps({"title": "Recenlty listened tracks", "content":content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
