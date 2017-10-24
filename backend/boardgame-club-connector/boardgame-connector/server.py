from .bgg.plays import Plays

from flask import Flask
import logging
import argparse

app = Flask(__name__)


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--loglevel', help='Log level', default='INFO', choices=['INFO', 'WARNING', 'DEBUG'])
    args = parser.parse_args()

    logging.basicConfig(format='[%(levelname)s] %(message)s', level=getattr(logging, args.loglevel.upper()))

    plays = Plays()
    plays.fetch_data()
