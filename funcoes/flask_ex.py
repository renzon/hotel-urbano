from funcoes import flask_poc
from funcoes.flask_poc import route, login_required, MANAGER, ADMIN

@login_required(MANAGER)
@route('/')
def home(usuario_logado):
    return 'Home Page %s' % usuario_logado


@route('/usuarios')
@login_required
def usuarios(usuario_logado):
    """
    Pagina de usuarios
    :param usuario_logado:
    :return:
    """
    return 'Página de Usuários %s' % usuario_logado


if __name__ == '__main__':

    for path in ['/', '/usuarios']:
        f = flask_poc.rotear(path)
        print(f('renzo'))

    print(home('renzo'))
    print(home('diego'))
    print(usuarios('renzo'))
    print(usuarios('diego'))
    print(usuarios.__name__)
    print(help(usuarios))
    print(usuarios.__closure__[0].cell_contents)
