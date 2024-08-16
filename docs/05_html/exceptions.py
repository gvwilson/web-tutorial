"""Things that can go wrong."""


class AppException(Exception):
    """Root of exception hierarchy."""

    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


class ModelException(AppException):
    pass


class ViewException(AppException):
    pass
