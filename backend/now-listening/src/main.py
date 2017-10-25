from flask import Flask, render_template
import requests
import json
import pytz
from datetime import datetime

app = Flask(__name__)

api_key = "ed858d2eca17c6396d503419915e66f6"
endpoint_url = "http://ws.audioscrobbler.com/2.0/"

usernames = ["ireneito", "halliz", "petriairio", "bflorry", "ko-Mik"]

class User:
    username = ""
    userpic = ""
    latestTrack = None
    sortTime = 0

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
        self.setSortTime()

    def render(self):
        dateStr = ""
        # date is not available for curretly playing track
        if "@attr" in self.latestTrack.keys():
            dateStr = "now playing"
        elif "date" in self.latestTrack.keys():
            dt = datetime.utcfromtimestamp(int(self.latestTrack["date"]["uts"])).replace(tzinfo=pytz.utc)
            localZone = pytz.timezone('Europe/Helsinki')
            localTime = localZone.normalize(dt.astimezone(localZone))
            dateStr = localTime.strftime('%d.%m.%Y %H:%M:%S')
        return render_template("user.html", username=self.username, artist=self.latestTrack["artist"]["#text"], \
                     track=self.latestTrack["name"], date=dateStr, imgurl=self.userpic)

    def setSortTime(self):
         if "@attr" in self.latestTrack.keys():
             self.sortTime = float('Inf')
         else:
             self.sortTime = int(self.latestTrack["date"]["uts"])


@app.route("/")
def index():
    result = ""
    users = [User(username) for username in usernames]
    users = sorted(users, key=lambda user: user.sortTime, reverse=True)
    for user in users:
        result += user.render() + "<br/>"
    content = render_template("list.html", listing=result)
    return json.dumps({"title": "Recenlty listened tracks", "content":content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
