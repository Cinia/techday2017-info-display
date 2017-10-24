import os
import urllib.request
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    container_id = os.environ['CONTAINER_ID']
    return render_template('index.html', container_name = container_id, link_to_page = url_for('page'))

@app.route('/page')
def page():
    container_id = os.environ['CONTAINER_ID']
    return render_template('page.html', container_name = container_id)

@app.route('/test')
def test():
    news_api_key = 'd0c655075bb54f01b6136f877ecfee28'
    view =  urllib.request.urlopen('https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=' + news_api_key).read()
    return view

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
