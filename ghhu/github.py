import requests


def avatar(nome):
    r = requests.get('https://api.github.com/users/{nome}'.format(nome=nome))
    js = r.json()
    return js['avatar_url']


if __name__ == '__main__':
    print(avatar('renzon'))

