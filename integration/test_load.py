import pytest
from subprocess import check_output, CalledProcessError


@pytest.mark.integration
@pytest.mark.high
def test_load_positive_call_load_command():
    """test command load"""
    out = (
        check_output(["dundie", "load", "tests/assets/people.csv"])
        .decode("utf-8")
        .split("\n")
    )
    assert len(out) == 2


@pytest.mark.integration
@pytest.mark.high
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_with_wrong_params(wrong_command):
    """test params dundie cli"""
    with pytest.raises(CalledProcessError) as error:
        check_output(
            ["dundie", wrong_command, "tests/assets/people.csv"]
        ).decode("utf-8").split("\n")

    assert "status 2" in str(error.getrepr())
