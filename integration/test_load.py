import pytest

from click.testing import CliRunner
from dundie.cli import load, main
from .constants import PEOPLE_FILE

cmd = CliRunner()


@pytest.mark.integration
@pytest.mark.high
def test_load_positive_call_load_command():
    """test command load"""
    out = cmd.invoke(load, PEOPLE_FILE)
    assert "Dunder mifflin Associates" in out.output


@pytest.mark.integration
@pytest.mark.high
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_with_wrong_params(wrong_command):
    """test params dundie cli"""
    out = cmd.invoke(main, wrong_command, PEOPLE_FILE)
    assert out.exit_code != 0
    assert f"No such command '{wrong_command}'" in out.output
