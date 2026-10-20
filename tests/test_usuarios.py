from usuarios import validar_email

def test_valido():
    assert validar_email("ana@exemplo.com") is True

def test_sem_arroba():
    assert validar_email("ana.exemplo.com") is False

def test_nao_string():
    assert validar_email(123) is False

def test_arroba_char():
    assert validar_email('@') is False

def test_so_arroba():
    assert validar_email("@") is False

def test_arroba_vazio_antes():
    assert validar_email("@a.com") is False

def test_nulo():
    assert validar_email(None) is False

def test_arroba_vazio_depois():
    assert validar_email("rogerio@") is False

def test_email_sem_dominio():
    assert validar_email("rogerio@gmail") is False