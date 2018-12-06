class SettingDoesNotExist(Exception):
    """Raised if variable is not in settings file."""
    pass


class NotDictException(Exception):
    """Raised if object is not dict."""
    pass


class ContainsDuplicatesException(Exception):
    """Raised if list contains duplicate elements."""
    pass
