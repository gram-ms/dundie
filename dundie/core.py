"""Core for dundie project"""

from csv import reader

from dundie.utils.log import get_logger
from dundie.database import connect, commit, add_person

log = get_logger()


def load(filepath: str):
    """Function that reads a file
    >>> load("assets/peaple.csv")
    Jim Halpert, Sales, Salesman, jim@dundlermifflin.com
    Dwighthrute, Sales, Manager, schrute@dundlermifflin.com
    """
    try:
        """Loads data from filepath to the database"""
        csv_data = reader(open(filepath))
    except FileNotFoundError as e:
        log.error(str(e))
        raise e

    db = connect()
    people = []
    headers = ["name", "dept", "role", "email"]
    for line in csv_data:
        person_data = dict(zip(headers, [item.strip() for item in line]))
        pk = person_data.pop("email")
        person, created = add_person(db, pk, person_data)
        return_data = person.copy()
        return_data["created"] = created
        return_data["email"] = pk
        people.append(return_data)

    commit(db)
    return people
