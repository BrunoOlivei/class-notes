import re
from validate_docbr import CPF

def cpf_valido(num_cpf: str):
    """Valida o cpf

    Args:
        cpf (str): número do cpf

    Returns:
        bool: true se o tamanho do cpf for igual a 11
    """
    cpf = CPF()
    return cpf.validate(num_cpf)

def nome_valido(nome: str):
    """Valida o nome

    Args:
        nome (str): nome do cliente

    Returns:
        bool: true se o nome conter apenas letras
    """

    return nome.isalpha()

def rg_valido(rg: str):
    """Valida o rg

    Args:
        rg (str): número do rg

    Returns:
        bool: true se o tamanho do rg for igual a 9
    """

    return len(rg) == 9

def celular_valido(celular: str):
    """Valida o celular

    Args:
        celular (str): número do celular

    Returns:
        bool: 
    """
    pattern = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    response = re.findall(pattern, celular)
    return response