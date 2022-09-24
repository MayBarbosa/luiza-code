
from src.example_4 import acessa_google


def test_acessa_google_inacessivel(mocker):
    mock_requests = mocker.patch("src.example_4.requests")
    mock_requests.get.side_effect = Exception
    assert acessa_google() == "Não foi possível acessar o Google"