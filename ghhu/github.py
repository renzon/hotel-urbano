import json

import requests


def avatar(nome):
    r = requests.get('https://api.github.com/users/{nome}'.format(nome=nome))
    js = json.loads(r.text)
    return js['avatar_url']

def repositorios(nome):
    """
    Retornar a lista de repos do usuário
    :param nome: nome do usuário
    :return: list
    """


if __name__ == '__main__':
    print(avatar('renzon'))
