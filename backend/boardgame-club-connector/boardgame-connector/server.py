from .boardgame_api import fetch_data
from .boardgame_api import api

import argparse
import logging
from flask import Flask

app = Flask(__name__)
app.register_blueprint(api)

@app.route('/')
def get_root():
    return '{"title": "cLautapelikerho API", "content": "Hello world from cLautapelikerho"}'


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--loglevel', help='Log level', default='INFO', choices=['INFO', 'WARNING', 'DEBUG'])
    parser.add_argument('-p', '--port', help='Port to host in', type=int, default=80)
    args = parser.parse_args()

    logging.basicConfig(format='[%(levelname)s] %(message)s', level=getattr(logging, args.loglevel.upper()))

    fetch_data()

    app.run('0.0.0.0', args.port)

