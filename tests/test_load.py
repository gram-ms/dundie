import uuid
from dundie.core import load
from tests.constants import PEAPLE_FILE
import pytest

# fixture for all functions on this file
@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    tmpdir.join('new_file.txt').write('isso é coco,bosta...')


@pytest.mark.unit
@pytest.mark.medium
def test_load():
    """Test function load function."""
    
    with open(f'arquivo_indesejado-{uuid.uuid4()}.txt', "w") as file_:
        file_.write("dados bostas pra tt")

    assert len(load(PEAPLE_FILE)) == 2
    assert load(PEAPLE_FILE)[0][0] == 'J'
