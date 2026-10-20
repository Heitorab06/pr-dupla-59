from usuarios import validar_email


def test_valido():
    assert validar_email("ana@exemplo.com") is True

def test_sem_arroba():
    assert validar_email("ana.exemplo.com") is False

def test_none():
    assert validar_email(None) is False

def test_dominio_incompleto():
    assert validar_email("ana@empresa.") is False

def test_usuario_vazio():
    assert validar_email("@empresa.com") is False