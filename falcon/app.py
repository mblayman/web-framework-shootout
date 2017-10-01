import falcon


class HelloResource:
    def on_get(self, req, resp):
        resp.content_type = 'text/html'
        resp.body = 'Hello World'


app = falcon.API()
hello = HelloResource()
app.add_route('/', hello)
