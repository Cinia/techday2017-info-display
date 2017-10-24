from ._api import USERNAME
from .data import Data

import logging


class Plays(Data):
    """ Data object for played games.
    """

    def __init__(self):
        """ Create a new Plays instance. Use `fetch_data` to get
        plays data from the BGG API.

        Then use the `plays` attribute to access plays.
        """
        self.plays = None

    def fetch_data(self) -> list:
        """ Fetch and parse plays data from BGG API.

        :return a list of `play` objects. Each play has a `length`, `game_name`, an `game_id` and a `comment`
        """
        uri = 'plays'
        params = {'username': USERNAME}
        xml_root = super().do_fetch(uri, params)
        plays = []

        for xml_play in xml_root:
            play = {}

            for xml_play_child in xml_play:
                if xml_play_child.tag == 'item':
                    play['game_name'] = xml_play_child.get('name')
                    play['game_id'] = xml_play_child.get('objectid')
                elif xml_play_child.tag == 'comments':
                    play['comment'] = xml_play[1].text

            play['length'] = xml_play.get('length')
            logging.debug("Play parsed: {}".format(play))

        self.plays = plays

