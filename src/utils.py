from urllib.parse import urlparse

from bs4 import BeautifulSoup
from requests import RequestException
from exceptions import ParserFindTagException, RequestError


# Перехват ошибки RequestException.
def get_response(session, url, encoding='utf-8'):
    try:
        response = session.get(url)
        response.encoding = encoding
        return response
    except RequestException as e:
        error_msg = f'Возникла ошибка при загрузке страницы {url}'
        raise RequestError(error_msg)


def get_soup(session, link, parser='lxml'):
    response = get_response(session, link)
    if response is None:
        return None
    soup = BeautifulSoup(response.text, features=parser)
    return soup


# Перехват ошибки поиска тегов.
def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        raise ParserFindTagException(error_msg)
    return searched_tag


def is_relative_url(url):
    parsed_url = urlparse(url)
    return not (parsed_url.scheme and parsed_url.netloc)
