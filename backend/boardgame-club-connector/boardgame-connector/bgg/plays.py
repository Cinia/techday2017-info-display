from ._api import USERNAME
from .data import Data

import logging


class Plays(Data):
    """ Data object for played games.
    """

    def fetch_data(self):
        """ Fetch and parse plays data from BGG API
        """
        uri = 'plays'
        params = {'username': USERNAME}
        root = super().do_fetch(uri, params)
        for child in root:
            logging.debug(child.tag)
