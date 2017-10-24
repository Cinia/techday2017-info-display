from .bgg.bgg_data_container import BggDataContainer

from flask import Blueprint, render_template
import logging

api = Blueprint('boargame_api', __name__, template_folder='templates')
container = BggDataContainer()


def fetch_data():
    """ Call to fetch data to the data container.
    """
    logging.info("Fetching data from BGG")
    container.fetch_data()
    logging.info("Data fetched")


@api.route('/plays/latestgames')
def last_played_games():
    games = container.plays.latest_played_games()

    logging.debug("latest games played: {}".format(games))

    html = render_template('game_list.html', games=games).replace('"', '\\"')
    title = 'Latest games played by cLautapelikerho'

    return '{{ "title": "{0}", "content": "{1}" }}'.format(title, html)

