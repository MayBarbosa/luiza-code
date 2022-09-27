from src.example_2 import user_add

def test_valida_usuario_nome_menos_10_caracteres_error(monkeypatch, capsys):
    inputs = iter(["Ana", 27])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    user_add()
    
    result = capsys.readouterr()
    assert result.out == "Nome do usuário deve conter mais de 10 caracteres\n"
    

def test_valida_usuario_existente_error(monkeypatch, capsys):
    inputs = iter(["Michelly Alves", 27])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    monkeypatch.setattr("src.example_2.users", [{"name": "Michelly Alves", "age": 27}])
    
    user_add()
    
    result = capsys.readouterr()
    assert result.out == "Já existe um usuário cadastrado com esse nome\n"
    
    
def test_valida_usuario_menor_18_error(monkeypatch, capsys):
    inputs = iter(["Michelly Alves", 17])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    user_add()
    
    result = capsys.readouterr()
    assert result.out == "Usuário deve ser maior de 18 anos e menor de 100 anos.\n"
    

def test_valida_usuario_maior_100_error(monkeypatch, capsys):
    inputs = iter(["Michelly Alves", 101])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    user_add()
    
    result = capsys.readouterr()
    assert result.out == "Usuário deve ser maior de 18 anos e menor de 100 anos.\n"
    

def test_valida_usuario_success(monkeypatch, capsys):
    inputs = iter(["Michelly Alves", 27])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    user_add()
    
    result = capsys.readouterr()
    assert result.out == "\nUsuário cadastrado com sucesso!\n"