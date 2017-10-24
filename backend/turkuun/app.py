import os
import time
import requests
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def test():
    lastFetch = 0
    try:
        lastFetchString = readFileStr("time")
        lastFetch = int(float(lastFetchString))
    except  (ValueError, IOError):
        lastFetch = 0
        
    fetchAfterS = 1
    currentTime = int(time.time())
    timesince = currentTime - lastFetch
    if timesince >= fetchAfterS:
        r = requests.get('https://rata.digitraffic.fi/api/v1/live-trains/station/JY/TKU?limit=3')
        data = r.json()
        try:
            timetableRows = data[0]["timeTableRows"]
            for v in timetableRows:
                station = v["stationShortCode"]
                if station == "JY":
                    if v["type"] == "DEPARTURE":
                        nextTimeString = v["scheduledTime"]
                        #2017-10-24T17:41:00.000Z
                        splitted = nextTimeString.split('T')
                        splitted = splitted[1].split(":")
                        nextTimeString = splitted[0] + ":" + splitted[1]
                        break
        except:
            nextTimeString = "-"
            
        lastFetch = time.time()
        view = "Seuraava juna Turkuun lähtee: " + nextTimeString
        view = view.encode()
        try:
            overWriteFile("cache", view)
            writeStr = str(lastFetch).encode()
            overWriteFile("time", writeStr)
            
        except (IOError):
            pass
    else :
        view = readFileStr("cache")
    return view

def deleteContent(fd):
    try:
        os.ftruncate(fd, 0)
        os.lseek(fd, 0, os.SEEK_SET)
    except (IOError, ValueError):
        pass

def overWriteFile(filename, overWriteWith):
    fd = os.open(filename, os.O_RDWR|os.O_CREAT)
    deleteContent(fd)
    os.write(fd, overWriteWith)
    os.close(fd)

def readFileStr(filename):
    fd = open(filename, "r")
    readStr = fd.read()
    fd.close()
    return readStr

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
