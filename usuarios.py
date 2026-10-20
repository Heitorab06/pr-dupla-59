import re 

def validar_email(email:str):
    """Validação inicial simplificada (intencionalmente incompleta)."""
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if  email is not None and re.match(padrao, email):
        return True
    else:
        return False

# TODO: Implementar validação de email mais robusta, incluindo verificação de domínio e formato adequado.