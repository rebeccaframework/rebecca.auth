# import logging
from pyramid import security
from pyramid.interfaces import IRequest
from .interfaces import IAuthenticator

# logger = logging.getLogger(__name__)

def login(request, identity, authenticator_name="", response=None):
    authenticator = get_authenticator(request, name=authenticator_name)
    authorized = authenticator.authenticate(request, identity)
    if not authorized:
        return False

    headers = security.remember(request, authorized)
    if response is None:
        response = request.response

    response.headerlist.extend(headers)
    return authorized

# def logout(request, authenticator_name="", response=None):

#     headers = security.forget(authorized)
#     if response is None:
#         response = request.response

#     response.headerlist.extend(headers)

def get_authenticator(request, name=""):
    reg = request.registry
    authenticator = reg.adapters.lookup([IRequest], IAuthenticator, name=name)
    return authenticator
