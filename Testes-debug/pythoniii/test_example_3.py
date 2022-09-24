from datetime import datetime

from src.example_3 import get_data_atual_e_retorna_periodo

def test_get_data_atual_e_retorna_periodo_manha(mocker):
    mock_now = mocker.patch("src.example_3.datetime")
    mock_now.now.return_value = datetime(2022, 9, 22, 10, 14, 0)
    
    assert get_data_atual_e_retorna_periodo() == "Manhã"
    

def test_get_data_atual_e_retorna_periodo_tarde(mocker):
    mock_now = mocker.patch("src.example_3.datetime")
    mock_now.now.return_value = datetime(2022, 9, 22, 14, 14, 0)
    
    assert get_data_atual_e_retorna_periodo() == "Tarde"
    
    
def test_get_data_atual_e_retorna_periodo_tarde(mocker):
    mock_now = mocker.patch("src.example_3.datetime")
    mock_now.now.return_value = datetime(2022, 9, 22, 20, 14, 0)
    
    assert get_data_atual_e_retorna_periodo() == "Noite"
    

def test_get_data_atual_e_retorna_periodo_none(mocker):
    mock_now = mocker.patch("src.example_3.datetime")
    mock_now.now.return_value = datetime(2022, 9, 22, 0, 14, 0)
    
    assert get_data_atual_e_retorna_periodo() == "Não foi possível identificar o período"
