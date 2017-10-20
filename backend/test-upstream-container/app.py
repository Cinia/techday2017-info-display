import os
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
