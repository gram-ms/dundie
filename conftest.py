import pytest
from unittest.mock import patch

MARKER = """
unit: mark unit tests
integration: mark integration tests
high: high priority
medium: medium priority
low: low priority
"""


def pytest_configure(config):
    """Obtain the MARKERs const"""
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)


@pytest.fixture(autouse=True)  # autouse = all functions
def go_to_tmpdir(request):
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield  # protocol generetor


@pytest.fixture(autouse=True, scope="function")
def setup_testing_database(request):
    """For each test, create a database file on tmpdir
    force database.py to use that filepath.
    """
    tmpdir = request.getfixturevalue("tmpdir")
    test_db = str(tmpdir.join("database.test.json"))
    with patch("dundie.database.DATABASE_PATH", test_db):
        yield
