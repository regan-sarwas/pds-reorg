import logging

logger = logging.getLogger(__name__)


class Config(object):
    """
    A collection of readonly properties that are initialized at application startup, and passed
    to the various objects and functions to avoid reliance on global variables.
    """
    def __init__(self, moves_db='X:\GIS\ThemeMgr\DataMoves.csv', ref_timestamp=None, remote_server=None, name=None):
        logger.debug("Initializing Config...")
        import config_file
        self.__moves_db = moves_db if moves_db is not None else config_file.moves_db
        self.__ref_timestamp = ref_timestamp if ref_timestamp is not None else config_file.ref_timestamp
        self.__remote_server = remote_server if remote_server is not None else config_file.remote_server
        self.__name = name if name is not None else config_file.name
        logger.debug("Initialized Config: %s", self)

    """
    Moves db path (required, see format elsewhere, | delimited)
    """
    @property
    def moves_db(self):
        return self.__moves_db

    """
    A reference timestamp for the last run (date and time, UTC)
    """
    @property
    def ref_timestamp(self):
        return self.__ref_timestamp

    """
    Path to remote server; UNC or symbolic link
    """
    @property
    def remote_server(self):
        return self.__remote_server

    """
    Short name, e.g. KEFJ
    """
    @property
    def name(self):
        return self.__name

    def __str__(self):
        text = ("<moves_db: {0}, ref_timestamp: {1}, remote_server: {2}, name: {3}>")
        text = text.format(self.moves_db, self.ref_timestamp, self.remote_server, self.name)
        return text