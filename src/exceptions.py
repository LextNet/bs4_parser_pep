
class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class RequestError(Exception):
    """Вызывается, когда парсер не может загрузить страницу."""
    pass
