def autheticated_only(method):
    def decorated(*args, **kwargs):
        if check_authenticated(kwargs['user']):
            return method(*args, **kwargs)
        else:
            raise UnauthenticatedError

    return decorated


def authorized_only(method):
    def decorated(*args, **kwargs):
        if check_authorized(kwargs['user'], kwargs['action']):
            return method(*args, **kwargs)
        else:
            raise UnauthorizedError

    return decorated


@authorized_only
@authenticated_only
def execute(action, *args, **kwargs):
    return action()
