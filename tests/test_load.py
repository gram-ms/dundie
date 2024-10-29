import uuid
from dundie.core import load
from tests.constants import PEAPLE_FILE
import pytest


@pytest.mark.unit
@pytest.mark.medium
def test_load_positive_has_2_people():
    """Test function has 2 people."""
    assert len(load(PEAPLE_FILE)) == 2


@pytest.mark.unit
@pytest.mark.medium
def test_load_positive_first_name_starts_with_j():
    """Test function load function."""
    assert load(PEAPLE_FILE)[0][0] == 'J'
