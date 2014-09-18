from pyramid.config import Configurator
import views


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('upload', '/upload')
    config.add_route('result', '/result')   
    config.add_route('process', '/process')
    config.add_route('post', '/post')
    config.add_route('form', '/form')
    #config.add_view('form')
    config.add_route('arquivo', '/arquivo')
    config.scan()
    return config.make_wsgi_app()
