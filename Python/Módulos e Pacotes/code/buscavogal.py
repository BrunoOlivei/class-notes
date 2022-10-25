def procura_vogais(frase: str) -> set:
    """Retorna as vogais encontradas na frase inserida pelo usuário"""
    vogais = set('aeiou')
    return vogais.intersection(set(frase))


def procura_letras(frase: str, letras: str = 'aeiou') -> set:
    """Retorna um cojunto de letras encontradas na frase, ambos informados pelo usuário"""
    return set(letras).intersection(set(frase))
