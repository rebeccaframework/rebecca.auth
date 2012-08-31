from pyramid.httpexceptions import HTTPFound

class Redirect(object):
    """ create view that only redirect to url generated with `route_name`.
    """

    def __init__(self, route_name, **default_values):
        self.route_name = route_name
        self.default_values = default_values

    def __call__(self, request):
        vars = self.default_values.copy()
        vars.update(request.matchdict)
        return HTTPFound(request.route_url(self.route_name, **vars))
