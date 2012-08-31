import unittest
from pyramid import testing
from .testing import DummyAuthenticator, DummyAuthenticationPolicy, DummyAuthorizationPolicy

class LoginTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def _callFUT(self, *args, **kwargs):
        from .api import login
        return login(*args, **kwargs)

    def _register_authenticator(self, authenticator):
        from pyramid.interfaces import IRequest
        from .interfaces import IAuthenticator
        self.config.registry.adapters.register([IRequest], IAuthenticator, "", authenticator)


    def test_it(self):
        self.config.set_authorization_policy(DummyAuthorizationPolicy())
        self.config.set_authentication_policy(DummyAuthenticationPolicy([('X-TESTING-HEADER', 'test')]))
        authenticator = DummyAuthenticator('testing-user')
        self._register_authenticator(authenticator)
        request = testing.DummyRequest()
        identity = {}
        result = self._callFUT(request, identity)

        self.assertEqual(result, 'testing-user')
        self.assertIn('X-TESTING-HEADER', request.response.headers)
