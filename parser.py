import logging

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except requests.exceptions.HTTPError as error:
        logger.exception(error)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    image = soup.find('a', class_='prettyPhotoLink')
    image_link = image['href']
    return image_link


def get_image():
    html = get_html('http://reactor.cc/tag/%D0%AD%D1%80%D0%BE%D1%82%D0%B8%D0%BA%D0%B0')
    return get_page_data(html)
