from .sources import *


class BggDataContainer:
    """ Contains all BGG data available from this API.

    Data is fetched according to the sources defined here and can be accessed
    through the attributes of this container.
    """

    def __init__(self):
        """ Create a new container. This initializes the sources but does not
        yet fetch data.
        """
        self.plays = plays.Plays()

    def __iter__(self):
        """ Iterate sources of this container.
        """
        for attr, value in self.__dict__.items():
            yield value

    def fetch_data(self):
        """ Call to fetch all data from the BGG API.
        """
        for source in self:
            source.fetch_data()
