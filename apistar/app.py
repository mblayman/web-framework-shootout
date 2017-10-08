from apistar import Include, Route, annotate
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar.renderers import HTMLRenderer


@annotate(renderers=[HTMLRenderer()])
def html():
    return 'Hello World'


def json():
    return {'hello': 'world'}


routes = [
    Route('/html', 'GET', html),
    Route('/json', 'GET', json),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.main()
