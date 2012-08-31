from zope.interface import implementer
from .interfaces import IAuthenticator

@implementer(IAuthenticator)
class DummyAuthenticator(object):
    def __init__(self, username):
        self.username = username

    def authenticate(self, request, identity):
        self.identity = identity
        return self.username

class DummyAuthenticationPolicy(object):
    def __init__(self, headers):
        self.headers = headers

    def remember(self, request, userid):
        return self.headers

class DummyAuthorizationPolicy(object):
    def __init__(self):
        pass
