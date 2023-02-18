import logging

from bs4 import BeautifulSoup
from requests import RequestException

from exceptions import ParserFindTagException

REQUEST_ERROR = 'Возникла ошибка при загрузке страницы {}'
FIND_TAG_ERROR = 'Не найден тег {} {}'
NONE_MESSAGE = 'По этому адресу "{}" не удалось получить содержимое'


def get_response(session, url, encoding='utf-8'):
    try:
        response = session.get(url)
        response.encoding = encoding
        return response
    except RequestException:
        raise ConnectionError(
            REQUEST_ERROR.format(url)
        )


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=({} if attrs is None else attrs))
    if searched_tag is None:
        raise ParserFindTagException(FIND_TAG_ERROR.format(tag, attrs))
    return searched_tag


def get_soup(session, url, features='lxml'):
    return BeautifulSoup(get_response(session, url).text, features)


def logger(logs, logging=logging.exception):
    for log in logs:
        logging(log)
