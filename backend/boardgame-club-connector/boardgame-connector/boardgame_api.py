from .bgg_plays import BggPlays

from flask import Blueprint, render_template
import logging

api = Blueprint('boargame_api', __name__, template_folder='templates')
data = BggPlays()


def fetch_data():
    """ Call to fetch data to the data container.
    """
    data.fetch_data()
    data.start_updating()


def stop_updating():
    """ Stop the scheduler thread that is updating plays data.
    """
    data.stop_updating.set()


@api.route('/plays/latestgames')
def last_played_games():
    games = data.latest_played_games()

    logging.debug("latest games played: {}".format(games))

    html = render_template('game_list.html', games=games).replace('"', '\\"')
    title = 'Latest games played by cLautapelikerho'

    return '{{ "title": "{0}", "content": "{1}" }}'.format(title, html)


@api.route('/plays/statistics')
def statistics():
    coop_statistics = data.cooperative_game_statistics()

    logging.debug("coop statistics: {}".format(coop_statistics))

    most_played = data.most_played_game()

    logging.debug("most played game: {}".format(most_played))

    html = render_template('statistics.html', coops=coop_statistics, most_played=most_played).replace('"', '\\"')
    title = 'cLautapelikerho statistics'
    return '{{ "title": "{0}", "content": "{1}" }}'.format(title, html)
