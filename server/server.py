from pyramid.config import Configurator

def make_app(global_conf, **settings):
    config = Configurator(settings=settings)

    config.add_route('api.play', '/api/play')
    config.add_route('api.quit', '/api/quit')
    config.add_route('api.move', '/api/move')
    config.add_route('api.updates', '/api/updates/{gameid}')

    config.scan('api')

    return config.make_wsgi_app()

if __name__ == '__main__':
    import gevent.monkey; gevent.monkey.patch_all()
    import gevent.pywsgi

    settings = {
    }
    app = make_app({}, **settings)

    listen = 'localhost', 8080
    server = gevent.pywsgi.WSGIServer(listen, app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.kill()