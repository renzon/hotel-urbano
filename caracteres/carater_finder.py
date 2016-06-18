import sys

import unicodedata
from collections import defaultdict
from functools import lru_cache

_cache = defaultdict(list)


for n in range(1, sys.maxunicode):
    char = chr(n)
    try:
        char_name = unicodedata.name(char)
    except ValueError:
        pass
    else:
        keys = char_name.split()
        for k in keys:
            _cache[k].append((char, char_name))

@lru_cache()
def procurar_char(palavra):
    """
    Procura caracter que contenha palavra em seu nome
    :param palavra: string
    :return: lista com tuplas (caracter, nome do carecter)

    # Encontrar naipes
    >>> all_suit = procurar_char('suit')
    >>> four_suits = {('♤','WHITE SPADE SUIT'),('♡','WHITE HEART SUIT'),('♢','WHITE DIAMOND SUIT'),('♧','WHITE CLUB SUIT')}
    >>> four_suits == set(all_suit).intersection(four_suits)
    True

    # Funciona com palavra do meio
    >>> ('♠','BLACK SPADE SUIT') in procurar_char('spade')
    True

    # Funciona com palavra do inicio
    >>> ('♠','BLACK SPADE SUIT') in procurar_char('Black')
    True

    """
    return _cache[palavra.upper()]


if __name__ == '__main__':
    print(procurar_char('suit'))
