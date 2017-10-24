from ._api import BASE_URL

import requests
import logging
from lxml import etree


class BggData:
    """ Generic data object for data fetched from the BGG API. The "raw" data (dictionary of data parsed
    from the BGG API accessed with the `data` attribute AFTER data has been fetched from the API using
    `fetch_data`.
    """

    def __init__(self):
        """ Create a new instance of a Data object.
        """
        self.data = None

    def fetch_data(self):
        """ Generic data fetch from the BGG API. Should be implemented
        in derived classes.
        """
        self.data = None
        self.do_fetch_data()

    def do_fetch_data(self):
        """ Must be implemented in derived classes. Should fetch (using request_data)
        and parse data from the BGG API.
        """
        raise NotImplementedError

    @staticmethod
    def request_data(uri: str, params: dict) -> etree:
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
