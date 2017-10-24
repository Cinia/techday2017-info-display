from .._api import USERNAME
from ..bgg_data import BggData
from ..errors import *

import logging


class Plays(BggData):
    """ Data object for played games.
    """

    def __init__(self):
        """ Create a new Plays instance. Use `fetch_data` to get
        plays data from the BGG API.

        Then use the `plays` attribute to access plays.
        """
        self.plays = None

    def _get_thumbnail(self, game_id: int) -> str:
        """ Return the thumbnail URL for the given game.

        :param game_id: id of the game in BGG to get thumbnail for
        :return: URL of the thumbnail
        """
        xml_root = BggData.request_data('thing', {'id': game_id})
        for node in xml_root[0]:
            if node.tag == 'thumbnail':
                return node.text

    def do_fetch_data(self):
        """ Fetch and parse plays data from BGG API.

        :return a list of `play` objects. Each play has a `length`, `game_name`, an `game_id` and a `comment`
        """
        uri = 'plays'
        params = {'username': USERNAME}
        xml_root = BggData.request_data(uri, params)
        plays = []

        for xml_play in xml_root:
            play = {}

            for xml_play_child in xml_play:
                if xml_play_child.tag == 'item':
                    play['game_id'] = int(xml_play_child.get('objectid'))
                    play['game_name'] = xml_play_child.get('name')
                    play['game_thumbnail'] = self._get_thumbnail(play['game_id'])
                elif xml_play_child.tag == 'comments':
                    play['comment'] = xml_play[1].text

            play['length'] = int(xml_play.get('length'))
            logging.debug("Play parsed: {}".format(play))

            plays.append(play)

        self.data = plays

    def latest_played_games(self) -> list:
        """ Get the names of games last played as a list.
        """
        if self.data is None:
            raise BggDataError("No data found for latest played games. Maybe it has not been fetched yet.")

        num_games = 10

        return [{'name': play['game_name'], 'thumbnail': play['game_thumbnail']} for play in self.data[:num_games]]
