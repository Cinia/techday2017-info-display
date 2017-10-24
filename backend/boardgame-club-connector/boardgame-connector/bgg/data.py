from ._api import BASE_URL

import requests
import logging
from lxml import etree


class Data:
    """ Generic data object for data fetched from the BGG API.
    """

    def fetch_data(self):
        """ Generic data fetch from the BGG API. Should be implemented
        in derived classes.
        """
        raise NotImplementedError

    def do_fetch(self, uri: str, params: dict) -> etree:
        """ Do a GET request to the BGG API.

        :param uri: the URI to request data from
        :param params: URL parameters to add to the request
        :return xml element tree containing the response
        """
        url = BASE_URL + uri
        response = requests.get(url, params=params)
        if response.status_code != 200:
            logging.error("Fetching failed! Status code {}".format(response.status_code))

        data = etree.fromstring(response.content)
        return data
