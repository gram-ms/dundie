"""Core for dundie project"""

from dundie.utils.log import get_logger

log = get_logger()


def load(filepath: str):
    """Function that reads a file
    >>> load("assets/peaple.csv")
    Jim Halpert, Sales, Salesman, jim@dundlermifflin.com
    Dwighthrute, Sales, Manager, schrute@dundlermifflin.com
    """
    try:
        """Loads data from filepath to the database"""
        with open(filepath) as file_:
            return file_.readlines()
    except Exception as e:
        log.error(str(e))
        raise
