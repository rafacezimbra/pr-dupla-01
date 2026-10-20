import re
def validar_email(email:str):
    
    padrao = r"[^@\s]+@[^@\s.]+(?:\.[^@\s.]+)+"
    return isinstance(email, str) and re.fullmatch(padrao, email) is not None

# TODO: Implementar validação de email mais robusta, incluindo verificação de domínio e formato adequado.

