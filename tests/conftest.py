import pytest

MARKER = """
unit: mark unit tests
high: high priority
medium: medium priority
low: low priority
"""

def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line('markers', line)


@pytest.fixture(autouse=True)# autouse = all functions
def go_to_tmpdir(request):
    tmpdir = request.getfixturevalue('tmpdir')
    with tmpdir.as_cwd():
        yield # protocol generetor
        
