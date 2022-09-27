# Método que recebe um número inteiro:
#     - Quando o número for multiplo de 3 ele vai retornar "Multiplo de 3"
#     - Quando o número for multiplo de 5 ele vai retornar "Multiplo de 5"
#     - Se não retorna o próprio número

from pytest import mark, fixture, raises
from src.example import validate_multiplos

@fixture
def minha_fixture():
    """Minha fixture

    Returns:
        _type_: _description_
    """
    return 3


def test_quando_validate_multiplos_recebe_1_retorna_1():
    entrada = 1 # DADO
    esperado = 1 # DADO
    resultado = validate_multiplos(entrada) # QUANDO
    assert resultado == esperado # ENTAO
    
    # assert validate_multiplos(1) == 1
    
@mark.multiplo_5
def test_quando_validate_multiplos_recebe_2_retorna_2():
    assert validate_multiplos(2) == 2
    
def test_quando_validate_multiplos_recebe_3_retorna_multiplo_3():
    assert validate_multiplos(3) == "Multiplo de 3"
    
@mark.multiplo_5
def test_quando_validate_multiplos_recebe_5_retorna_multiplo_5():
    assert validate_multiplos(5) == "Multiplo de 5"
    
@mark.skip
def test_quando_validate_multiplos_recebe_0_retorna_None():
    assert validate_multiplos(0) == None
    
    
@mark.parametrize(
    "entrada",
    [0, 1, 2]
)
def test_quando_validate_multiplos_recebe_numero_retorna_numero(entrada):
    assert validate_multiplos(entrada) == entrada
    

@mark.parametrize(
    "entrada,esperado",
    [(0, 0), (1, 1), (2, 2), (3, "Multiplo de 3"), (5, "Multiplo de 5")]
)
def test_quando_validate_multiplos_recebe_numero_retorna_numero(entrada, esperado):
    assert validate_multiplos(entrada) == esperado
    

def test_valida_multiplos_deve_escrever_caiu_no_metodo(capsys):
    validate_multiplos(0)
    resultado = capsys.readouterr()
    assert resultado.out == "Caiu no método\n"
    
def test_minha_fixture(minha_fixture):
    print(minha_fixture)
    
def test_valida_multiplos_retorna_value_error():
    with raises(ValueError):
        assert validate_multiplos("A") == None