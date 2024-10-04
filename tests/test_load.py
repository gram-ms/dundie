from dundie.core import load
from tests.constants import PEAPLE_FILE
import pytest


@pytest.mark.unit
@pytest.mark.medium
def test_load():
    """Test function load function."""
    assert len(load(PEAPLE_FILE)) == 2
    assert load(PEAPLE_FILE)[0][0] == 'J'
