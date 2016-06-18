import sys

import unicodedata


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
    for n in range(1, sys.maxunicode):
        char = chr(n)
        try:
            char_name = unicodedata.name(char)
        except ValueError:
            pass
        else:
            print(n, char_name)


if __name__ == '__main__':
    print(procurar_char('suit'))
