import functools

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


class login_required:
    @classmethod
    def __init__(self,group):
        self.group = group

    def __call__(self, funcao):
        @functools.wraps(funcao)
        def decorada(usuario, *args, **kwargs):
            if usuario in _BD[self.group]:
                return funcao(usuario, *args, **kwargs)
            return 'Usuario {} nao pode acessar funcao {}'. \
                format(usuario, funcao.__name__)

        return decorada

