_rotas = {}


def route(path):
    def decorator(funcao):
        _rotas[path] = funcao
        return funcao

    return decorator


def rotear(path):
    return _rotas[path]


ADMIN = 'ADMIN'
MANAGER = 'MANAGER'
_BD = {ADMIN: ['renzo', 'luis'], MANAGER: ['diego', 'henrique']}


def login_required(group):
    def decorator(funcao):
        def decorada(usuario, *args, **kwargs):
            if usuario in _BD[group]:
                return funcao(usuario, *args, **kwargs)
            return 'Usuario {} nao pode acessar funcao {}'.\
                format(usuario, funcao.__name__)

        return decorada

    return decorator
