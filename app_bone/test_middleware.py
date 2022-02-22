from werkzeug.wrappers import Request
from flask import request


class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # not Flask request - from werkzeug.wrappers import Request
        # request = Request(environ)
        # print(environ)
        # print('path: %s, url: %s' % (request.path, request.url))
        # just do here everything what you need
        return self.app(environ, start_response)


def middleware_func():
    # print(type(request))
    setattr(request, 'salam', 'poya')
    # print(request.salam)
