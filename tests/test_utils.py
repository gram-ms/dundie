import pytest
from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize(
    "address",
    [
        "maria.silva@example.com",
        "john_doe123@example.co.uk",
        "nome.sobrenome@exemplo.io",
        "email_teste@domain.travel",
    ],
)
def test_positive_check_valid_email(address):
    """Ensue email is valid."""
    assert check_valid_email(address) is True


@pytest.mark.parametrize(
    "address", ["contato@empresa.+org", "cliente+vip@exemplo.+com.br"]
)
@pytest.mark.unit
def test_negative_check_valid_email(address):
    """Ensue email is not valid."""
    assert check_valid_email(address) is False


@pytest.mark.unit
def test_generate_simple_password():
    """Test generation of random simple passwords
    TODO: Generate hashed complex passwords, encrypit it
    """
    passwords = []
    for _ in range(100):
        passwords.append(generate_simple_password(8))
    assert len(set(passwords)) == 100
