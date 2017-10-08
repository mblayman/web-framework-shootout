import falcon


class HelloResource:
    def on_get(self, req, resp):
        resp.content_type = 'text/html'
        resp.body = 'Hello World'


class JsonResource:
    def on_get(self, req, resp):
        resp.media = {'hello': 'world'}


app = falcon.API()
app.add_route('/html', HelloResource())
app.add_route('/json', JsonResource())
