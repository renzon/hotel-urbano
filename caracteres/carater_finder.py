def procurar_char(palavra):
    """
    Procura caracter que contenha palavra em seu nome
    :param palavra: string
    :return: lista com tuplas (caracter, nome do carecter)

    # Encontrar naipes
    >>> procurar_char('suit')
    [('♠','BLACK SPADE SUIT'),('♥','RED HEART SUIT'),('♦','RED DIAMOND SUIT'),('♣','BLACK CLUB SUIT'),('♤','WHITE SPADE SUIT'),('♡','WHITE HEART SUIT'),('♢','WHITE DIAMOND SUIT'),('♧','WHITE CLUB SUIT')]

    # Funciona com palavra do meio
    >>> ('♠','BLACK SPADE SUIT') in procurar_char('spade')
    True

    # Funciona com palavra do inicio
    >>> ('♠','BLACK SPADE SUIT') in procurar_char('Black')
    True

    """
    return 5
