from zope.interface import Interface

class IAuthenticator(Interface):
    def authenticate(request, identity):
        """ """
