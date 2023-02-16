import logging
import re
from urllib.parse import urljoin

import requests_cache
from tqdm import tqdm

from configs import configure_argument_parser, configure_logging
from constants import (ALL_VERSIONS, BASE_DIR, DOWNLOADS, EXPECTED_STATUSES,
                       MAIN_DOC_URL, MAIN_PEP_URL)
from outputs import control_output
from utils import find_tag, get_soup

DIFFERENT_STATUSES_MESSAGE = (
    'Несовпадающие статусы "{}". '
    'Статус на общей странице "{}". '
    'Статус на карточке "{}".'
)

NONE_MESSAGE = 'По этому адресу "{}" не удалось получить содержимое.'
LOOKUP_MESSAGE = 'Текст "{}" не найден в  "{}". '
ERROR = 'Сбой в работе программы: {}'
LOGS = []


def pep(session):
    soup = get_soup(session, MAIN_PEP_URL)
    statuses = []
    for row in tqdm(soup.select('#numerical-index tbody tr')):
        _, table_status = row.find('abbr')['title'].split(',')
        url = urljoin(MAIN_PEP_URL, row.find('a')['href'])
        status = get_soup(session, url).find('abbr').text
        statuses.append(status)
        if table_status.strip() not in status:
            LOGS.append(
                DIFFERENT_STATUSES_MESSAGE.format(
                    url, table_status, status
                )
            )
    logging.exception(*LOGS)
    return (
        [('Статус', 'Количество')]
        + [(pattern, statuses.count(pattern)) for pattern in EXPECTED_STATUSES]
        + [('Общее количество', len(statuses))]
    )


def whats_new(session):
    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')
    # soup = get_soup(session, whats_new_url)
    sections_by_python = get_soup(session, whats_new_url).select(
        '#what-s-new-in-python div.toctree-wrapper li.toctree-l1'
    )
    results = [('Ссылка на статью', 'Заголовок', 'Редактор, Автор')]
    for section in tqdm(sections_by_python):
        version_a_tag = section.find('a')
        href = version_a_tag['href']
        version_link = urljoin(whats_new_url, href)
        soup = get_soup(session, version_link)
        results.append(
            (version_link,
             find_tag(soup, 'h1').text,
             find_tag(soup, 'dl').text.replace('\n', ''))
        )
    return results


def latest_versions(session):
    sidebar = find_tag(
        get_soup(session, MAIN_DOC_URL),
        'div', attrs={'class': 'sphinxsidebarwrapper'}
    )
    for ul in sidebar.find_all('ul'):
        if ALL_VERSIONS in ul.text:
            a_tags = ul.find_all('a')
            break
    else:
        raise LookupError(LOOKUP_MESSAGE.format(ALL_VERSIONS, ul.text))
    results = [('Ссылка на документацию', 'Версия', 'Статус')]
    for a_tag in a_tags:
        text_match = re.search(
            r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)',
            a_tag.text
        )
        if text_match is not None:
            version, status = text_match.groups()
        else:
            version, status = a_tag.text, ''
        results.append((a_tag['href'], version, status))
    return results


def download(session):
    downloads_url = urljoin(MAIN_DOC_URL, 'download.html')
    pdf_a4_tag = get_soup(session, downloads_url).select_one(
        'div.body table a[href$="pdf-a4.zip"]'
    )
    archive_url = urljoin(
        downloads_url, pdf_a4_tag['href']
    )
    filename = archive_url.split('/')[-1]
    downloads_dir = BASE_DIR / DOWNLOADS
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename
    response = session.get(archive_url)
    with open(archive_path, 'wb') as file:
        file.write(response.content)
    logging.info(
        f'Архив был загружен и сохранён: {archive_path}'
    )


MODE_TO_FUNCTION = {
    'whats-new': whats_new,
    'latest-versions': latest_versions,
    'download': download,
    'pep': pep
}


def main():
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(f'Аргументы командной строки: {args}')
    session = requests_cache.CachedSession()
    if args.clear_cache:
        session.cache.clear()
    parser_mode = args.mode
    try:
        control_output(MODE_TO_FUNCTION[parser_mode](session), args)
    except Exception as error:
        logging.exception(ERROR.format(error))


if __name__ == '__main__':
    configure_logging()
    logging.info('Парсер запущен!')
    main()
    logging.info('Парсер завершил работу.')
    # whats_new(requests_cache.CachedSession())
