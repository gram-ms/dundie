from dundie.core import load
from tests.constants import PEOPLE_FILE
import pytest


@pytest.mark.unit
@pytest.mark.medium
def test_load_positive_has_2_people(request):
    """Test function has 2 people."""
    assert len(load(PEOPLE_FILE)) == 2


@pytest.mark.unit
@pytest.mark.medium
def test_load_positive_first_name_starts_with_j(request):
    """Test function load function."""
    assert load(PEOPLE_FILE)[0]["name"] == "Jim Halpert"
